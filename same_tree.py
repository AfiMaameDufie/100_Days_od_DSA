'''
    100. Same Tree

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


    Example 1:

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:

    Input: p = [1,2], q = [1,null,2]
    Output: false
'''

# Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

#         Checking to see if p and q are both None
        if not p and not q:
            return True
#         one of p and q is None
        if not q or not p:
            return False
        
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    

# Algorithm Complexity
# Time : O(N)
# Space : O(N)