class Node():
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList():
    """
    Singly Linked List
    """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time.
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """
        Adds a new Node containing data at the head of the list.
        Takes O(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Returns the node or 'None' if not found.
        
        Takes O(n) time.
        """
        
        current = self.head
        
        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Now containing data at index position.
        Insertion takes O(1) time, 
        but finding the node at the insertion position takes O(n) time.
        
        Takes overall O(n) time.
        """
        
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = Node.next_node
                position -= 1
        
        prev_node = current
        next_node = current.next_node
        
        prev_node.next_node = new
        new.next_nodee= next_node
        
    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node	
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current    
        
    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        
        nodes = []
        current = self.head                                                             #pointer to head node
        
        while current != None:                                                          # If current is equal to None, current is the Tail.
            if current is self.head:                                                    # If the node is the head this string will be added to the nodes list
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:                                             # If the node is the Tail this string will be added to the nodes list
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)                                     # makes a regular node, the pointer will be added later
            
            current = current.next_node
        return '->'.join(nodes)                                                         # joins all strings in the nodes list together and adds a pointer to the next node in the list
