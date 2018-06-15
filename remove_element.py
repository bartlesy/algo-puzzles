# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n_remove = nums.count(val)
        for _ in range(n_remove):
            nums.remove(val)
        return len(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ptr1 = 0
        ptr2 = 0
        n_vals = nums.count(val)
        if n_vals == len(nums):
            return 0

        while (ptr1 < len(nums)) and (ptr2 < len(nums)):
            while nums[ptr2] != val:
                ptr2 += 1
                # if ptr 2 reaches the last then we can quit
                if ptr2 >= (len(nums) - n_vals):
                    print(nums)
                    return len(nums) - n_vals

            ptr1 = ptr2

            while ptr1 < (len(nums) - 1):
                nums[ptr1] = nums[ptr1 + 1]
                ptr1 += 1
            ptr2 -= 1
        print(nums)
        return len(nums) - n_vals

if __name__ == '__main__':
    sln = Solution()
    print(sln.removeElement([3, 2, 2, 3], 3))
    print(sln.removeElement([0,1,2,2,3,0,4,2], 2))
    print([0, 1, 3, 0, 4])
    print(sln.removeElement([1], 1))
