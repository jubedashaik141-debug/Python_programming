f=open("leap_year.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

with open("leap_year.txt") as f:
    print(f.read(3))
    print(f.readline())
    print(f.readlines())
