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
    A1 = []
    A2 = []
    for i in range(20):
        A1.append(random.randrange(1, 2 ** 5))
    for i in range(10):
        A2.append(random.randrange(1, 2 ** 5))
    sort.insertion_sort(A1)
    sort.insertion_sort(A2)
    print(A1)
    print(A2)
    A = A1 + A2
    print(A)
    sort.merge(A, 0, 19, 29)
    print(A)


def main():
    # insertion_sort_test()
    merge_sort_test()


if __name__ == '__main__':
    main()
