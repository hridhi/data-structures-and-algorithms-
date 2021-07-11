#You are given n activities with their start and finish times. Select the maximum number of activities 
#that can be performed by a single person, assuming that a person can only work on a single activity at a time. 

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        req=[]
        for i in range(n):
            req.append([start[i],end[i]])
        sorter=lambda x: x[1]
        sorted(req,key=sorter)
        selected=[]
        j=0
        cnt=0
        selected.append(req[0])
        for i in range(1,n):
            if req[i][0]>=req[j][1]:
                selected.append(req[i])
                j=i
                cnt+=1
        return cnt 
            
