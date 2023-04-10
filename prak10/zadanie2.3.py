def rotate_matrix(matrix):
    return [list(row) for row in zip(*reversed(matrix))]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    print(i)
print()
rotated_matrix = rotate_matrix(matrix)
for i in rotated_matrix:
    print(i)
