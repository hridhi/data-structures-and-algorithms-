def maxProduct(self,arr, n):
        # code here
        over_all_max=1
        maxi=mini=1
        for i in range(n):
            if arr[i]==0:
                maxi=mini=1
            if arr[i]>0:
                maxi,mini=maxi*arr[i],min(arr[i]*mini,1)
                if over_all_max<maxi:
                    over_all_max=maxi
            if arr[i]<0:
                maxi,mini=max(mini*arr[i],1),maxi*arr[i]
                if over_all_max<maxi:
                    over_all_max=maxi
        return over_all_max
