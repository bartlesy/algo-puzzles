#!/usr/bin/env python3
# https://techdevguide.withgoogle.com/paths/foundational/sequence-2/find-longest-word-in-dictionary-that-subsequence-of-given-string/#code-challenge

def word_is_subseq(w, S):
    j = 0
    len_s = len(S)
    for c in w:
        while S[j] != c:
            j += 1
            if j == len_s:
                return False
    return True



def solution(S, D):
    D.sort(key=len, reverse=True)
    for w in D:
        if word_is_subseq(w, S):
            return w
    return None

from copy import deepcopy
from collections import defaultdict

def word_is_subseq2(idx_d, w):
    local_idx_d = deepcopy(idx_d)
    for i, c in enumerate(w):
        idx_list = local_idx_d[c]
        if not idx_list:
            return False
        while idx_list[0] < i:
            idx_list.pop(0)
    return True

def solution2(S, D):
    idx_dict = defaultdict(list)
    for i, c in enumerate(S):
        idx_dict[c].append(i)
    D.sort(key=len, reverse=True)
    for w in D:
        if word_is_subseq2(idx_dict, w):
            return w
    return None


if __name__ == '__main__':
    D = ["able", "ale", "apple", "bale", "kangaroo"]
    S = "abppplee"

    print(solution(S, D))
    print(solution(S, ['weed']))
    print(solution2(S, D))
    print(solution2(S, ['weed']))
