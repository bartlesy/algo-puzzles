#
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length at most 12.
# S will consist only of letters or digits.

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        paths = [S.lower()]
        for i, c in enumerate(S):
            if c.isalpha():
                for j in range(len(paths)):
                    path = list(paths[j][:])
                    path[i] = c.upper()
                    paths.append(''.join(path[:]))
        return paths


if __name__ == '__main__':
    sln = Solution()
    print(sln.letterCasePermutation('3z4'))
    print(sln.letterCasePermutation('a1b2'))





