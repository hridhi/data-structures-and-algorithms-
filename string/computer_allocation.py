#Write a function “runCustomerSimulation” that takes following two inputs
#a) An integer ‘n’: total number of computers in a cafe and a string:
#b) A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs. 
#The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer.
def comp(str1,n):
    visited=[]
    count=0
    for i in range(len(str1)):
        if str1[i] not in visited and n!=0:
            visited.append(str1[i])
            n=n-1
        elif str1[i] in visited:
            visited.remove(str1[i])
            n=n+1
        elif str1[i] not in visited and n==0:
            count+=1
    return int(count/2)
str1="GACCBDDBAGEE"
print(comp(str1,3))
