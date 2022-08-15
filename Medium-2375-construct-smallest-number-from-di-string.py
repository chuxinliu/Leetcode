class Solution:
    '''
    Backtracking
    '''
    
    def smallestNumber(self, pattern: str) -> str:
        
        n = len(pattern)
        if n==1:
            if pattern == "I": return "12"
            else: return "21"
            
        nums = [1]
        pn = 0 # pointer at nums list
        pp = 0 # pointer at pattern
        
        while pp < n:
            
            if pattern[pp] == "I": new = nums[pn]+1
            else: new = nums[pn]-1
            nums.append(new)
            pn, pp = pn+1, pp+1
            # print("append new:", nums)
            
            while self.valid(nums, pattern) == False:
                if nums[pn] < 9: 
                    if pattern[pp-1]=="I":
                        nums[pn] = nums[pn]+1
                    else:
                        nums.pop()
                        pn, pp = pn-1, pp-1
                        nums[pn] = nums[pn]+1
                else: 
                    nums.pop()
                    pn, pp = pn-1, pp-1
                    nums[pn] = nums[pn]+1
                # print("end of 2nd while loop:", nums)
            
            # print("end of 1st while loop:", nums)
        
        output = ""
        for i in nums:
            output = output + str(i)
        return output

    def valid(self, nums, pattern):
        '''
        check if a list is valid: use every number once, between 1 to 9, consistent with pattern
        '''
        if len(nums)>len(set(nums)): return False # use every number once

        for i in nums: # between 1 to 9
            if i<1 or i>9: return False

        for i in range(len(nums)-1): # consistent with pattern
            if pattern[i]=="I" and nums[i]>=nums[i+1]: return False
            if pattern[i]=="D" and nums[i]<=nums[i+1]: return False

        return True
        
                
            
