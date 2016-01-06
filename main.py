import sort
import random


def Fermat(n):
    fermat = []
    for i in range(n):
        fermat.append(2 ** (2 ** i) + 1)
    return fermat


def main():
    # Insertion-sort
    # a = list(range(2 ** 31))
    a = []
    i = 0
    while i < 2 ** 10:
        a.append(random.randrange(1, 2 ** 10))
        i += 1
    print(a)
    random.shuffle(a)
    sort.insertion_sort(a)
    print(a)

if __name__ == '__main__':
    main()
