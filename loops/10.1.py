#For your hobbies
hobbies = []

# Add your code below!
counter = 0
print("enter 3 hobbies one at a time")
while counter < 3:
    hobby = str(input("Your hobby: "))
    hobbies.append(hobby)
    counter += 1
print("---------------")
print("list of hobbies")
print(hobbies)
