class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # if n is smaller than 3, no need to pop
        n = len(nums)
        if n<=2: return len(nums)
        
        # add a number at the end to mark the end of the array
        cur = nums[0]
        end = nums[0] - 1
        nums.append(end)
        
        i = 1
        count = 0
        while nums[i]!=end:
            if count == 0:
                if nums[i] == cur: count = 1
                else: cur = nums[i]
                i+=1
            else: # count = 1
                if nums[i]==cur:
                    nums.pop(i)
                else:
                    cur = nums[i]
                    count = 0
                    i+=1
                   
        nums.pop()
        return len(nums)
        
