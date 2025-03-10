class CustomList:
    def __init__(self, capacity=10):
        """
        Initializes a new CustomList with a given capacity.
        If no capacity is provided, it defaults to 10.
        """
        self._capacity = capacity  # Maximum number of elements the list can hold
        self._size = 0  # Keeps track of the current number of elements in the list
        self._array = [None] * self._capacity  # Internal list storage, initially filled with None
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")
    
    def append(self, element):
        """
        Adds an element to the end of the list.
        If the list is full, it resizes automatically to accommodate more elements.
        """
        if self._size >= self._capacity:
            self._resize()  # Resize if the list is at full capacity
        
        self._array[self._size] = element  # Insert the new element at the next available position
        self._size += 1  # Increase the size counter
        print(f"Appended {element} to the list")
    
    def get(self, index):
        """
        Retrieves an element at a specific index.
        If the index is out of range, an error is raised.
        """
        if 0 <= index < self._size:  # Check if the index is within valid range
            return self._array[index]
        raise IndexError("Index out of bounds")  # Error if index is invalid
    
    def set(self, index, element):
        """
        Replaces an existing element at a given index with a new value.
        If the index is invalid, an error is raised.
        """
        if 0 <= index < self._size:  # Check if the index is within bounds
            self._array[index] = element  # Replace the old value with the new element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of bounds")  # Raise an error if index is out of range
    
    def size(self):
        """
        Returns the current number of elements in the list.
        """
        return self._size  # Simply return the size of the list
    
    def _resize(self):
        """
        Doubles the capacity of the list when it reaches full capacity.
        This helps in dynamically handling more elements.
        """
        self._capacity *= 2  # Double the current capacity
        new_array = [None] * self._capacity  # Create a new, larger array
        for i in range(self._size):  # Copy old elements to new array
            new_array[i] = self._array[i]
        self._array = new_array  # Replace the old array with the new larger one
    
    def __repr__(self):
        """
        Returns a string representation of the list containing only stored elements.
        """
        return f"CustomList({self._array[:self._size]})"  # Display only the filled portion of the list

# Example usage demonstrating functionality
custom_list = CustomList()  # Creating a new CustomList

custom_list.append(5)  # Adding an element to the list
print(f"Element at index 0: {custom_list.get(0)}")  # Retrieving the first element

custom_list.set(0, 10)  # Changing the first element to 10
print(f"Element at index 0: {custom_list.get(0)}")  # Printing the modified element

print(f"Current size: {custom_list.size()}")  # Printing the current size of the list
