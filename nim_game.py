class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True
        T = [None for _ in range(n + 1)]
        for i in range(4):
            T[i] = True
        for i in range(4, n + 1):
            T[i] = T[i - 1] == False or T[i - 2] == False or T[i - 3] == False
        return T[n]


if __name__ == "__main__":
    sln = Solution()
    for i in range(1, 11):
        print(i)
        print(sln.canWinNim(i))
        print()
