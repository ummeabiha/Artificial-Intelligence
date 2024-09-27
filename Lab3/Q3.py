def sort_hyphen(sentence):
    sentence.sort()
    return '-'.join(sentence)

sentence= input("Enter a sentence: ").split('-')
print("Sorted Sentence: " , sort_hyphen(sentence))