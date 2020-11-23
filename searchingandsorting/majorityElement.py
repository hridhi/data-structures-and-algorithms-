#Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.


def majorityElement(A,N):
    #Your code here
    dictOfElems = dict()
    for elem in A:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
    for x,y in dictOfElems.items():
        if y> N/2:
            return x 
    return -1
