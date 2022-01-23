class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snums = sorted(nums)
        neighbor, multiple = [], []
        i=0
        
        while i < len(nums)-1:
            if snums[i]==snums[i+1]:
                multiple.append(snums[i])
            if snums[i]+1==snums[i+1]:
                neighbor.append(snums[i])
                neighbor.append(snums[i+1])
            i+=1
        
        return list(set(snums)-set(neighbor)-set(multiple))
