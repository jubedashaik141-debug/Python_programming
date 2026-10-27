import re
aadhar=input("enter aadhar number:")
if re.fullmatch(r'\d{12}',aadhar):
    print("valid Aadhar")
else:
    pirnt("Invalid aadhar")
