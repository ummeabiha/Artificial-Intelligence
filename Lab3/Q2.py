def is_pangram(sentence):
    alph = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(filter(str.isalpha, sentence.lower()))
    return alph <= sentence_set

sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print(f"'{sentence}' is a pangram")
else:
    print(f"'{sentence}' is not a pangram")
