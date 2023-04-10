
numbers = [1, 2, 3, 4, 5]

##map
def square(x):
    return x * x
squared_numbers = list(map(square, numbers))
print(squared_numbers) 

##filter
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers) 

##reduce
from functools import reduce
def multiply(x, y):
    return x * y
product = reduce(multiply, numbers)
print(product) 