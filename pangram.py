import string

def isPangram(str1, alphabet = string.ascii_lowercase):
    dict = {}
    for i in alphabet:
        dict[i] = 0
    str1 = str1.lower()
    str1 = str1.replace(" ","")
    for character in str1:
        if(dict[character] == 0):
            dict[character] = 1
    for i in alphabet:
        if(dict[i] == 0):
            print("Not a pangram")
            break;
    else:
        print("Pangram!")
        
pangram = "The quick brown fox jumps over the lazy dog"
isPangram(pangram)
print (pangram) 