age = input("Please enter your age: ")
print(type(age))
# input() function would take the value and convert it in string type
age = eval(age)  # converts the value from string to its original form
print(age, type(age))

if age >= 18:
    print("please go ahead and vote")
else:
    print("come back later")

# so it means eval only convert string only to original form ?
# eval converts to only numbers ? will it convert to date as well
