# Write a removeDuplicates() function that takes a list and deletes any duplicate nodes from the list. The list is not sorted. 
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if head is None or head.next is None:
            return head
        arr=[]
        temp=head
        arr.append(temp.data)
        while(temp.next):
            if temp.next.data not in arr:
                arr.append(temp.next.data)
                temp=temp.next
            else:
                temp.next=temp.next.next
        return head 
                    
               
