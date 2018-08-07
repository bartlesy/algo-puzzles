# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
#
# For example, given a 3-ary tree:
#
#
#
#
# Return its postorder traversal as: [5,6,3,2,4,1].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        out_list = []
        def traverse(root, out_list):
            if not root:
                return
            for child in root.children:
                traverse(child, out_list)
            out_list.append(root.val)
            return
        traverse(root, out_list)
        return out_list

    def postorder(self, root):
        if not root:
            return []
        stack = [root]
        visited = []
        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)
            visited.append(node.val)
        return visited[::-1]


