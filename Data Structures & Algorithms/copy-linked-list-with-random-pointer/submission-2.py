"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Solution:
    # create a copy of every node and store the relationship 
    # original node -> copied node in a hash map
    # connect the copied nodes' next and random pointers

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we need the hash map to store original node -> copied node
        # we initialise the hash map with None because node.next or node.random
        # could point to None i.e. null and if we didn't do this we would get an error
        hash_map = {None: None}
        
        # intialise p1 pointer 
        p1 = head
        
        # while p1 is not pointing to null 
        while p1:
            # store in the hashmap each node and only its value for now
            hash_map[p1] = Node(p1.val)
            # move on to the next node
            p1 = p1.next
        
        # we reset the pointer back to the start of the original list
        # to do our second pass
        p1 = head 
        
        # while p1 pointer is not pointing to null 
        while p1:
            # store the current copied node in another pointer called copy
            # we set copy.next of our new pointer to the copied version 
            # using the hash-map 
            # and the same for random
            copy = hash_map[p1]
            copy.next = hash_map[p1.next]
            copy.random = hash_map[p1.random]
            p1 = p1.next
        
        # we don't return copy because by this pointing copy will be pointing
        # to the end of the list
        # we return hash_map[head] because it points to the first copied node
        return hash_map[head]
        