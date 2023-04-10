string = input("Введите строку: ")
unique_chars = []
for char in string:
    if char not in unique_chars:
        unique_chars.append(char)
unique_chars.sort()
print("Уникальные символы в строке:")
for char in unique_chars:
    print(char, end=" ")