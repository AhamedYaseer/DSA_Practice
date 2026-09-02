# Stacks

This folder contains DSA problems solved using the Stack data structure.

## Common Patterns Used (till date)

- Stack Simulation
- LIFO (Last In, First Out)
- Matching Parentheses
- Reverse Polish Notation
- Monotonic Stack
- Next Greater Element
- Minimum Tracking
- Index Tracking

## Problems Covered

| Problem | Main Technique |
|---|---|
| Baseball Game | Stack Simulation |
| Valid Parentheses | Stack / Matching Parentheses |
| Evaluate Reverse Polish Notation | Stack / Reverse Polish Notation |
| Daily Temperatures | Monotonic Stack / Next Greater Element |
| Min Stack | Two Stacks / Minimum Tracking |

## Complexity Goal

Stacks are commonly used when the most recently added element needs
to be accessed first, following the LIFO principle.

Typical target:
- Time: O(n) for single-pass stack problems
- Space: O(n) in the worst case

For problems such as Daily Temperatures, a monotonic stack can reduce
a brute-force O(n²) approach to O(n) because each index is pushed and
popped at most once.
