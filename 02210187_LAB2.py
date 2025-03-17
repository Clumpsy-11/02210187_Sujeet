class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Helps with efficient appends
        self._size = 0
        print("Created new LinkedList")
        print(f"Current size: {self._size}")
        print(f"Head: {self.head}")
    
    def append(self, element):
        """Add element to the end of the list"""
        new_node = Node(element)
        
        # Empty list case
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # Regular case - add to end
            self.tail.next = new_node
            self.tail = new_node
            
        self._size += 1
        print(f"Appended {element} to the list")
    
    def get(self, index):
        """Get element at index position"""
        # Check bounds
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return None
            
        # Traverse to the node
        current = self.head
        for _ in range(index):  # Use _ since we don't use the counter
            current = current.next
            
        print(f"Element at index {index}: {current.data}")
        return current.data
    
    def set(self, index, element):
        """Change element at index position"""
        # Check bounds
        if index < 0 or index >= self._size:
            print("Index out of bounds")
            return
            
        # Find the node
        current = self.head
        for _ in range(index):
            current = current.next
            
        # Update the data
        current.data = element
        print(f"Set element at index {index} to {element}")
    
    def size(self):
        """Return number of elements in the list"""
        print(f"Current size: {self._size}")
        return self._size
    
    def prepend(self, element):
        """Add element to the beginning of the list"""
        new_node = Node(element)
        
        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self._size += 1
        print(f"Prepended {element} to the list")
    
    def print_list(self):
        """Print all elements in the list"""
        if not self.head:
            print("Linked list: []")
            return
        
        # Build string representation
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
            
        print(f"Linked list: [{' '.join(elements)}]")


# Test the implementation
if __name__ == "__main__":
    # Create a new list
    my_list = LinkedList()
    
    # Test basic operations
    my_list.append(5)
    my_list.get(0)
    my_list.set(0, 10)
    my_list.get(0)
    my_list.size()
    my_list.prepend(10)
    my_list.print_list()  