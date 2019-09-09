class Solution:
    def sum_nodes(self, root):
        if not root:
            return 0
        l_sum = self.sum_nodes(root.left)
        r_sum = self.sum_nodes(root.right)
        return l_sum + r_sum + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node_tilt = abs(self.sum_nodes(root.left) - self.sum_nodes(root.right))
        left_tilt = self.findTilt(root.left)
        right_tilt = self.findTilt(root.right)
        return left_tilt + right_tilt + node_tilt
