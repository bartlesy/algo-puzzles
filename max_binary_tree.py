class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        head = TreeNode(max(nums))
        idx = nums.index(head.val)
        head.left = self.constructMaximumBinaryTree(nums[:idx])
        head.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return head
