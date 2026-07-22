# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # The output is in the form of a linked list
        # so we need to create a new linked list for output
        
        # we create a new linked list with the head dummy 
        dummy = ListNode()

        # we initialise a new pointer that initally points to dummy
        # but as we write out output this pointer is going to move
        tail = dummy

        # we initialise a carry value of 0 for addition
        carry = 0
        
        # we initalise pointer to iterate through each linked list
        # one for each linked list of numbers
        p1, p2 = l1, l2

        # the loop continues as long as both pointers are not pointing to 
        # null and the carray is more than 0 
        while p1 or p2 or carry > 0:
            # we intialise two variables to hold our numbers
            # from the linked lists
            # if the pointer points to null we take the value 0 otherwise
            # we take the actual value
            val1 = 0 if p1 is None else p1.val
            val2 = 0 if p2 is None else p2.val

            # we calculate total for those numbers
            total = val1 + val2 + carry
            
            # the store variable holds the value to store in new linked list
            # carry holds the carry value from that addition
            store = total % 10
            carry = total // 10

            # we populate linked list with out result
            tail.next = ListNode(store)
            
            # rather than iterating thorugh list
            # because we are creating it these two statements are swapped 
            # as opposed if we're simply iterating through list
            tail = tail.next 
            
            # if p1 is pointing to None p1.next will yield an error
            if p1:
                p1 = p1.next
            # if p2 is pointing to None p2.next will yield an error
            if p2:
                p2 = p2.next
        
        # we don't include the dummy head we want the one after that 
        # because that is where our linked list actually starts
        return dummy.next
        
        
        
