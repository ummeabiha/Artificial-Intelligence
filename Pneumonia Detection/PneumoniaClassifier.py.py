import tkinter as tk
from tkinter import filedialog, Label, messagebox
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from PIL import Image, ImageTk
import numpy as np

# Load the model
model_path = "CNN-model-final.h5"  # Update this path to your actual model file
model = load_model(model_path)
classes = ['Normal Pneumonia', 'Bacterial Pneumonia', 'Viral Pneumonia']

# Function to check if the image is a valid X-ray
def is_valid_xray(image_path):
    try:
        img = Image.open(image_path)
        img.verify()
        if img.mode != 'L' or img.size[0] < 100 or img.size[1] < 100:
            return False
        return True
    except Exception as e:
        print(f"Invalid X-ray: {e}")
        return False

# Define the image classification function
def classify_image(image_path, model):
    img = load_img(image_path, target_size=(255, 255))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = prediction[0][class_index]
    return img, classes[class_index], confidence

# Define the GUI
class PneumoniaDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pneumonia Type Classifier")
        self.root.configure(bg="#000000")  # Black background
        self.root.geometry("500x650")

        # Create a frame to hold all components
        self.frame = tk.Frame(root, bg="#000000")
        self.frame.pack(expand=True)  

        # Title label
        self.title_label = tk.Label(
            self.frame, text="Pneumonia Type Classifier", font=("Arial", 26, "bold"), fg="#ffffff", bg="#000000"
        )
        self.title_label.pack(pady=(20, 10))

        # Image display area
        self.img_label = Label(self.frame, bg="#000000")  # Add dimensions for the image label
        self.img_label.pack(pady=10)

        # Prediction result area
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 16), fg="#ffffff", bg="#000000")
        self.result_label.pack(pady=10)

        # Upload button with padding
        self.upload_button = tk.Button(
            self.frame, text="Upload X-ray", command=self.upload_image, font=("Arial", 14),
            bg="#1F1F1E", fg="#ffffff"
        )
        self.upload_button.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            if not is_valid_xray(file_path):
                messagebox.showerror("Invalid Image", "The uploaded file is not a valid X-ray image.")
                self.result_label.config(text="Invalid X-ray image.", fg="#EE2A41")
                self.img_label.config(image="")  # Clear any previous image
                return

            img = Image.open(file_path)
            img = img.resize((220, 220))  # Resize image for display
            img = ImageTk.PhotoImage(img)
            self.img_label.configure(image=img)
            self.img_label.image = img

            _, prediction, confidence = classify_image(file_path, model)
            self.result_label.config(
                text=f"Prediction: {prediction}\n\nConfidence: {confidence:.2f}", fg="#ffffff"
            )

# Create the application window
root = tk.Tk()
app = PneumoniaDetectorApp(root)
root.mainloop()
