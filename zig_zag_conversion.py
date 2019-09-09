# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        out_rows = [[] for _ in range(numRows)]
        down = True
        out_row = 0

        for i, c in enumerate(s):
            out_rows[out_row].append(c)
            if i and out_row in [0, numRows - 1]:
                down = not down

            if down:
                out_row += 1

            else:
                out_row -= 1

        return "".join(map("".join, out_rows))


if __name__ == "__main__":
    sln = Solution()
    print(sln.convert("PAYPALISHIRING", 4))
    print("PINALSIGYAHRPI")
    print(sln.convert("PAYPALISHIRING", 3))
    print("PAHNAPLSIIGYIR")
    print(sln.convert("AB", 1))
    print("AB")
