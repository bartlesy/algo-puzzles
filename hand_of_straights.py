# https://leetcode.com/problems/hand-of-straights/description/
# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
#
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
def build_straight(hand, W):
    straight = []
    tar_card = min(hand)
    straight.append(tar_card)
    hand.remove(tar_card)
    while len(straight) < W:
        tar_card = tar_card + 1
        if tar_card not in hand:
            return False
        hand.remove(tar_card)
        straight.append(tar_card)
    return True


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if not hand:
            return False
        if len(hand) % W:
            return False
        hand.sort()
        while hand:
            res = build_straight(hand, W)
        return res


if __name__ == '__main__':
    sln = Solution()
    tests = [
        ([1,2,3,6,2,3,4,7,8], 3, True),
        ([1, 2, 3, 4, 5], 4, False)
    ]
    for hand, W, res in tests:
        print(res, sln.isNStraightHand(hand, W))
