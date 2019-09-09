def array123(nums):
    ptr_1 = 0
    ptr_2 = 0
    tar_num = [1, 2, 3]
    while ptr_2 < len(nums):
        if nums[ptr_1] == nums[ptr_2]:
            if nums[ptr_1] == 3:
                return True
            ptr_1 += 1
        ptr_2 += 1
    return False
