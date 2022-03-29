class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = 1, len(nums)-1
        while i<=j:
            mid, cnt = floor(0.5*(i+j)), 0
            for k in nums: # count numbers <= mid
                if k<=mid: cnt+=1
            if cnt>mid: # duplicate is <= mid
                if j == mid: return mid
                else: j = mid
            else: i = mid + 1 # duplicate is > mid
