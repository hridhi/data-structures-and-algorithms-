#Given pointer to the head node of a linked list, the task is to reverse the linked list.
#We need to reverse the list by changing the links between nodes.
#one way to solve this by using stack but it will take extra space complexity 
#another way to solve is to keep 3 pointers , prev , curr and next which will take O(n) time complexity 
#another way is through reccursion 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
    def reverse_recursive(self, head):
      if head is None or head.next is None: 
          return head 
      rest = self.reverse_recursive(head.next) 

      head.next.next = head 
      head.next = None
      return rest 

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85)
llist.printList() 
llist.reverse() 
print ("\nReversed Linked List")
llist.printList() 
llist.head = llist.reverse_recursive(llist.head) 
print ("\nReversed Linked List")
llist.printList() 
