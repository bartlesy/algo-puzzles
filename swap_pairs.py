# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node = head
        prev_node = None

        if head.next:
            head = head.next

        while node:
            node2 = node.next
            if not node2:
                return head
            node.next = node2.next
            node2.next = node

            if prev_node:
                prev_node.next = node2

            prev_node = node
            node = node.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node = head

        if head.next:
            head = head.next
            node.next = self.swapPairs(head.next)
            head.next = node

        return head
