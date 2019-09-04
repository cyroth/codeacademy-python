#For your lists
#Write a second for loop that goes through the numbers list and prints each element squared, each on its own line.
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
    print(num)

# Add your loop below!
for num in numbers:
    print("the square of", end=' ')
    print(num, end=' ')
    print("is", end=' ')
    print(num * num)
