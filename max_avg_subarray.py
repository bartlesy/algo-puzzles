"""
https://leetcode.com/problems/maximum-average-subarray-i/description/

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""


def findMaxAverage(nums, k):
    if not nums:
        return nums
    T = [float("-inf") for _ in nums]
    cur_sum = 0
    for i, x in enumerate(nums):
        if i < (k - 1):
            cur_sum += x
        elif i == (k - 1):
            cur_sum += x
            T[i] = cur_sum / k
        else:
            cur_sum -= nums[i - k]
            cur_sum += x
            T[i] = cur_sum / k
    return max(T)


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
