#Напишите функцию для транспонирования матрицы.


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(matrix)
print(trans_matrix)
