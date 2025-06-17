"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            if node.child:
                original_next = node.next
                node.next = self.flatten(node.child)
                node.child.prev = node
                node.child = None
                while node.next:
                    node = node.next
                node.next = original_next
                if original_next:
                    original_next.prev = node
                    
            node = node.next
        return head
