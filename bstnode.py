"""
Module: bstnode.py
Author: Kenneth Lambert (textbook)
"""

class BSTNode(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
