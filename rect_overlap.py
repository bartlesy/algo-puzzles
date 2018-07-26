# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
#
# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two (axis-aligned) rectangles, return whether they overlap.
#
# Example 1:
#
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:
#
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Notes:
#
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.

from itertools import combinations
def rec_area(rec):
    bottom = min([rec[1], rec[3]])
    top = max([rec[1], rec[3]])
    left = min([rec[0], rec[2]])
    right = max([rec[0], rec[2]])
    return abs(top - bottom) * abs(right - left)

def overlap_area(rec1, rec2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """
    bottom = max([rec1[1], rec2[1]])
    left = max([rec1[0], rec2[0]])
    right = min([rec1[2], rec2[2]])
    top = min([rec1[3], rec2[3]])
    overlap_width = right - left
    overlap_height = top - bottom
    return overlap_width * overlap_height

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        bottom = max([rec1[1], rec2[1]])
        left = max([rec1[0], rec2[0]])
        right = min([rec1[2], rec2[2]])
        top = min([rec1[3], rec2[3]])
        overlap_width = right - left
        overlap_height = top - bottom
        return (overlap_width > 0) and (overlap_height > 0)

# overlap 2
# We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.
#
# Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
# Example 2:
#
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
# Note:
#
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
    def rectangleArea(self, rectangles):
        tot_area = sum(map(rec_area, rectangles))
        for rec1, rec2 in filter(lambda x: self.isRectangleOverlap(*x), combinations(rectangles, 2)):
            tot_area -= overlap_area(rec1, rec2)
        return tot_area % (10 ^ 9 + 7)


if __name__ == '__main__':
    sln = Solution()
    print(sln.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]), True)
    print(sln.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]), False)
    print(sln.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
    print(sln.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3]]))
