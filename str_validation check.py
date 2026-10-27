roll_no="MCA077"
print(roll_no.isalnum())
print(roll_no.isdigit())

text=input("enter age:")
if text.isdigit():
    age=int(text)
    print("valid number:",age)
else:
    print("digits only please")


print("programme:",roll_no[:3])
print("roll_number:",roll_no[3:])

    
