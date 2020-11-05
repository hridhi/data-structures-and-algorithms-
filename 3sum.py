class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        m=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: continue
            l=i+1
            r=n-1
            while (l<r):
                s=nums[i]+nums[l]+nums[r];
                if s==0:
                    ir=[]
                    ir.append(nums[i]) 
                    ir.append(nums[l])
                    ir.append(nums[r])
                    m.append(ir)
                    l=l+1;
                    r=r-1;
                    while(l<r and nums[l-1]==nums[l]):l=l+1;
                    while (l<r and nums[r+1]==nums[r]): r=r-1;
                elif(s<0):
                    l=l+1;
                else:
                    r=r-1;
                    
        return m;
