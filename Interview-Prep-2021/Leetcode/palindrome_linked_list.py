# LINK: https://leetcode.com/problems/palindrome-linked-list/

## FYI: sorting is very important with anagrams and palindromes! ##
## FYI: Make sure to record the link to the problem before starting leetcode! ##

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        p1=head
        stack=[]
        
        while p1!=None:
            stack.append(p1.val)
            p1=p1.next
        
        return stack==stack[::-1]

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4

p1 = ListNode(1)
p2 = ListNode(0)
p3 = ListNode(3)

p1.next = p2
p2.next = p3

foo = Solution();
print(foo.isPalindrome(n1));
print(foo.isPalindrome(p1));