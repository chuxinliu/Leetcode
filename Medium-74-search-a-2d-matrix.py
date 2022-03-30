class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nums = [] 
        for i in matrix: #flatten the matrix
            nums+=i

        i, j = 0, len(nums)-1
        while i<=j: #bi-section search
            mid = floor(0.5*(i+j))
            if nums[mid]==target: return True
            elif nums[mid]>target: j = mid-1 
            else: i = mid+1
        return False
