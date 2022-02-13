class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        c0, c1 = collections.Counter(), collections.Counter()
        
        n=len(nums)
        if n==1:
            return 0
        for i in range(0,n,2):
            c0[nums[i]]+=1
            if i==n-1: break
            c1[nums[i+1]]+=1
        
        c0_most1, c0_most1f = c0.most_common(1)[0][0], c0.most_common(1)[0][1]
        c1_most1, c1_most1f = c1.most_common(1)[0][0], c1.most_common(1)[0][1]
        c0_most2 = c0.most_common(2)
        c1_most2 = c1.most_common(2)
        
        c1_total = floor(n/2)
        c0_total = n -c1_total
        
        if c0_most1!=c1_most1:
            return n-c0_most1f-c1_most1f
        
        
        if c0_most1==c1_most1:
            
            # if both of them have only 1 element
            if len(c0_most2)==1 and len(c1_most2)==1:
                return c1_total
            
            # if one of them has only 1 element
            if len(c0_most2)==1:
                return min(c1_total-c1_most2[1][1], n-c0_most2[0][1])
            if len(c1_most2)==1:
                return min(c0_total-c0_most2[1][1], n-c1_most2[0][1])
            
            # if both have at least 2 elements
            return min(n-c0_most1f-c1_most2[1][1], n-c1_most1f-c0_most2[1][1])
