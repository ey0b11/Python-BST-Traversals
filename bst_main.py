"""
Module:  bst_main.py

Author:  Eyob Ollivierre
Date:  4/20/25
Based on code in textbook by Ken Lambert, with modifications and additional methods added by Student Author

Description:
A linked implementation of binary search tree.

Students write methods:
preorder
postorder
height
is_balanced
successor
predecessor

For extra credit, students can write method:
levelorder

All other methods are provided, including inorder.
"""

import math
from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue



class LinkedBST(AbstractCollection):
    """A link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """
        Initializes an empty binary search tree.
        If a source collection is provided, its elements are added to the tree.

        Args:
            sourceCollection (iterable, optional): An optional collection of initial elements.
        """
        self.root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __len__(self):
        """Returns the number of nodes of the tree."""
        return self.size

    def __str__(self):
        """Returns a string representation of the tree rotated 90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.left, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.right, level + 1)
            return s

        return recurse(self.root, 0)

    def alt_str(self):
        """Returns a string representation of the tree using branching characters."""
        def recurse(node, prefix="", is_left=True, is_root=False):
            if node is None:
                return ""

            result = prefix
            if not is_root:
                result += "└── " if is_left else "┌── "
            result += str(node.data) + "\n"

            if node.left or node.right:
                if node.right:
                    result += recurse(
                        node.right,
                        prefix + ("    " if is_left or is_root else "│  "),
                        is_left=False
                    )
                if node.left:
                    result += recurse(
                        node.left,
                        prefix + ("    " if is_left or is_root else "│  "),
                        is_left=True
                    )
            return result

        return recurse(self.root, "", True, is_root=True)

    def __iter__(self):
        """Supports iteration over the tree using preorder traversal (Root, Left, Right)."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self.root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def preorder(self):
        """Returns an iterator for preorder traversal (Root, Left, Right)."""
        lyst = []

        def recurse(node):
            if node is not None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return iter(lyst)

    def inorder(self):
        """Returns an iterator for inorder traversal (Left, Root, Right)."""
        lyst = []

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self.root)
        return iter(lyst)

    def postorder(self):
        """Returns an iterator for postorder traversal (Left, Right, Root)."""
        lyst = []

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)

        recurse(self.root)
        return iter(lyst)

    def levelorder(self):
        """Returns an iterator for level-order traversal (breadth-first traversal)."""
        lyst = []
        if self.isEmpty():
            return iter(lyst)

        queue = LinkedQueue()
        queue.add(self.root)

        while not queue.isEmpty():
            node = queue.pop()
            lyst.append(node.data)
            if node.left is not None:
                queue.add(node.left)
            if node.right is not None:
                queue.add(node.right)

        return iter(lyst)

    def __contains__(self, item):
        """Determines whether the tree contains a given item."""
        return self.find(item) is not None

    def find(self, item):
        """Searches for an item in the tree and returns the stored value if found."""
        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            elif node.data > item:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self.root)

    # Mutator methods
    def clear(self):
        """Removes all elements from the tree, resetting it to an empty state."""
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds a new item to the tree, maintaining the binary search tree property."""
        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(item)
                else:
                    recurse(node.right)

        if self.isEmpty():
            self.root = BSTNode(item)
        else:
            recurse(self.root)

        self.size += 1

    def remove(self, item):
        """Removes the specified item from the tree."""
        if not item in self:
            raise KeyError("Item not in tree.")

        def liftMaxInLeftSubtreeToTop(top):
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        if self.isEmpty():
            return None

        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self.root
        parent = preRoot
        direction = 'L'
        currentNode = self.root

        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right

        if itemRemoved == None:
            return None

        if not currentNode.left == None and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            if currentNode.left == None:
                newChild = currentNode.right
            else:
                newChild = currentNode.left
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild

        self.size -= 1
        if self.isEmpty():
            self.root = None
        else:
            self.root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """Replaces the data of a node in the tree that matches the given item."""
        probe = self.root
        while probe is not None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Computes the height of the binary search tree."""
        def recurse(node):
            if node is None:
                return -1
            else:
                return 1 + max(recurse(node.left), recurse(node.right))

        return recurse(self.root)

    def is_balanced(self):
        """Checks whether the binary search tree is globally balanced."""
        if self.isEmpty():
            return True
        return self.height() <= math.floor(math.log2(self.size)) + 1

    def successor(self, item):
        """Finds and returns the successor of a given item in the binary search tree."""
        node = self.root
        succ = None
        while node is not None:
            if item < node.data:
                succ = node.data
                node = node.left
            else:
                node = node.right
        return succ

    def predecessor(self, item):
        """Finds and returns the predecessor of a given item in the binary search tree."""
        node = self.root
        pred = None
        while node is not None:
            if item > node.data:
                pred = node.data
                node = node.right
            else:
                node = node.left
        return pred

def main(is_extra_credit=False):
    """Demonstrates full functionality of the LinkedBST class."""
    print("Creating a binary search tree...")

    tree = LinkedBST()

    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        tree.add(val)

    print("\nTree printed sideways:\n")
    print(tree)

    print("\nAlternate Representation of the tree: \n")
    print(tree.alt_str())

    print(f"Inorder traversal: {list(tree.inorder())}")
    print(f"Preorder traversal: {list(tree.preorder())}")
    print(f"Postorder traversal: {list(tree.postorder())}")

    if is_extra_credit:
        print()
        print(f"(Extra Credit) Level-order traversal: {list(tree.levelorder())}")

    print(f"\nFind 60 in tree? {'Yes' if 60 in tree else 'No'}")
    print(f"Find 99 in tree? {'Yes' if 99 in tree else 'No'}")

    replaced = tree.replace(30, 35)
    print(f"Replacing 30 with 35: {'Replaced' if replaced else 'Not found'}")
    print(f"Inorder after replacement: {list(tree.inorder())}")

    height = tree.height()
    balanced = tree.is_balanced()
    print(f"\nTree height: {height}")
    print(f"\nTree size: {len(tree)}")
    print(f"Is the tree globally balanced (based on log₂(n))? {'Yes' if balanced else 'No'}")

    print(f"\nSuccessor of 40: {tree.successor(40)}")
    print(f"Predecessor of 60: {tree.predecessor(60)}")
    print(f"Successor of 80: {tree.successor(80)}")
    print(f"Predecessor of 20: {tree.predecessor(20)}")

    print("\nAdding unbalanced values to skew the tree...")
    for val in [90, 100, 110]:
        tree.add(val)

    print("Tree after skewed additions rotated sideways:\n")
    print(tree)

    print("\nTree after skewed additions in alternate representation: \n")
    print(tree.alt_str())

    height = tree.height()
    balanced = tree.is_balanced()
    print(f"\nTree height: {height}")
    print(f"\nTree size: {len(tree)}")
    print(f"Is the tree globally balanced (based on log₂(n))? {'Yes' if balanced else 'No'}")

    if is_extra_credit:
        print()
        print(f"(Extra Credit) Level-order traversal: {list(tree.levelorder())}")

if __name__ == "__main__":
    main(is_extra_credit=True)
