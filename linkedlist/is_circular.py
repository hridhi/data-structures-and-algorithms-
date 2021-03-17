def isCircular(head):
    # Code here
    if head is None:
        return 1
    temp=head
    while (temp.next!=None and temp.next!=head):
        temp=temp.next
    if (temp.next==None):
        return 0
    else:
        return 1
