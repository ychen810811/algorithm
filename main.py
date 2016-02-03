# -*- coding: utf-8 -*-

import sort
import max_subarray
import random
import matrix


def Fermat(n):
    fermat = []
    for i in range(n):
        fermat.append(2 ** (2 ** i) + 1)
    return fermat


def insertion_sort_test():
    A = [random.randrange(0, 2 ** 10) for i in range(2 ** 20)]
    sort.insertion_sort(A)


def merge_sort_test():
    A = [random.randrange(0, 2 ** 10) for i in range(2 ** 20)]
    sort.merge_sort(A, 0, len(A) - 1)


def bubble_sort_test():
    A = [random.randrange(1, 2 ** 10) for i in range(24)]
    print(A)
    sort.bubble_sort(A)
    print(A)


def max_subarray_test():
    A = [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print('Left: %s, Right: %s, sum: %s' % max_subarray.max_subarray(A, 0, 16))


def max_subarray_time_linear_test():
    A = [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print('Left: %s, Right: %s, sum: %s' % max_subarray.max_subarray_time_linear(A, 0, 16))


def test_matrix_multiply():
    A = [[1, 3, 2, 1], [4, 6, 1, 3], [5, 8, 9, 4], [1, 3, 3, 6]]
    B = [[1, 5, 6, 9], [2, 4, 1, 6], [3, 3, 7, 5], [4, 1, 8, 4]]
    C = matrix.square_matrix_multiply(A, B)
    print(C)


def test_matrix_multiply_recursive():
    A = [[1, 3, 2, 1], [4, 6, 1, 3], [5, 8, 9, 4], [1, 3, 3, 6]]
    B = [[1, 5, 6, 9], [2, 4, 1, 6], [3, 3, 7, 5], [4, 1, 8, 4]]
    C = matrix.square_matrix_multiply_recursive(A, B)
    print(C)


def test_matrix_multiply_recursive_in_place():
    C = [[0 for j in range(4)] for i in range(4)]
    A = [[1, 3, 2, 1], [4, 6, 1, 3], [5, 8, 9, 4], [1, 3, 3, 6]]
    B = [[1, 5, 6, 9], [2, 4, 1, 6], [3, 3, 7, 5], [4, 1, 8, 4]]
    size = len(C)
    idx_range = [list(range(size)), list(range(size))]
    matrix.multiply_recursive_in_place(C, A, B, idx_range, idx_range, idx_range, size)
    print(C)


def main():
    # insertion_sort_test()
    # merge_sort_test()
    # bubble_sort_test()
    # max_subarray_test()
    # max_subarray_time_linear_test()
    test_matrix_multiply()
    test_matrix_multiply_recursive()
    test_matrix_multiply_recursive_in_place()


if __name__ == '__main__':
    main()
