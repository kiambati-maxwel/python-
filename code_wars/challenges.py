def pig_it(text):
    #your code here
    split_space = text.split()
    str = ""
    
    for word in split_space:
        messed_word = word[1:] + word[0] + "ay"
        str = str + " " + messed_word
    
    if len(split_space[-1]) == 1:
        return str[:-2]
    return str

print(pig_it("Hello you there"))

word = 'hello'

def pig(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
x
