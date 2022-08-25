'''
    101. Symmetric Tree

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Example 1:

    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Example 2:

    Input: root = [1,2,2,null,3,null,3]
    Output: false
 

    Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

'''

class Solution():
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:  
        if not root:
            return True;
                # Return the function recursively...
        return self.isSimilar(root.left,root.right)
    
#         For symmetric trees, the left subtree reflection is a mirror of the right subtree
    def isSimilar(self, leftroot, rightroot):
#             If both nodes are null/ nodes are null pointers, return True
        if leftroot and rightroot == None:
            return True
#        If exactly one of them is a null node, return False
        if leftroot or rightroot == None:
            return False
#         If root nodes do not have the same value, return False
        if leftroot.val != rightroot.val:
            return False
        
#       Return true if the values of root nodes are same and left as well as right subtrees are symmetric / on both sides
        return self.isSimilar(leftroot.left,rightroot.right) and self.isSimilar(leftroot.right,rightroot.left)

