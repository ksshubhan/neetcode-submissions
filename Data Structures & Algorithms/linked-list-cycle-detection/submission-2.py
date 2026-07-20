# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Required understanding of Floyds hare and tortoise algorithm
    # we can detect a cycle in a linked list by establishing a slow and past pointer
    # the slow pointer will move one at at time and the fast pointer will move two 
    # at a time
    # if these pointers point at the same node it means a cycle is present
    # look at notion for more detail
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # intialise our slow(p1) and fast(p2) pointers 
        # to point to the head of the same linked list
        p1 ,p2 = head, head

        # IMPORTANT: 
        # python evaluates conditions in order
        # if p2 is null it means we have reached the end and there is no cycle
        # if this is not the case it maybe the case that p2.next is null
        # these depend if the list is odd or even in length
        # and it works because if we evaluate p2 being null then we exit while loop
        # python won't bother checking the second condition which is good 
        # because None.next woudl return an error
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            # if pointers point to the same node we have found a cycle 
            if p1 == p2:
                return True
        
        # if we end up exiting loop then it means there was no cycle
        return False
