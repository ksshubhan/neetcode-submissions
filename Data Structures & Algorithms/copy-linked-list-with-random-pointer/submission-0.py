"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}
        p1 = head
        while p1:
            hash_map[p1] = Node(p1.val)
            p1 = p1.next
        
        p1 = head 
        
        while p1:
            copy = hash_map[p1]
            copy.next = hash_map[p1.next]
            copy.random = hash_map[p1.random]
            p1 = p1.next
        
        return hash_map[head]
        