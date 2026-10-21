# Linked List

This folder contains linked-list DSA problems solved in Python.

The goal is to understand how nodes and pointers work, modify links safely, and compare solutions by their time and space complexity.

## Common Patterns Used (till date)

* Linked List Traversal
* Pointer Tracking
* In-Place Node Modification
* Skipping Duplicate Nodes

## Problems Covered

| Problem | Approach / Pattern |
| --- | --- |
| [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Linked List Traversal, In-Place Modification |

## Problem-Solving Flow

For each problem, I aim to follow this progression:

1. Understand the problem and linked-list structure.
2. Develop a straightforward solution.
3. Analyze time and space complexity.
4. Look for ways to reduce extra space or unnecessary traversal.
5. Implement the improved solution while preserving earlier approaches when relevant.
6. Record the final complexity and the reason the solution works.

## Key Ideas Practiced

* Use a pointer to traverse the list without losing access to the head.
* Check that a node and its `next` node exist before accessing their values.
* Update `current.next` to skip a node when it is safe to do so.
* In a sorted list, equal values appear next to each other, so duplicates can be removed in one pass.
* When removing a duplicate, keep the current pointer in place so it can check the new next node too.

## Complexity Notes

For **Remove Duplicates from Sorted List**:

* **Time:** `O(n)` — each node is processed at most once.
* **Extra Space:** `O(1)` — the existing links are modified without building another list.
