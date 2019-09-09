from collections import deque


def get_final_str(in_str):
    out_str = []
    for i, c in enumerate(in_str):
        if c == "#":
            if out_str:
                out_str.pop()
        else:
            out_str.append(c)
    return "".join(out_str)


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return get_final_str(S) == get_final_str(T)


if __name__ == "__main__":
    test_cases = [
        ({"S": "a##c", "T": "#a#c"}, True),
        ({"S": "a#c", "T": "b"}, False),
    ]

    sln = Solution()

    for case, res in test_cases:
        print(sln.backspaceCompare(**case), res)
