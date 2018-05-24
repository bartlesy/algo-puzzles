def dfs(nums, cur_res, out_res, i=0):
    print("\t" * i, nums, cur_res, out_res)
    for i, x in enumerate(nums):
        out_res.append(cur_res + [x])
        dfs(nums[i + 1:], cur_res + [x], out_res, i + 1)
    return


def subsets(nums):
    out_res = [[]]
    dfs(nums, [], out_res)
    return out_res


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
