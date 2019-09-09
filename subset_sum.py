def subset_sum(arr, tar):
    T = [[False for _ in range(tar + 1)] for __ in range(len(arr) + 1)]

    T[0][0] = True
    for i, x in enumerate(arr):
        for sub_tar in range(tar + 1):
            if x <= sub_tar:
                T[i + 1][sub_tar] = ((T[i][sub_tar - x]) and True) or (
                    T[i][sub_tar]
                )
            else:
                T[i + 1][sub_tar] = T[i][sub_tar]

    return T[-1][-1]


print(subset_sum([1, 2, 3], 5))
