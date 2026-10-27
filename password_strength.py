import re
password=input("Enter Password:")
pattern=r'^(?=*[a-z])(?=*[A-Z])(?=*[@#$%^&+=!]).{8,}$'
if re.fullmatch(pattern,password):
    print("Strong Password")
else:
    print("Weak password")
