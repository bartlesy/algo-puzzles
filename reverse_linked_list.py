from utils import build_linked_list, traverse_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        last_node = None
        next_node = node.next
        while node.next:
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node
        node.next = last_node
        return node


if __name__ == "__main__":
    ex_vals = list(range(10))
    ex_ll = build_linked_list(ex_vals)
    traverse_list(ex_ll)
    print()
    print("reversing...")
    print()
    sln = Solution()
    traverse_list(sln.reverseList(ex_ll))
