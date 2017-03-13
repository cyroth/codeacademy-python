#For your hobbies
#Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.
hobbies = []

# Add your code below!
print "enter 3 hobbies one at a time"
for count in range(3):
    hobby = str(raw_input("Your hobby: "))
    hobbies.append(hobby)
print "---------------"
print "list of hobbies"
print hobbies
