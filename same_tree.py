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

                # If both trees are empty then return true...
        if p == None and q == None:
            return True
        # If one of the tree is empty and the other is not then return false...
        elif p == None or q == None:
            return False
        # If the value of p tree is equal to the value of q tree...
        elif p.val == q.val:
            # continue to judge the value of the left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If the value is different, false is returned
        return False
    

# Algorithm Complexity
# Time : O(N)
# Space : O(N)