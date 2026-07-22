# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        
        p1, p2 = l1, l2

        while p1 or p2 or carry > 0:
            val1 = 0 if p1 is None else p1.val
            val2 = 0 if p2 is None else p2.val
            total = val1 + val2 + carry
            
            store = total % 10
            carry = total // 10

            tail.next = ListNode(store)
            tail = tail.next 
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return dummy.next
        
        
        
