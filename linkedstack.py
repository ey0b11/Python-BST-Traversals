"""
Module: linkedstack.py
Author: Kenneth Lambert (textbook)
"""

from node import Node
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    """A link-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        
        def visitNodes(node):
            """Adds items to tempList from tail to head."""
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
                
        tempList = list()                
        visitNodes(self.items)
        return iter(tempList)

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self.items.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None

    def push(self, item):
        """Adds item to the top of the stack."""
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        data = self.items.data
        self.items = self.items.next
        self.size -= 1
        return data
        
        
