# https://leetcode.com/problems/rotate-list/description/

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(int_list):
    nodes = [ListNode(x) for x in int_list]
    for n1, n2 in zip(nodes, nodes[1:]):
        n1.next = n2
    return nodes[0]


def traverse_list(head):
    node = head
    while node:
        print(node.val)
        node = node.next
    return


# naive solution
def _rotate_right(head, k):
    n_rots = 0
    while n_rots < k:
        node = head
        last_node = None
        while node.next:
            last_node = node
            node = node.next
        node.next = head
        head = node
        last_node.next = None
        n_rots += 1
    return head

# cheap hack to make naive solution workable
# better method would be to just cut off the rotated list and rotate it all
# at once, but effort
def rotate_right(head, k):
    n = 0
    node = head
    while node:
        n += 1
        node = node.next
    return _rotate_right(head, k % n)


# this is the chop and rotate version
def get_linked_list_len(head):
    n = 0
    node = head
    while node:
        n += 1
        node = node.next
    return n


def rotate_right(head, k):
    n = get_linked_list_len(head)
    k_mod_n = k % n
    i = 0
    node = head
    while i < (k_mod_n):
        last_node = node
        node = node.next
        i += 1

    new_head = node
    last_node.next = None

    while node.next:
        node = node.next
    node.next = head

    return new_head



for ex_list, k in [(range(1, 6), 2), (range(3), 4)]:
    ex_head = build_linked_list(ex_list)
    traverse_list(ex_head)
    print()
    traverse_list(rotate_right(ex_head, k))
    print()


