name="penguin"
age=38
weight=104
is_student=True
#printing different variables and their data type
print("Name:",name)
print("Data Type of Name is", type(name))

print("Age:",age)
print("Data Type of Age is", type(age))

print("Weight:",weight)
print("Data Type of Weight is", type(weight))

print("is_student:",is_student)
print("Data Type of is_student is", type(is_student))

#Type casting to convert the datatypes of variables
print("\n After type Casting...")
age=str(age)
print(age)
print("Data Type for Age is",type(age))
print(weight)
print("Data Type of Weight is", type(weight))
weight=int(weight)