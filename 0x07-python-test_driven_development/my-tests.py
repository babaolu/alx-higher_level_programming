#!/usr/bin/python3
#matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[2]],[[2]]))
print("=====")
print(matrix_mul([[1]], [3]))
