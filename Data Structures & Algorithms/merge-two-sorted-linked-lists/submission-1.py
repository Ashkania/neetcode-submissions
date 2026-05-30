# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while list1:
            l.append(list1.val)
            list1 = list1.next
        
        while list2:
            l.append(list2.val)
            list2 = list2.next
        
        if l:
            l = sorted(l)
            head = cur = ListNode(l[0])
        else:
            return None

        for n in l[1:]:
            cur.next = ListNode(n)
            cur = cur.next

        return head

