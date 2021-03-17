class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def push(self,value):
        temp=Node(value)
        temp2=self.head
        temp.next=self.head
        if self.head is not None:
            while(temp2.next!=self.head):#circular linked list 
                temp2=temp2.next
            temp2.next=temp
        else:
            temp.next=temp
        self.head=temp
    def printList(self):
        temp=self.head
        if self.head is not None:
            while (True):
                print(temp.data)
                temp=temp.next
                if(temp==self.head):
                    break
    def splitList(self,head1,head2):
        slow_ptr=fast_ptr=self.head
        if self.head is None:
            return 
        while(fast_ptr.next!=self.head and fast_ptr.next.next!=self.head):
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next
            
        if fast_ptr.next.next==self.head:
            fast_ptr=fast_ptr.next
        head1.head=self.head
        if self.head.next!=self.head:
            head2.next=slow_ptr.next
            
        fast_ptr.next=slow_ptr.next#makeing 2 crcular halfs 
        slow_ptr.next=self.head
        
        
head = CircularLinkedList()  
head1 = CircularLinkedList() 
head2 = CircularLinkedList() 
  
head.push(12) 
head.push(56) 
head.push(2) 
head.push(11) 
head.printList() 
  
# Split the list  
head.splitList(head1 , head2) 
  

head1.printList() 
  

head2.printList() 
