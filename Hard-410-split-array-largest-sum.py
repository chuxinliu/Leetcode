class Solution:
    
    def mini(self, mid, nums, m):
        '''
        a function to see if a certain minimum can be achieve in m subarrays
        '''
        i,n = 0, len(nums)
        while m>1 and i<n:
            cnt = mid
            while cnt-nums[i]>=0:
                cnt, i = cnt-nums[i], i+1
                if i==n: break
            m-=1
        return sum(nums[i:])<=mid
    
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        binary search
        '''
        i, j = max(nums), sum(nums)
        while i<j:
            mid = floor(0.5*(i+j))
            if self.mini(mid, nums, m): j = mid
            else: i = mid+1      
        return i
