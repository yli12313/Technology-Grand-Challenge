# LINK: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        # Constraints
        # - The number of nodes in the list is in the range [0, 5000]
        # - -5000 <= Node.val <= 5000

        # Topic: Linked List and Recursion.

        # Approach 1 (Iterative Approach):
        # - The iterative approach is not hard. You have to set a temp
        # variable to 'cur.next'; then you can begin updating pointers such 
        # that you update: 

        #    1) cur.next -> prev
        #    2) prev -> cur
        #    3) cur -> temp

        # TC: O(N)
        # SC: O(1)

        """
        cur = head
        prev = None

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
        """

        # Approach 2 (Recursive Approach):
        # - Not exactly sure what's going on, but this is how you do it recursively.
        # - UPDATE: I was able to understand it! Don't quit and keep trying!

        # NOTE: The best way to think about a recursive problem is to break it down into 
        # a sub-problem.

        # TC: O(N)
        # SC: O(N)

        # Base case: If the 'head' or 'head.next' is None, then return the 'head'. Can't 
        # reverse the linked list in these two cases!
        if head == None or head.next == None:
            return head
        
        # Let the 'newHead' recurse to the very end of the linked list. 'newHead' will point to
        # the last node and serve as the head of the reversed linked list. We will return this
        # as the answer!
        newHead = self.reverseList(head.next)

        # After 'newHead' points to the last node in the linked list, the recursion jumps
        # back a level and now you are at the SECOND TO LAST NODE. You set:

        # 1) head.next.next -> head
        # 2) head.next -> None

        # This is just genius!

        head.next.next = head
        head.next = None

        # Return 'newHead' as the answer.
        return newHead
