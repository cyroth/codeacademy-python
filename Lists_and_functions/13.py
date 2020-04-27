#Modifying each element in a list in a function

n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
# Don't forget to return your new list!
    return x

<<<<<<< HEAD
print (double_list(n))
=======
print(double_list(n))
>>>>>>> 546cb0aea475b47e30c64b4850f8f308dd9e916a
