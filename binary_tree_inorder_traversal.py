'''
    Binary Tree Inorder Traversal
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Example 2:
    Input: root = []
    Output: []

    Example 3:

    Input: root = [1]
    Output: [1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        
        def Inorder(root):
#      Check if root is None, if True, return
            if(root==None):
                return 
#      Check if the left side of root is not None, append root.left  
            if(Inorder(root.left)!= None):
                self.res.append(root.left)
#      then set the root to val  
            self.res.append(root.val)
#      If root.right is not None, append root.right
            if(Inorder(root.right)!= None):
                self.res.append(root.right)
        Inorder(root)
#      return the new inorder traversal
        return self.res
    

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def Inorder(root):
            if not root: return

            Inorder(root.left)
            res.append(root.val)
            Inorder(root.right)

        Inorder(root)
        return res

# DFS Traversal Solutions:

# Pre-Order (Root, Left, Right)
# In-Order (Left, Root, Right)
# Post-Order (Left, Root, Right)