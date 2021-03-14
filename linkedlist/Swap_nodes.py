# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fromstart=head
        for i in range(k-1):
            fromstart=fromstart.next
        temp=fromstart
        fromend=head
        while(temp.next):
            temp=temp.next
            fromend=fromend.next
        fromend.val,fromstart.val=fromstart.val,fromend.val
        return head
