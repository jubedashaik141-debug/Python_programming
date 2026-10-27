student={"name":"jubeda","age":20,"course":"MCA","CGPA":8.9}
print(student)
#accessing element
print(student["name"])
print(student["course"])
#adding elements
student["lang"]="python"
student["sec"]="A"
print(student)
#updating elements
student["CGPA"]=10
print(student)
#delete an element
del student["CGPA"]
print(student)
