# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.
#
# Example 1:
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?


class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur_len = 0
        peaked = 0
        max_len = 0
        mountain_start = 0

        for i, x in enumerate(A):
            if i < (len(A) - 1):
                if x < A[i + 1] and not mountain_start:
                    mountain_start = 1
            if i == 0:
                continue
            if mountain_start:
                if x < A[i - 1]:
                    if not peaked:
                        peaked = 1
                    cur_len += 1
                if x > A[i - 1]:
                    if not peaked:
                        cur_len += 1
                    else:
                        max_len = max([max_len, cur_len])
                        cur_len = 0
                        mountain_start = 0
        return max_len


def find_peaks(A):
    res = []
    for i, (x, y, z) in enumerate(zip(A, A[1:-1], A[2:])):
        if x < y > z:
            res.append(i + 1)
    return res


def get_mtn_size(A, peak_idx):
    i = peak_idx - 1
    j = peak_idx + 1
    cur_len = 3
    while i > 0:
        i -= 1
        if A[i] < A[i + 1]:
            cur_len += 1
        else:
            break

    while j < (len(A) - 1):
        j += 1
        if A[j] < A[j - 1]:
            cur_len += 1
        else:
            break
    return cur_len


class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peaks = find_peaks(A)
        if not peaks:
            return 0
        return max(map(lambda p: get_mtn_size(A, p), peaks))


if __name__ == "__main__":
    sln = Solution()

    test_cases = [[2, 1, 4, 7, 3, 2, 5], [2, 2, 2], [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]]

    test_res = [5, 0, 11]
    for case, res in zip(test_cases, test_res):
        print(sln.longestMountain(case), res)
