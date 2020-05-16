"""
1-2-3-4-5-Null
odd = head
even = head.next
odd.next = even.next
odd = odd.next
even.next = odd.next
even = even.next
1-2-3-4-Null
1-3-Null , 2-4
Input = 1-2-Null ->return same
1-2-3-Null 
1-3,2-Null
1-NULL -> ?
Steps:
1. If odd (repeat till even is Null and even.next is Null)
    odd = head
    even = head.next
    odd.next = even.next
    odd = odd.next
    even.next = odd.next
    even = even.next
2. join odd.next with head of even

Time Complexity = O(N)
Space Complexit = O(1)

 

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        odd = head
        oddHead = head
        even = odd.next
        evenHead = even
        while even != None and even.next !=None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return oddHead
        
        
        
        
        
        
        
        
        
        
        
        
        
