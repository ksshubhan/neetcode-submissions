# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Very difficult to understand
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to re order list so it follows:
        # first, last, second, second-last, third, third-last and so on

        # the problem with a singly linked list is that it is difficult to go
        # backwards so we can do this by splitting the list in two and then 
        # reversing the second half

        # this works because we have 1, 2, 3 elements and interleaved are the
        # last, second-last and third-last so if we have 123456
        # and the output is 162543 then we can write this as 1 2 3 6 5 4 
        # and interleave the 6 5 4 in between the 1 2 3

        # so first we need to find the middle of the list
        # which we can do using a slow and fast pointer
        # we have the slow pointer move one a time and the fast pointer 
        # move two at a time
        # because of this by the time and fast pointer reaches the end of the linked list
        # the slow pointer would have only traversed half the list 
        # so whatever the node the slow pointer is pointing to is the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now that we have identified the middle 
        # we can split the list in two
        # we set second = slow.next because we only want the nodes 
        # that come backwards from the end so 4 and 5 not 3 as well
        # because 3 is part of 1 2 3 
        second = slow.next
        
        # here we do the splitting slow.next -> None instead of 4
        # and we set prev to None to allow us to begin reversing the list
        # because currently there is no prev node and we need to start from
        # somewhere
        # so we will have 1-2-3-None, second-4-5-None
        prev = slow.next = None
        
        # now we actually reverse the second list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # now we merge the two lists
        # head points to the start of first half
        # prev points to the start of the second half
        # following the sequence of code tells us how we arrange the nodes
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2