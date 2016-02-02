# -*- coding: utf-8 -*-

import pprint
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
    A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    B = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    C = matrix.square_matrix_multiply(A, B)
    print(C)


def test_matrix_multiply_strassen():
    A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    B = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    C = matrix.square_matrix_multiply_strassen(A, B)
    pprint.pprint(C)


def test_matrix_multiply_in_place():
    A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    B = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    C = [[0] * 4] * 4
    matrix.multiply_in_place(C, A, B, [[0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 1, 2, 3]], 4)
    print(C)


def main():
    # insertion_sort_test()
    # merge_sort_test()
    # bubble_sort_test()
    # max_subarray_test()
    # max_subarray_time_linear_test()
    # test_matrix_multiply()
    # test_matrix_multiply_strassen()
    test_matrix_multiply_in_place()


if __name__ == '__main__':
    main()
