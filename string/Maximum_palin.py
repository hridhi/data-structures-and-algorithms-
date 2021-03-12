def longestPalSubstr(string):
    maxLength = 1
    start = 0
    length = len(string)
    low = 0
    high = 0
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
    return string[start:start + maxLength]


def rotate(input,d): 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
    return Lsecond + Lfirst 


for _ in range(int(input())):
    print("string input ")
    s=input()#"madamimadam"
    print("give q")
    for _ in range(int(input())):
        l,r=map(int,input().split())
        ans=[]
        e=s[l-1:r]
        for i in range(len(e)):
            e=rotate(e,1)
            a=longestPalSubstr(e)
            if a in ans:
                pass
            else:
                ans.append(a)
        print(len(ans))
