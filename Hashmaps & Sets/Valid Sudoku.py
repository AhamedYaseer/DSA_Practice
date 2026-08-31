Problem:
Valid Sudoku (https://leetcode.com/problems/valid-sudoku/description/)

Approach:
Frequency Counting for Rows, Columns, and 3×3 Subsections

Why this works:
A valid Sudoku board must satisfy three conditions:
- Each row contains no duplicate digits.
- Each column contains no duplicate digits.
- Each 3×3 subsection contains no duplicate digits.

We use a frequency dictionary containing digits 0–9 and create a
copy for each row, column, and 3×3 subsection.

For each section, we count the occurrences of every digit. If any
digit occurs more than once, the board is invalid.

The '.' cells are ignored because they are not present in the
frequency dictionary.

If all 3 check is done and no condition failed, we return true

Time Complexity:
O(n²)
For a fixed 9×9 Sudoku board, we examine every cell a constant
number of times while checking rows, columns, and 3×3 subsections.

Space Complexity:
O(n)
We use a frequency dictionary for each row, column, and subsection.
For the fixed 9×9 board, this is effectively O(1).

# ----------------------------------
# Frequency Counting for Rows, Columns, and 3×3 Subsections
# ----------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        number = {
            '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
            '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
        }

        # Each row
        for i in board:
            mod_num = number.copy()   #shallow copying to avoid affecting original

            for j in i:
                if j in mod_num:
                    mod_num[j] += 1

            for i in mod_num:        #once 9 elements are traversed, we'll check the occurence of number
                if mod_num[i] > 1:
                    return False

        # Each column
        for i in range(len(board[0])):
            mod_num = number.copy()

            for j in range(0, 9):
                if board[j][i] in mod_num:
                    mod_num[board[j][i]] += 1

            for i in mod_num:
                if mod_num[i] > 1:
                    return False

        # Each 3×3 subsection
        rs = 0
        re = 2
        cs = 0
        ce = 2

        while ce < 9 and re < 9:
            mod_num = number.copy()

            for i in range(rs, re + 1):
                for j in range(cs, ce + 1):
                    if board[i][j] in mod_num:
                        mod_num[board[i][j]] += 1

            for i in mod_num:      #here, out of first for loop, as in the above -> all 9 element gets traversed only after both loop ends
                if mod_num[i] > 1:
                    return False

            cs, ce = cs + 3, ce + 3

            if ce > 9:
                cs = 0
                ce = 2
                rs, re = rs + 3, re + 3

        return True


Approach:
Hash Sets / Duplicate Detection

Why this works:
A valid Sudoku board must satisfy three conditions:
- No duplicate digits in any row.
- No duplicate digits in any column.
- No duplicate digits in any 3×3 subsection.

We maintain three collections of sets:
- row[r] stores the numbers already encountered in row r.
- col[c] stores the numbers already encountered in column c.
- sec[sect] stores the numbers already encountered in each 3×3 subsection.

For every non-empty cell, we check whether the number already exists
in its corresponding row, column, or subsection.

If it exists in any of them, the board is invalid and we immediately
return False.

Otherwise, we add the number to all three sets.

The subsection index is calculated using:

    sect = (r // 3) * 3 + (c // 3)

This maps each cell to one of the nine 3×3 subsections.

Time Complexity:
O(n²)
We visit every cell once. Set membership, insertion, and lookup take
O(1) on average.

Space Complexity:
O(n²)
We maintain sets for all rows, columns, and 3×3 subsections.

For the fixed 9×9 Sudoku board, this is effectively O(1).

# ----------------------------------
# Hash Sets / Duplicate Detection
# ----------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sec = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                sect = (r // 3) * 3 + (c // 3)

                if num in row[r] or num in col[c] or num in sec[sect]:
                    return False

                row[r].add(num)
                col[c].add(num)
                sec[sect].add(num)

        return True
