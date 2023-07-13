
import re

#Find Word
txt = "Bangladesh is my country Bangladesh is my country Bangladesh is my country"
x = re.findall("c", txt)
print(x.count("c"))

# pra = "My name is Fahad"
# a = re.findall("na", pra)
# print(a.count("na")) 


# Varify Email
patt = "[a-zA-z0-9]+@[a-zA-Z]+\.(com|net|in)"
def isValid(email):
    if re.search(patt, email):
        print("Email is Valid")
    else:
        print("Email is not valid")
isValid("mdshahaer@gmail.com")
isValid("mdshahaer415514@gmail.com")