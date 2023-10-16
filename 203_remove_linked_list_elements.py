# Definition for singly-linked list.
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

    def removeElements(self, head, val):
        # Approach 1:

        cur = head
        
        if head.val == val and head.next != None:
            head = head.next

        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        self.printElements(head)
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
print(foo.removeElements(n1,6));
