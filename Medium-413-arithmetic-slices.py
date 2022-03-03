class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        output = 0
        n = len(nums)
        
        if n>=3:
            # calculate first differences
            first_diff = []
            for i in range(n-1):
                first_diff.append(nums[i+1]-nums[i])
            
            # count number of same first differences
            d0 = first_diff[0]
            ct = []
            cd = 1
            for i in range(1, n-1):
                if first_diff[i]==d0:
                    cd += 1
                    if i==n-2: ct.append(cd)
                else: 
                    ct.append(cd)
                    d0 = first_diff[i]
                    cd = 1
            
            # use the number of same first differences to get output
            for j in ct:
                output += j*(j-1)/2
            
        return int(output)
