# -*- coding:utf-8 -*-


# INSERTION SORT algorithm implementation
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


# Merge function for MERGE SORT algorithm implementation
def merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    L.append(None)
    R.append(None)
    j = k = 0
    for i in range(p, r + 1):
        try:
            if L[j] <= R[k]:
                A[i] = L[j]
                j += 1
            else:
                A[i] = R[k]
                k += 1
        except TypeError as e:
            if L[j] is None:
                A[i:r + 1] = R[k:-1]
                break
            elif R[k] is None:
                A[i:r + 1] = L[j:-1]
                break
            else:
                raise e
