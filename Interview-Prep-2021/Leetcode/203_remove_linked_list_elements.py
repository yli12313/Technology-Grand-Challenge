# LINK: https://leetcode.com/problems/remove-linked-list-elements/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def printElements(self, head):
        cur = head

        while cur != None:
            print(cur.val, end="->")
            cur = cur.next
        
        print()

    def removeElements(self, head, val):
        # Constraints: 
        # - The number of nodes in the list is in the range [0,10^4].
        # - 1 <= Node.val <= 50
        # - 0 <= val <= 50

        # Topic: Linked List
        # This is a Linked List or Recursion problem.

        # Approach 1:
        # - Remove all the nodes at the front of the linked list that's equal to val.
        # - Set a pointer cur to point at head.
        # - Do a while loop when cur is not None and cur.next is not None.
        # - If the next node has val, set cur.next to cur.next.next.
        # - Else increment cur.

        # Approach 1 (YouTube):
        # - Treat the case where the node at the head of the list has Node.val == val. 
        #   - Keep in mind that multiple nodes can start at the beginning of the linked 
        # list where the condition is true.
        # - Define a while loop that will loop through the linked list.
        # - Define condition that will check if the next node has Node.val == val.
        #   - If the condition is true, then delete the next node.
        #   - Else increase the cursor.

        # TC: O(N)
        # SC: O(1)

        # TRICK: Make sure to use '==' when doing a check for equality!
        while head != None and head.val == val:
            head = head.next

        cur = head

        while cur != None and cur.next != None:
            # TRICK: Make sure to use '==' when doing a check for equality!
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                # TRICK: To increment the pointer, you have to do 'cur = cur.next'.
                cur = cur.next
        
        # self.printElements(head)
        return head    

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = None

foo = Solution();
foo.removeElements(n1,6)
