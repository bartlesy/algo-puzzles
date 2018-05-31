class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        best_i = 0
        best_j = 0
        max_len = 1
        max_idxs = {}
        max_idxs[s[0]] = 0

        cur_i = 0
        cur_j = 0
        while cur_j < len(s):
            # print(f"""s: {s}, cur_i: {cur_i}, cur_j: {cur_j}, sub_str: {s[cur_i:cur_j + 1]}, max_len: {max_len}, {max_idxs}""")
            c1 = s[cur_i]
            c2 = s[cur_j]

            if (cur_i <= max_idxs.get(c2, float('-inf')) < cur_j):
                max_len = max([max_len, cur_j - cur_i])
                cur_i = max_idxs[c2] + 1

            max_idxs[c2] = cur_j
            cur_j += 1

        max_len = max([max_len, cur_j - cur_i])
        return max_len


if __name__ == '__main__':
    sln = Solution()
    print(sln.lengthOfLongestSubstring('aaaaa'))
    print(sln.lengthOfLongestSubstring('abcbb'))
    print(sln.lengthOfLongestSubstring('aaabbb'))
