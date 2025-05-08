# 🌲 Python Binary Search Tree Traversals

This project implements a **Linked Binary Search Tree (BST)** in Python with full traversal methods, node operations, and structural checks. Originally developed for a Data Structures course at Wake Tech, it has been refined for public demonstration and professional use.

---

## ✅ Features

- 📥 **Insertion**: Add elements using `add(item)`
- ❌ **Removal**: Delete nodes with `remove(item)`
- 🔁 **Replacement**: Update a node’s value with `replace(old, new)`
- 🔎 **Search Helpers**:
  - `successor(item)` — next higher value
  - `predecessor(item)` — next lower value
- 🔢 **Tree Traversals**:
  - `inorder()`
  - `preorder()`
  - `postorder()`
  - `levelorder()` *(extra credit)*
- 📐 **Structural Analysis**:
  - `height()` — tree depth
  - `is_balanced()` — checks balance based on log₂(n)
- 📊 **Display**:
  - Rotated tree view
  - Symbolic vertical branch layout

---

##  File Overview

| File Name             | Description                                 |
|----------------------|---------------------------------------------|
| `bst_main.py`         | Primary script to run and test the BST demo |
| `bstnode.py`          | Node structure for BST                      |
| `node.py`             | Basic node structure for other ADTs         |
| `linkedstack.py`      | Stack structure used internally             |
| `linkedqueue.py`      | Queue structure for level-order traversal   |
| `abstract*.py` files  | Abstract base classes for collections       |

---

## How to Run

From terminal:

```bash
python bst_main.py
