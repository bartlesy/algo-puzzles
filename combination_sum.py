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


def combo_sum(num_list, target):
    out_list = []
    num_list.sort()

    def helper(num_list, target, cur_list, out_list=out_list):
        if target == 0:
            out_list.append(cur_list[:])
            return
        for i, x in enumerate(num_list):
            if x <= target:
                cur_list.append(x)
                helper(num_list[i:], target - x, cur_list, out_list)
                cur_list.pop()
        return
    helper(num_list, target, [], out_list)
    return out_list


if __name__ == '__main__':
    print(combination_sum(list(range(1, 10)), 5))
    print(combo_sum(list(range(1, 10)), 5))



