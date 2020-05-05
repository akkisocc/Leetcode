# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast!=None :
            slow = slow.next
            if fast.next is None:
                break
            fast = fast.next.next
            
        return slow
        
        
        
