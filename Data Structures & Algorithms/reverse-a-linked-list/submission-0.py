# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
 
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        l = l[::-1]

        if l:
            head_new = cur = ListNode(l[0])
            for n in l[1:]:
                cur.next = ListNode(n)
                cur = cur.next

            return head_new
        else:
            return None