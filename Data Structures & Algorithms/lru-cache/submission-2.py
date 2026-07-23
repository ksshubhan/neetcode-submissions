# Very long problem
# Need to verify linking and delinking nodes

# LRU cache problem involves two things:
# 1. find a key quickly 
# 2. re-order items quickly whenever they are used i.e. least/most recently used

# a hash map will solve 1. because self.hash_map[key] is O(1)
# a linked list is good be

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev

            prev_node = self.right.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = self.right
            self.right.prev = node


            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = Node(key, value)
            
            new_node = self.hash_map[key]
            prev_node = self.right.prev

            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.next = self.right
            self.right.prev = new_node
        else:
            self.hash_map[key].val = value

            node = self.hash_map[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev

            prev_node = self.right.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = self.right
            self.right.prev = node


        if len(self.hash_map) > self.capacity:
            node = self.left.next
            
            self.left.next = node.next
            node.next.prev = self.left
            
            self.hash_map.pop(node.key)
        