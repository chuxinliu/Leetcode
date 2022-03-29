class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        i, j, bk = 0, len(nums)-1, 0 
        # bi-search for split point
        while i<=j and bk == 0:
            mid = floor(0.5*(i+j))
            if nums[i]==nums[mid] and nums[j]==nums[mid]: 
                i+=1
                if i>j: split = j
            elif nums[i]>nums[mid]: j = mid
            elif nums[mid]>nums[j]: 
                if i==mid: split, bk = j, 1
                i = mid
            else: split, bk = i, 1
        
        # bi-search for target
        snums = nums[split:]+nums[:split]
        i, j = 0, len(nums)-1
        while i<=j:
            mid = floor(0.5*(i+j))
            if snums[mid]==target: return True
            elif snums[mid]>target: j = mid-1
            else: i = mid+1
        return False 
