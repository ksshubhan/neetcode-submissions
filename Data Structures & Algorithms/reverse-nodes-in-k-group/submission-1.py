# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # initialise a dummy node
        dummy = ListNode(0, head)

        # intialise a tail pointer that points to dummy
        tail = dummy

        # intialise a pointer that points to head
        curr = head 

        # while there is at least one node left try process another group
        while curr is not None:
            # iterate to find the next k group of nodes to reverse    
            for i in range(k):
                # if there are no nodes left to form a group
                # we do not reverse and leave the rest of the nodes as they 
                # are and stop
                if curr is None:
                    # we return our finished linked list
                    return dummy.next
                # otherwise we move on to the next node
                curr = curr.next

            # if we have reached here then it means we have found a group of nodes
            # to reverse

            # intialise current pointer to head
            current = head
            # initialise new pointer prev to curr
            prev = curr

            # reversal code from re order linked lists
            while current != curr:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            # once we have reversed the group the pointers no longer point
            # in the correct places to continue
            
            # before reversal tail will point to the node before current group
            # we want to tail to point to first node of reversed group
            # which will be prev
            tail.next = prev

            # then we want tail to point to node at the end of the reverse group
            tail = head
            
            # then head will point to the first node after the reversed group 
            head = curr

        # if we reach here then there are no more reversals to make
        # having reach end of linked list so we return our final linked list
        return dummy.next
