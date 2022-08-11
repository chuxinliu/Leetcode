class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []
        
        for i in nums:
            
            # if larger than last number of sub, extend 
            if not sub: sub.append(i)
            elif sub[-1]<i: sub.append(i)
            
            # if smaller: swap the number that's larger than it
            elif sub[-1]>i:
                
                # binary search
                p1, p2 = 0, len(sub)-1
                while p1<p2:
                    mid = floor(0.5*(p1+p2))
                    if sub[mid]>=i: p2=mid # potential swapping index 
                    else: p1 = mid+1 # not swapping index, add 1
                sub[p1] = i                        
            
        return len(sub)
