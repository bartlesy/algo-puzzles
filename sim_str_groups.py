# https://leetcode.com/problems/similar-string-groups/description/
def numSimilarGroups(A):
    out = 0
    for i, x in enumerate(A):
        for y in A[i + 1:]:
            n_diffs = 0
            for c1, c2 in zip(x, y):
                n_diffs += 1 if c1 != c2 else 0
            out += 1 if n_diffs <= 2 else 0
    return out

if __name__ == '__main__':
    print(numSimilarGroups(["tars","rats","arts","star"]))
    print(numSimilarGroups(["blw","bwl","wlb"]))


