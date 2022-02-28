class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # when length is zero
        if not nums: return []
        
        # when length is one
        n = len(nums)            
        start = nums[0]
        if n==1: return [str(start)]
        
        # general case
        output = []
        i = 1
        while i<n:
            end = nums[i]
            if end == nums[i-1] + 1: 
                if i==n-1: output.append(str(start)+'->'+str(end))
            else:
                if start == nums[i-1]: output.append(str(start)) 
                else: output.append(str(start)+'->'+str(nums[i-1]))
                start = nums[i]
                if i==n-1: output.append(str(start))
            i+=1       
        return output 
