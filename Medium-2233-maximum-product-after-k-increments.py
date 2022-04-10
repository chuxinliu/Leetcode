class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        snums = sorted(nums)
        stotal = []
        total = 0
        for i in snums:
            total+=i
            stotal.append(total)
        n = len(nums)
        
        # find the breaking point
        i, j = 0, n-1
        while i<j:
            mid = ceil(0.5*(i+j))
            if snums[mid]*(mid+1)-stotal[mid]<=k: i = mid
            else: j=mid-1
            
        level = snums[j]
        remain = k - (snums[j]*(j+1)-stotal[j])
        
        if j==n-1:
            add, res = remain // n, remain % n
            if res>0: output = ((level+add)**(n-res)) * ((level+add+1)**res)
            else: output = (level+add)**(n-res)
         
        else:
            if remain<=j+1: output = level**(j+1-remain) * ((level+1)**remain)
            else:
                add, res = remain // (j+1), remain % (j+1)
                output = ((add+level)**(j+1-res)) * ((level+add+1)**res)

            for i in snums[j+1:]:
                output *= i
        
        return output % (10**9+7)
