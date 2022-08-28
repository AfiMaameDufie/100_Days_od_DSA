'''
    108. Convert Sorted Array to Binary Search Tree

    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


    Example 1:

    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

    Example 2:

    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

    Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
'''

'''
Method: recursion

Since nums is a sorted list, the middle element nums[len(nums)//2] must be the root node of nums.
Thus, after setting the middle element be the root, finding the middle element in the left subarry nums[:len(nums)//2] and right subarry nums[len(nums)//2 + 1 : ]

For example, nums = [0, 1, 2, 3, 4, 5, 6, 7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         Checking length total num

        total_nums = len(nums)
        
#         If it is null return None
        if not total_nums:
            return None
        
#         Finding the mid node
        mid = total_nums // 2
        
        return TreeNode(
            nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:])
        )


# Algo Complexity
# Time Complexity: O(n log n)
# Space Complexity: O(n)