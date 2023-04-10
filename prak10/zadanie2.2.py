my_list = [2, 4, 7, 8, 10]
print(any(num % 3 == 0 for num in my_list))
print(all(num % 2 == 0 for num in my_list))