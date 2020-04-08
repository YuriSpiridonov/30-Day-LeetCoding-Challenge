"""
Task 8:
    Given a non-empty, singly linked list with head node head, 
    return a middle node of linked list.
    If there are two middle nodes, return the second middle node.
    Example:
    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  
    (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and 
    ans.next.next.next = NULL.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #def middleNode(self, head: ListNode) -> ListNode:
    def middleNode(head):    
        tick = False
        half = head
        while head:
            head = head.next
            if tick:
                half = half.next
            tick = not tick
        return half
