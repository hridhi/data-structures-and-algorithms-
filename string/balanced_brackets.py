#Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

#exp="[()]{}{[()()]()}"
exp="[(])"
open=["(","[","{"]
close=[")","]","}"]
stack=[]
balanced=True
for i in exp:
    if i in open:
        stack.append(i)
    else:
        temp=-1
        for h in range(3):
            if close[h]==i:
                temp=h
        if len(stack)>0:
            j=stack[-1]
            if j !=open[temp]:
                balanced=False
                break
            stack=stack[:-1]
print(balanced)
            
            
