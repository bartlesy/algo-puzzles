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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal(root):
    if not root:
        return
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    return


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)
    return
