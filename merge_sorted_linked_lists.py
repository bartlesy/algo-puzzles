# https://leetcode.com/problems/merge-two-sorted-lists/description/

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    cur_node = head

    while l1 and l2:
        if l1.val < l2.val:
            cur_node.next = l1
            l1 = l1.next
        else:
            cur_node.next = l2
            l2 = l2.next
        cur_node = cur_node.next
    if l1:
        cur_node.next = l1
    if l2:
        cur_node.next = l2
    return head

