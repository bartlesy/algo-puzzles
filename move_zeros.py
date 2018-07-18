
def move_zeros(nums):
    zero = 0
    for i in range(len(nums)):
        if not nums[i] == 0 and zero <= i:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums

print(move_zeros([0, 0, 1]))
print(move_zeros([0, 0, 1, 1, 1]))


