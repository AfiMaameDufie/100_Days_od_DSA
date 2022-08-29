'''
    110. Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def height(root):
            if not root:
                return 0
            return 1 +  max(height(root.left), height(root.right))
        left,right=height(root.left),height(root.right)
        if abs(left - right) <=1:
            return True and self.isBalanced(root.left) and self.isBalanced(root.right)
        return False


# Algorithm Complexity
# O(nlogn)