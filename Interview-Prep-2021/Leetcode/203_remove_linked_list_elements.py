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
        while head is not None and head.val == val:
            head = head.next

        cur = head

        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
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
