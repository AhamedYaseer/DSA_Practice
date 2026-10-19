Problem:
Remove Duplicates from Sorted List (https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Approach:
Linked List Traversal (In-Place Modification)

Why this works:
Since the linked list is sorted, duplicate values will always be next to each other.

We use the `current` pointer to traverse the list.
If `current.val` is equal to `current.next.val`, we skip the duplicate node by updating `current.next`.
Otherwise, we move `current` to the next node.

Time Complexity:
O(n)
The list is traversed once.

Space Complexity:
O(1)
Only one pointer is used.

# ----------------------------------
# In-place linked list solution
# ----------------------------------

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current=head

        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next

        return head
