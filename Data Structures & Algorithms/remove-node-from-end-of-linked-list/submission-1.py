# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # There are two parts to solving this
    # first we need to find the nth element from the end 
    # then we need to remove the element
    # to remove the element we need to stop at the element before 
    # and then skip it, to do this we use a dummy node
    # we place the dummy node at the start of the linked list 
    # so instead of the nth element from the end we get the element just before it
    # then we just change the pointer of that element to skip the nth element from the end
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create our dummy node at the start of our linked list head
        dummy = ListNode(0, head)

        # we create two pointers
        p1 = dummy
        p2 = head

        # IMPORTANT: we traverse the linked list with our p2 pointer until 
        # it reaches the nth element
        for i in range(1, n):
            p2 = p2.next
        
        # now here we traverse both pointers 
        # p1 is starting from the dummy node
        # p2 is starting from the nth node
        # when p2 reaches the end of the linked list - None
        # p1 will be pointing to the nth element from the end
        # (the above is very important to understand)
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        # at this point p1 points to the node before the one we want to remove 
        # so now we just update the pointer of p1 to skip p1.next 
        # which is our element to remove
        p1.next = p1.next.next

        # we return dummy.next not dummy because dummy
        # includes the dummy node 0 so instead of 124 we get 0124
        return dummy.next

