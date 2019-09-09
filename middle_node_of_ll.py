# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        middle = head
        middle_i = 0
        node = head
        while node:
            node = node.next
            i += 1
            if middle_i < i // 2:
                middle_i += 1
                middle = middle.next
        return middle
