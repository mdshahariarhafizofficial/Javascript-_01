import re

txt = "Bangladesh is my country"
x = re.findall("my", txt)
print(x.count("my"))


# Find Email

ptt = "[a-zA-z0-9]+@[a-zA-Z]+\.(com|net|in)"
def isValid(Email):
    if re.search(ptt, Email):
        print("is Valid")
    else:
        print("Not Valid")
isValid("adfhkasfg3556@gmail.com")
isValid("adfhkasfg...@gmail.com")
isValid("345adfhkasfg56@gmail.com")