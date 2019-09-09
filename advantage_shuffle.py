"""
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
"""
from collections import defaultdict, Counter


class Solution:
    def get_next_ele(self, idx_lu, target):
        min_advs = list(filter(lambda x: x > target, idx_lu))
        if min_advs:
            return min(min_advs)
        return min(idx_lu)

    def update_ele(self, idx_lu, ele):
        idx_lu[ele] -= 1
        if not idx_lu[ele]:
            del idx_lu[ele]
        return

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        idx_lu = Counter(A)

        out = []
        for i, b in enumerate(B):
            next_ele = self.get_next_ele(idx_lu, b)
            self.update_ele(idx_lu, next_ele)
            out.append(next_ele)
        return out


if __name__ == "__main__":
    sln = Solution()
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    print(sln.advantageCount(A, B))
    print("should be", [2, 11, 7, 15])
    A = [2, 0, 4, 1, 2]
    B = [1, 3, 0, 0, 2]
    print(sln.advantageCount(A, B))
    print("should be", [2, 0, 2, 1, 4])
