import re
pan=input("Enter PAN number:")
if re.fullmatch(r'[A-Z]{5}[0-9]{4}[A-Z]',pan):
    print("valid pan")
else:
    print("Invalid PAN")
