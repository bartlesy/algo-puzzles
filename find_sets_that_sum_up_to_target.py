def count_sets(arr, total):
    """
    returns number of subsets that add up to total
    """
    return rec(arr, total, len(arr) - 1)


def rec(arr, total, i):
    """
    return # subsets that add up to total only considering
    arr[:i] elements
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if i < 0:
        return 0
    if total < arr[i]:
        return rec(arr, total, i - 1)
    return rec(arr, total, i - 1) + rec(arr, total - arr[i], i - 1)


def count_sets_dp(arr, total):
    T = [[0 for _ in range(total + 1)] for row in [0] + arr]
    T[0][0] = 1
    for i, x in enumerate([0] + arr):
        for j, b in enumerate(range(total + 1)):
            if i == j == 0:
                continue
            if x > b:
                T[i][j] = T[i - 1][j]
            if x <= b:
                T[i][j] = T[i - 1][j - x] + T[i - 1][j]
    return T[-1][-1]


def count_sets_dp_reuse(arr, total):
    T = [[0 for _ in range(total + 1)] for row in [0] + arr]
    for i, x in enumerate([0] + arr):
        for j, b in enumerate(range(total + 1)):
            if j == 0:
                T[i][j] = 1
            if x > b:
                T[i][j] = T[i - 1][j]
            if x <= b:
                T[i][j] = T[i][j - x] + T[i - 1][j]
    return T[-1][-1]


print(count_sets([2, 4, 6, 10], 16))
print(count_sets([2, 4, 6, 10], 2))
print(count_sets(range(1, 11), 5))
print()
print(count_sets_dp([2, 4, 6, 10], 16))
print(count_sets_dp([2, 4, 6, 10], 2))
print(count_sets_dp(list(range(1, 11)), 5))
print()
print(count_sets_dp_reuse([2, 4, 6, 10], 8))
