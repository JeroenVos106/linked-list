# Singly Linked List Implementation

This is a Python implementation of a singly linked list data structure.

## Node

The `Node` class represents a single node of the linked list. It has two attributes:

- `data`: holds the data of the node.
- `next_node`: points to the next node in the list.

### Methods

- `__init__(self, data)`: Initializes a new node with the given data.
- `__repr__(self)`: Returns a string representation of the node.

## LinkedList

The `LinkedList` class represents the linked list itself.

### Methods

- `__init__(self)`: Initializes an empty linked list.
- `is_empty(self)`: Checks if the linked list is empty.
- `size(self)`: Returns the number of nodes in the list.
- `add(self, data)`: Adds a new node containing data at the head of the list.
- `search(self, key)`: Searches for the first node containing data that matches the key.
- `insert(self, data, index)`: Inserts a new node containing data at the specified index position.
- `remove(self, key)`: Removes the node containing data that matches the key.

## Usage

```python
# Create a new linked list
my_list = LinkedList()

# Add elements to the list
my_list.add(5)
my_list.add(10)
my_list.add(15)

# Print the list
print(my_list)  # Output: [Head: 15]->[10]->[Tail: 5]

# Search for a node
node = my_list.search(10)
print(node)  # Output: <Node data: 10>

# Remove a node
my_list.remove(10)
print(my_list)  # Output: [Head: 15]->[Tail: 5]

Time Complexity
add: O(1)
search: O(n)
insert: O(n)
remove: O(n)
size: O(n)
```
