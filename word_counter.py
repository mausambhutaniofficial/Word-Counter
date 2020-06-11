#SIMPLE CODE TO GET THE COUNT OF WORDS IN YOUR NAME OR ANY STRING

def word_counter(string):
    counter={}
    for char in string.lower():
        counter[char]=string.lower().count(char)
    return counter

string=input("enter a string ") 
print(word_counter(string))