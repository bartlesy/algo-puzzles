# Find all possible combinations of k numbers that add up to a number n
# given that only numbers from 1 to 9 can be used and each combination
# should be a unique set of numbers.
#
# Note:
#
#     All numbers will be positive integers.
#     The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#


def combo_sum3(k, n):
    all_nums = list(range(1, 10))
    all_out = []

    def helper(k, n, all_nums, cur_list, all_out=all_out):
        if not k and not n:
            all_out.append(cur_list[:])
        if not k:
            return
        for i, x in enumerate(all_nums):
            if x <= n:
                cur_list.append(x)
                helper(k - 1, n - x, all_nums[i + 1 :], cur_list, all_out)
                cur_list.pop()
        return

    helper(k, n, all_nums, [], all_out)
    return all_out


if __name__ == "__main__":
    print(combo_sum3(3, 9))
    print("should be: [[1,2,6], [1,3,5], [2,3,4]]")
    print(combo_sum3(3, 7))
    print("should be: [[1,2,4]]")
