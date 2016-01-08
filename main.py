# -*- coding:utf-8 -*-

import sort
import random


def Fermat(n):
    fermat = []
    for i in range(n):
        fermat.append(2 ** (2 ** i) + 1)
    return fermat


def insertion_sort_test():
    a = []
    i = 0
    while i < 2 ** 10:
        a.append(random.randrange(1, 2 ** 10))
        i += 1
    print(a)
    random.shuffle(a)
    sort.insertion_sort(a)
    print(a)


def merge_sort_test():
    A = []
    for i in range(2 ** 10):
        A.append(random.randrange(1, 2 ** 10))
    print(A)
    sort.merge_sort(A, 0, len(A) - 1)
    print(A)


def main():
    # insertion_sort_test()
    merge_sort_test()


if __name__ == '__main__':
    main()
