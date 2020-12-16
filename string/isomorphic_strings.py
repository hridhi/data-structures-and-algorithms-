#Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
#Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible 
#for every character of str1 to every character of str2 while preserving the order.
#Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’


#my approach 
def areIsomorphic(str1,str2):
    if len(str1)!=len(str2):
        return 0
    dictOfElems = dict() 
    for elem in str1:
        if elem in dictOfElems:
            dictOfElems[elem] += 1 
        else:
            dictOfElems[elem] = 1
    dictOfElems2 = dict()
    for elem in str2:
        if elem in dictOfElems2:
            dictOfElems2[elem] += 1 
        else:
            dictOfElems2[elem] = 1
    for x,y in dictOfElems2.items():
        print(x,y)
    for x,y in dictOfElems.items():
        print(x,y)
    a=list(dictOfElems.values())
    b=list(dictOfElems2.values())
    n= len(dictOfElems)
    for i in range(n):
        if a[i]!=b[i]:
            return 0
    return 1
str1="rfkqyuqf"
str2="jkxyqvnr"
print(areIsomorphic(str1,str2))

#gfg solution 
#An Efficient Solution can solve this problem in O(n) time. The idea is to create an array to store mappings of processed characters.

#1) If lengths of str1 and str2 are not same, return false.
#2) Do following for every character in str1 and str2
 #  a) If this character is seen first time in str1, 
  #    then current of str2 must have not appeared before.
   #   (i) If current character of str2 is seen, return false.
    #      Mark current character of str2 as visited.
     # (ii) Store mapping of current characters.
   #b) Else check if previous occurrence of str1[i] mapped
    #  to same character.

