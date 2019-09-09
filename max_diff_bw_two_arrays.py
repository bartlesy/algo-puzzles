# want an O(N) solution for finding the two elements with the max diff in arrays
arr1 = [1, 9, 10, 3]
arr2 = [11, 10, 4, 6]


def get_mins_maxs(arr):
    min1 = float("inf")
    min2 = float("inf")
    max1 = float("-inf")
    max2 = float("-inf")
    for x in arr:
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    return min1, min2, max1, max2


def max_diffs_bw_elements(arr1, arr2):
    arr2_extremes = get_mins_maxs(arr2)
    arr1_res = []
    for i, x in enumerate(arr1):
        min1, min2, max1, max2 = arr2_extremes
        if arr2[i] == max1:
            max1 = max2
        if arr2[i] == min1:
            min1 = min2
        arr1_res.append(abs(max([x - max1, x - min1], key=abs)))
    return arr1_res


def max_diffs(arr1, arr2):
    return max_diffs_bw_elements(arr1, arr2), max_diffs_bw_elements(arr2, arr1)


print(max_diffs(arr1, arr2))
print(max_diffs([10, 10, 1, 1], [1, 1, 10, 10]))
