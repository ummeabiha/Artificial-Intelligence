courses = {"MAD": 4, "CCN": 4, "SQE": 3, "SPM": 3, "ECOM" : 3}
max_marks = 100

def get_marks():
    marks = {}
    for course in courses:
        score = float(input(f"Enter marks for {course}: "))
        marks[course] = (score, get_grade(score))
    return marks

def get_grade(marks):
    grading_scale = [(94, 'A+'), (85, 'A'), (80, 'A-'), 
    (75, 'B+'),(70, 'B'), (67, 'B-'), (64, 'C+'), (60, 'C'),
    (57, 'C-'), (54, 'D+'), (50, 'D'), (0, 'Fail')]
    for threshold, grade in grading_scale:
        if marks >= threshold: return grade

def calc_gpa(marks):
    grade_points = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.4, 
        'B': 3.0, 'B-': 2.7, 'C+': 2.4, 'C': 2.0, 'C-': 1.7, 
        'D+': 1.3,'D': 1.0, 'Fail': 0.0}
    total_points, total_credits = 0, 0

    for course, (score, grade) in marks.items():
        credits = courses[course]
        total_points += grade_points[grade] * credits
        total_credits += credits
    return total_points / total_credits if total_credits > 0 else 0

def print_marksheet(name, roll, marks, total, perc, overall_grade, gpa):
    print("\n==================== Marksheet ====================")
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print("--------------------------------------------------")
    print("Course\t\tMarks\tGrade")
    for course, (score, grade) in marks.items():
        print(f"{course}\t\t{score}\t{grade}")
    print("--------------------------------------------------")
    print(f"Total Marks: {total}")
    print(f"Percentage: {perc:.2f}%")
    print(f"Grade: {overall_grade}")
    print(f"GPA: {gpa:.2f}")
    print("==================================================")


name = input("Enter student's name: ")
roll = input(f"Enter {name}'s roll number: ")
marks = get_marks()
total = sum(score for score, _ in marks.values())
perc = (total / (len(courses) * max_marks)) * 100
overall_grade = get_grade(perc)
gpa = calc_gpa(marks)
print_marksheet(name, roll, marks, total, perc, overall_grade, gpa)


