'''
    876. Middle of the Linked List
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

    Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100

    I came across Floyd's Cycle Detection Algorithm, also known as Floyd's Tortoise and Hare Algorithm. 
    The idea behind the algorithm is that, if you have two pointers in a linked list, one moving twice as fast (the hare) than the other (the tortoise), 
    then if they intersect, there is a cycle in the linked list. 
    If they don't intersect, then there is no cycle.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Floyd's Tortoise and Hare algorithm
    
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = fast = head
        # while fast and fast.next :
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow


        #         [1, 3, 5, 9, 15]


        pointer = [head]
        while pointer[-1].next:
            pointer.append(pointer[-1].next)
        return pointer[len(pointer) // 2]