'''
    Remove Duplicates from Sorted List

    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.

    Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

    Example 2:

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle special case that the list is empty
        if head == None:
            return head
        # Initialize current with the address of head node...
        current = head
        # Traverse the list until the second last node
        while current.next != None:
            # If the value of current is equal to the value of prev...
            # It means the value is present in the linked list...
            if current.val == current.next.val:
                # Hence we do not need to include current again in the linked list...
                # So we increment the value of current...
                tmp = current.next
                current.next = current.next.next
                del tmp
            # Otherwise, we increment the current pointer...
            else:
                current = current.next
        # Return the sorted linked list without any duplicate element...
        return head 