# -*- coding: utf-8 -*-


# 4.2: Implemented simple algorithm of SQUARE MATRIX MULTIPLICATION
def square_matrix_multiply(A, B):
    "4.2: Simple algorithm of SQUARE MATRIX MULTIPLICATION"
    n = len(A)
    C = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# Internal: matrice addition
def _add(A, B):
    "Internal: Addition operation for matrice"
    n = len(A)
    C = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


# 4.2: SQUARE MATRIX MULTIPLICATION - Simple divide-and-conquer
def square_matrix_multiply_recursive(A, B):
    "4.2: Simple divide-and-conquer algorithm of SQUARE MATRIX MULTIPLICATION"
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    C = [[None for j in range(n)] for i in range(n)]
    A_1_1 = [x[:n // 2] for x in A[:n // 2]]
    A_1_2 = [x[n // 2:] for x in A[:n // 2]]
    A_2_1 = [x[:n // 2] for x in A[n // 2:]]
    A_2_2 = [x[n // 2:] for x in A[n // 2:]]
    B_1_1 = [x[:n // 2] for x in B[:n // 2]]
    B_1_2 = [x[n // 2:] for x in B[:n // 2]]
    B_2_1 = [x[:n // 2] for x in B[n // 2:]]
    B_2_2 = [x[n // 2:] for x in B[n // 2:]]
    C_1_1 = _add(square_matrix_multiply_recursive(A_1_1, B_1_1), square_matrix_multiply_recursive(A_1_2, B_2_1))
    C_1_2 = _add(square_matrix_multiply_recursive(A_1_1, B_1_2), square_matrix_multiply_recursive(A_1_2, B_2_2))
    C_2_1 = _add(square_matrix_multiply_recursive(A_2_1, B_1_1), square_matrix_multiply_recursive(A_2_2, B_2_1))
    C_2_2 = _add(square_matrix_multiply_recursive(A_2_1, B_1_2), square_matrix_multiply_recursive(A_2_2, B_2_2))
    for i in range(n // 2):
        C[i][:n // 2] = C_1_1[i]
        C[i][n // 2:] = C_1_2[i]
        C[i + n // 2][:n // 2] = C_2_1[i]
        C[i + n // 2][n // 2:] = C_2_2[i]
    return C


# 4.2: Simple divide-and-conquer - this version implements in-place calculation to
# avoid copying elements to new sub-matrices (resulting to O(n^2) cost)
def multiply_recursive_in_place(C, A, B, C_index_range, A_index_range, B_index_range, size):
    "4.2: Simple divide-and-conquer algorithm of SQUARE MATRIX MULTIPLICATION - inline calculation"
    if size == 1:
        C[C_index_range[0][0]][C_index_range[1][0]] += A[A_index_range[0][0]][A_index_range[1][0]] * B[B_index_range[0][0]][B_index_range[1][0]]
        return C

    # C11 = A11 * B11 + A12 * B21
    C_sub_range = [C_index_range[0][:size // 2], C_index_range[1][:size // 2]]
    A_sub_range = [A_index_range[0][:size // 2], A_index_range[1][:size // 2]]
    B_sub_range = [B_index_range[0][:size // 2], B_index_range[1][:size // 2]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)
    A_sub_range = [A_index_range[0][:size // 2], A_index_range[1][size // 2:]]
    B_sub_range = [B_index_range[0][size // 2:], B_index_range[1][:size // 2]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)

    # C12 = A11 * B12 + A12 * B22
    C_sub_range = [C_index_range[0][:size // 2], C_index_range[1][size // 2:]]
    A_sub_range = [A_index_range[0][:size // 2], A_index_range[1][:size // 2]]
    B_sub_range = [B_index_range[0][:size // 2], B_index_range[1][size // 2:]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)
    A_sub_range = [A_index_range[0][:size // 2], A_index_range[1][size // 2:]]
    B_sub_range = [B_index_range[0][size // 2:], B_index_range[1][size // 2:]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)

    # C21 = A21 * B11 + A22 * B21
    C_sub_range = [C_index_range[0][size // 2:], C_index_range[1][:size // 2]]
    A_sub_range = [A_index_range[0][size // 2:], A_index_range[1][:size // 2]]
    B_sub_range = [B_index_range[0][:size // 2], B_index_range[1][:size // 2]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)
    A_sub_range = [A_index_range[0][size // 2:], A_index_range[1][size // 2:]]
    B_sub_range = [B_index_range[0][size // 2:], B_index_range[1][:size // 2]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)

    # C22 = A21 * B12 + A22 * B22
    C_sub_range = [C_index_range[0][size // 2:], C_index_range[1][size // 2:]]
    A_sub_range = [A_index_range[0][size // 2:], A_index_range[1][:size // 2]]
    B_sub_range = [B_index_range[0][:size // 2], B_index_range[1][size // 2:]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)
    A_sub_range = [A_index_range[0][size // 2:], A_index_range[1][size // 2:]]
    B_sub_range = [B_index_range[0][size // 2:], B_index_range[1][size // 2:]]
    multiply_recursive_in_place(C, A, B, C_sub_range, A_sub_range, B_sub_range, size // 2)

    return C
