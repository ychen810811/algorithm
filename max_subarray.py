# -*- coding: utf-8 -*-


# 4.1: Max subarray crossing mid-point function for MAX SUBARRAY algorithm
def max_cross_subarray(A, low, mid, high):
    left_sum = float('-inf')
    tmp = 0
    for i in range(mid, low - 1, -1):
        tmp += A[i]
        if tmp > left_sum:
            left_sum = tmp
            left_index_max = i

    right_sum = float('-inf')
    tmp = 0
    for j in range(mid + 1, high + 1):
        tmp += A[j]
        if tmp > right_sum:
            right_sum = tmp
            right_index_max = j

    return (left_index_max, right_index_max, left_sum + right_sum)


# 4.1: for sort method: key function
def _tupple_element_2(t):
    return t[2]


# 4.1: MAX SUBARRAY algorithm
def max_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])

    candidate_left = max_subarray(A, low, (low + high) // 2)
    candidate_right = max_subarray(A, (low + high) // 2 + 1, high)
    candidate_cross = max_cross_subarray(A, low, (low + high) // 2, high)
    candidate_list = [candidate_left, candidate_right, candidate_cross]
    candidate_list.sort(key=_tupple_element_2, reverse=True)
    return max(candidate_list, key=_tupple_element_2)


# 4.1-5: MAX SUBARRAY algorithm in linear time, but its space complexity is O(n) rather than O(1)
def max_subarray_time_linear(A, low, high):
    max_subarray_at_index = [(low, low, A[low])]
    for i in range(low + 1, high + 1):
        if max_subarray_at_index[i - 1][2] < 0:
            max_subarray_at_index.append((i, i, A[i]))
        else:
            max_subarray_at_index.append((max_subarray_at_index[i - 1][0], i, max_subarray_at_index[i - 1][2] + A[i]))

    max_subarray = max_subarray_at_index[0]
    for i in range(low + 1, high + 1):
        if max_subarray_at_index[i][2] > max_subarray[2]:
            max_subarray = max_subarray_at_index[i]

    return max_subarray
