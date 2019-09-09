#!/usr/bin/env python3


def all_subsets(nums):
    """
    2^N combinations
    trick is to realize for each number there is a choice w/ 2 options:
        1. include in subnset
        2. exclude in subset
    so, iterate over input and create a copy including this number
    """
    paths = [[]]
    for x in nums:
        # using i in range pattern to keep from modifying array as
        # we're iterating over it - causing an infinite loop
        for i in range(len(paths)):
            paths.append(paths[i][:] + [x])
    return paths


if __name__ == "__main__":
    print(all_subsets([1, 2]))
