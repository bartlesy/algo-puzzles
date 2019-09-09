def merge(nums1, m, nums2, n):
    res_set = []
    sub_list1 = nums1[:m]
    res_idx = 0
    i = 0
    j = 0
    while res_idx < (m + n) and i < m and j < n:
        if sub_list1[i] <= nums2[j]:
            res_set.append(sub_list1[i])
            i += 1
            res_idx += 1
        else:
            res_set.append(nums2[j])
            j += 1
            res_idx += 1
    if j == n:
        res_set += sub_list1[i:]
    if i == m:
        res_set += nums2[j:]

    for i, x in enumerate(res_set):
        nums1[i] = x
    return
