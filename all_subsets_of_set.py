

def all_subsets(nums):
    out = [[]]
    for x in nums:
        tmp = []
        for path in out:
            tmp.append(path[:] + [x])
        out.extend(tmp)
    return out

print(all_subsets([1, 2, 3]))


