def matrix_operation(matrix1, matrix2, operation):
    """
    Выполняет операцию над двумя матрицами.

    matrix1 - первая матрица.
    matrix2 - вторая матрица.
    operation - символ операции ('+', '-', '*').
    """
    result = []
    for i, row1 in enumerate(matrix1):
        row_result = []
        for j, element1 in enumerate(row1):
            element2 = matrix2[i][j]
            if operation == '+':
                element_result = element1 + element2
            elif operation == '-':
                element_result = element1 - element2
            elif operation == '*':
                element_result = element1 * element2
            else:
                raise ValueError("Неверный символ операции")
            row_result.append(element_result)
        result.append(row_result)
    return result
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
addition_result = matrix_operation(matrix1, matrix2, '+')
subtraction_result = matrix_operation(matrix1, matrix2, '-')
multiplication_result = matrix_operation(matrix1, matrix2, '*')
print("Матрица 1 :")
for row in matrix1:
    print(row)
    
print("Матрица 2 :")
for row in matrix2:
    print(row)

print("Результат сложения:")
for row in addition_result:
    print(row)

print("Результат вычитания:")
for row in subtraction_result:
    print(row)

print("Результат умножения:")
for row in multiplication_result:
    print(row)

for row in matrix_operation(matrix1, matrix2, input('символ:')):
    print(row)
