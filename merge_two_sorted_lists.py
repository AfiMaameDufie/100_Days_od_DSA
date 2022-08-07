'''
    Merge Two Sorted Lists

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:

    Input: list1 = [], list2 = []
    Output: []
    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.  
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Just take random value and create dummy node 
        
        dummyNode=ListNode(0) 
        tail=dummyNode

        while True:
            
            # when list1 will empty then value of list2 will added to tail
            if list1 is None:
                tail.next = list2
                break
                
            # when list2 will empty then value of list1 will added to tail    
            if list2 is None:
                tail.next = list1
                break
            
            if list1.val<=list2.val:
                
            # small value added to the tail
                tail.next=list1
                list1=list1.next 
                
            #  move forward 
            else:
                tail.next=list2 
            
            # small value added to the tail and then move forward 
                list2=list2.next 
            
            #  move forward 
            tail=tail.next
            
        # because at first we took a random dummy so we don't need that    
        return dummyNode.next              

