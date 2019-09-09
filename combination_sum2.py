class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res_set = []

        def helper(cur_nums, full_nums, tar, res_list):
            if tar == 0:
                if cur_nums not in res_set:
                    res_set.append(cur_nums[:])

            for i, x in enumerate(full_nums):
                if x <= tar:
                    cur_nums.append(x)
                    helper(cur_nums, full_nums[(i + 1) :], tar - x, res_list)
                    cur_nums.pop()

        helper([], candidates, target, res_set)
        return res_set
