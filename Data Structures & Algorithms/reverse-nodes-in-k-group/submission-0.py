# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        curr = head 

        while curr is not None:

            for i in range(k):
                if curr is None:
                    return dummy.next
                curr = curr.next

            current = head
            prev = curr
            while current != curr:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            tail.next = prev
            tail = head
            
            head = curr

        return dummy.next
