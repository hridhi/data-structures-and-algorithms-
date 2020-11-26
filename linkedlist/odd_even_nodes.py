# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head== None: return None
        odd=ListNode(0)
        odd=head
        even=ListNode(0)
        even=head.next
        evenhead=ListNode(0)
        evenhead=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenhead
        return head
            
        
