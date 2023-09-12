# LINK: https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        # Constraints:
        # - The number of nodes in the linked list is in the range [0,10^4].
        # - -10^6 <= Node.val <= 10^6

        # Topic: LinkedList

        # Approach 1:
        # - If head is None, return None.
        # - Define odd (o), even (e), evenHead (eHead).
        # - Loop while e and eHead are not None.
        # - Update o.next, o, e.next, e.
        # - Update o.next.
        # - return head.

        # TC: O(N)
        # SC: O(1)

        if head == None:
            # TRICK: Return None here, and not False.
            return None

        o = head
        e = head.next
        eHead = e

        while e != None and e.next != None:
            # TRICK: The order is: o.next, o, e.next, e.
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next

        o.next = eHead
        return head
