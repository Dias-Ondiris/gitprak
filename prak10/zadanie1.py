import random
import string
import math

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def capitalize_string(string):
    return string.capitalize()

def reverse_string(string):
    return string[::-1]

def count_occurrences(string, substring):
    return string.count(substring)

def square_root(number):
    return math.sqrt(number)

def absolute_value(number):
    return abs(number)

def is_even(number):
    return number % 2 == 0

def is_alpha(string):
    return string.isalpha()

def sort_list(list):
    return sorted(list)

def sum_list(list):
    return sum(list)

random_string = generate_random_string(10)
capitalized_string = capitalize_string(random_string)
reversed_string = reverse_string(capitalized_string)
occurrences = count_occurrences(reversed_string+"AAA", 'A')
square_root_value = square_root(occurrences)
absolute_value_number = absolute_value(square_root_value)
is_even_boolean = is_even(absolute_value_number)
list_of_numbers = [2, 4, 6, 8, 10]
sorted_list = sort_list(list_of_numbers)
sum_of_numbers = sum_list(sorted_list)

print(f"Random string: {random_string}")
print(f"Capitalized string: {capitalized_string}")
print(f"Reversed string: {reversed_string}")
print(f"Occurrences of 'A': {occurrences}")
print(f"Square root: {square_root_value}")
print(f"Absolute value: {absolute_value_number}")
print(f"Is even: {is_even_boolean}")
print(f"Sorted list: {sorted_list}")
print(f"Sum of numbers: {sum_of_numbers}")