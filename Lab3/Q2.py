def is_pangram(sentence):
    alph= 'abcdefghijklmnopqrstuvwxyz'.split()
    if (sentence == alph):
        return True
    return False

sentence= input("Enter a sentence: ")

if(is_pangram(sentence.lower().split())):
    print("'"+ sentence + "' is a panagram")
else:
    print("'"+ sentence + "' is not a panagram")


