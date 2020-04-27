#Passing a range into a function

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

<<<<<<< HEAD
print (my_function(range(0,3))) # Add your range between the parentheses!
=======
print(my_function(list(range(0,3)))) # Add your range between the parentheses!
>>>>>>> 546cb0aea475b47e30c64b4850f8f308dd9e916a
