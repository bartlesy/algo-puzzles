#!/usr/bin/env python3
def combination_sum(num_list, target):
    all_out = []
    num_list.sort()

    def helper(num_list, target, cur_list):
        if target == 0:
            all_out.append(cur_list[:])
        for i, x in enumerate(num_list):
            if x <= target:
                cur_list.append(x)
                helper(num_list[i:], target - x, cur_list)
                cur_list.pop()
        return
    helper(num_list, target, [])
    return all_out

if __name__ == '__main__':
    print(combination_sum(list(range(1, 10)), 5))
