# -*- coding:utf-8 -*-

import sort
import random


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


def main():
    insertion_sort_test()
    # merge_sort_test()
    # bubble_sort_test()


if __name__ == '__main__':
    main()
