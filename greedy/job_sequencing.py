#Given a set of N jobs where each job i has a deadline and profit associated to it. 
#Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
#We earn the profit if and only if the job is completed by its deadline. 
#The task is to find the maximum profit and the number of jobs done.

def JobScheduling(Jobs,n):
    #sorting by profit 
    result=0
    cnt=0
    sorter= lambda x : x[2]
    Jobs= sorted(Jobs,key=sorter)
    Jobs=Jobs[::-1]
    #print(Jobs)
    y=set()
    for i in Jobs: 
        #print(i[1],y)
        if i[1] not in y :
            #print(i)
            y.add(i[1])
            cnt+=1 # to keep track of how many jobs can be done 
            result+=i[2] # tracking maximum profit 
    return cnt,result 
n=4
Jobs=[[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
print(JobScheduling(Jobs,n))
