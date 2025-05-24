class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head  # Start traversal from the head of the list.
        # Move `current` pointer `index` times to reach the target node.
        for _ in range(index):
            current = current.next
        return current.val  # Return the value stored in the found node.

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:  # Case 1: The list is currently empty.
            self.head = new_node
            self.tail = new_node  # The new node is both the head and the tail.
        else:  # Case 2: The list is not empty.
            new_node.next = self.head  
            self.head = new_node      
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:  # Case 1: The list is currently empty.
            self.head = new_node
            self.tail = new_node  # The new node is both the head and the tail.
        else:  # Case 2: The list is not empty.
            self.tail.next = new_node  
            self.tail = new_node      
        self.size += 1 
 

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return # Do nothing for invalid indices.

        if index == 0:  # Special case: add at the very beginning.
            self.addAtHead(val)
            return
        
        if index == self.size: # Special case: add at the very end.
            self.addAtTail(val)
            return

        # For insertion in the middle (0 < index < size).
        new_node = ListNode(val)
        current = self.head
        # Traverse to the node *before* the insertion point.
        # We need to reach `index - 1` steps from the head.
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        # 'current's `next` pointer should now point to the new node.
        current.next = new_node
        self.size += 1 


    def deleteAtIndex(self, index: int) -> None:
         if index < 0 or index >= self.size:
            return 
        
         if index == 0:  # Special case: deleting the head node.
            self.head = self.head.next 
            if self.size == 1:  
                self.tail = None
            self.size -= 1 
            return
            
         current = self.head
       
         for _ in range(index - 1):
            current = current.next
        
        
         node_to_delete = current.next
        
         current.next = node_to_delete.next
        
        
         if node_to_delete == self.tail:
            self.tail = current  # The new tail is the node *before* the deleted one.
            
         self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)