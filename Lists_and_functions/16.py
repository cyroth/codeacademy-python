#Using strings in lists in functions
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    result = ""
    result = x+y
    return result
<<<<<<< HEAD
print (join_lists(m, n))
=======
print(join_lists(m, n))
>>>>>>> 546cb0aea475b47e30c64b4850f8f308dd9e916a
# You want this to print [1, 2, 3, 4, 5, 6]
