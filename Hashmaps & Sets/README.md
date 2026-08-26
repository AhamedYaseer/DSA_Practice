# Hashmaps & Sets

This folder contains DSA problems that use hash maps and hash sets
for efficient membership checking, frequency counting, and duplicate
detection.

## Common Patterns Used (till date)

- Hash Map / Frequency Counting
- Hash Set / Membership Checking
- Hash Set / Duplicate Detection
- Character Frequency Counting
- Fixed-Size Frequency Signature
- Hashable Tuple as Dictionary Key
- Early Return
- Matrix Traversal


## Problems Covered

| Problem | Approach / Pattern |
|------------------------------|------------------------------------|
| Jewels and Stones            | Hash Set, Membership Checking      |
| Contains Duplicate           | Hash Map, Membership Tracking      |
| Contains Duplicate           | Hash Map                           |
| Ransom Note.                 | Hash Map / Frequency Counting      |
| Valid Anagram                | Hash Map / Frequency Counting      |
| Maximum Number of Balloons   | Hash Map / Frequency Counting      |
| Valid Sudoku                 | Hash Set / Duplicate Detection     |
| Group Anagrams               | Hash Map / Frequency Signature     |
| Majority Element             | Hash Map / Frequency Counting      |
| Longest Consecutive Sequence | Hash Set / Sequence Start Detection|


## Key Concepts Learned

- Hash maps store key-value pairs and provide average O(1) lookup,
  insertion, and deletion.
- Hash sets store unique values and provide average O(1) membership
  checking.
- Use a hash map when additional information such as frequency is
  required.
- Use a hash set when only existence/membership needs to be tracked.

## Complexity

Hash Map:
- Average lookup: O(1)
- Average insertion: O(1)
- Space: O(n) in the worst case

Hash Set:
- Average membership check: O(1)
- Average insertion: O(1)
- Space: O(n) in the worst case
