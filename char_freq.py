text=input("Enter String:")
for ch in sorted(set(text)):
    print(ch,"=",text.count(ch))
