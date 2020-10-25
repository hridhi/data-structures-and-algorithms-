#In this challenge, you will be given a string. You must split it into two contiguous substrings,
#then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

#For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. 
#Note that all letters have been used, the substrings are contiguous and their lengths are equal. 
#Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

def anagram(s):
    if len(s)%2: return -1
    l = len(s)//2
    a = Counter(s[:l]) #splittign the array 
    b = Counter(s[l:])
    return l-sum((a & b).values())  # the total numbers minus similar elements in both a and b
    
