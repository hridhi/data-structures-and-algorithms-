# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:return None
        a=headA
        b=headB
        while a!=b:
            a=headB if a==None else a.next
            b=headA if b==None else b.next
        return b
            
#time limit exceeding code 
# brute force approach 
        
def intersetPoint(head1,head2):
    #code here
    count=0
    count1=0
    req=0
    while head1.next!=None:
        count+=1
    while head2.next!=None:
        count1+=1
    if count>count1:
        req=1
    else:
        req=2
    if req==1:
        for i in range(abs(count=count1)):
            head1=head1.next
    else:
        for i in range(abs(count=count1)):
            head2=head2.next
    for i in range(min(count,count1)):
        if head1.data==head2.data:
            return head1.data
        head1=head1.next
        head2=head2.next
        
