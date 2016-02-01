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


# 4.2: SQUARE MATRIX MULTIPLICATION - Strassen algorithm
def square_matrix_multiply_strassen(A, B):
    "4.2: Strassen algorithm of SQUARE MATRIX MULTIPLICATION"
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    C = [[None] * n] * n
    A_1_1 = [x[:n // 2] for x in A[:n // 2]]
    A_1_2 = [x[n // 2:] for x in A[:n // 2]]
    A_2_1 = [x[:n // 2] for x in A[n // 2:]]
    A_2_2 = [x[n // 2:] for x in A[n // 2:]]
    B_1_1 = [x[:n // 2] for x in B[:n // 2]]
    B_1_2 = [x[n // 2:] for x in B[:n // 2]]
    B_2_1 = [x[:n // 2] for x in B[n // 2:]]
    B_2_2 = [x[n // 2:] for x in B[n // 2:]]
    C_1_1 =