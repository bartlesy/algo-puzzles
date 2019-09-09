# https://leetcode.com/problems/merge-k-sorted-lists/description/


def get_min_element(lists):
    cur_min = float("inf")
    min_ele = None
    for i, x in enumerate(lists):
        if x.val < cur_min:
            cur_min = x.val
            min_ele = i
    return min_ele


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = list(filter(None, lists))
        if not lists:
            return []
        node_idx = get_min_element(lists)
        node = lists[node_idx]
        head = node
        lists[node_idx] = lists[node_idx].next
        cur_node = node
        lists = list(filter(None, lists))
        while lists:
            node_idx = get_min_element(lists)
            node = lists[node_idx]
            cur_node.next = node
            lists[node_idx] = lists[node_idx].next
            cur_node = node
            lists = list(filter(None, lists))
        return head
