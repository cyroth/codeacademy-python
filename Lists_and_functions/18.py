#Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results
<<<<<<< HEAD
print (flatten(n))
=======
print(flatten(n))
>>>>>>> 546cb0aea475b47e30c64b4850f8f308dd9e916a
