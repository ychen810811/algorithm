# -*- coding: utf-8 -*-


# 4.2: Implemented traditional algorithm of SQUARE MATRIX MULTIPLICATION
def square_matrix_multiply(A, B):
    "4.2: Traditional algorithm of SQUARE MATRIX MULTIPLICATION"
    n = len(A)
    C = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def square_matrix_multiply_strassen(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
