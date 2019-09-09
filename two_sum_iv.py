class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tar_nums = set()

        def traverse(root, k):
            if not root:
                return False
            rem = k - root.val
            if root.val in tar_nums:
                return True
            tar_nums.add(rem)
            l_res = traverse(root.left, k)
            r_res = traverse(root.right, k)
            return l_res or r_res

        return traverse(root, k)
