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

        # Topic: Linked List

        # Approach 1:
        # - Check that if head is None, then return None.
        # - Define odd, even, and evenHead pointers.
        # - Do a while() loop that continues to run as long as even and even.next IS NOT None.
        # - Update the pointers in the following order: odd.next, odd, even.next, even.
        # - Assign odd.next to evenHead.
        # - Return head.

        # TC: O(N)
        # SC: O(1)

        # TRICK: Have to put the 'head == None' check at the beginning!
        if head == None:
            # TRICK: Return None here, and not False.
            return None

        o = head
        e = head.next
        eHead = e

        while e != None and e.next != None:
            # TRICK: The order is: 1) o.next, 2) o, 3) e.next, 4) e.
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next

        o.next = eHead
        return head
