"""
Modujle: node.py
Author: Kenneth Lambert (textbook)
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
