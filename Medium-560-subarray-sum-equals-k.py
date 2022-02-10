class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        c = collections.Counter()
        for i in nums:
            total += i
            c[str(total)]+=1        
        
        output = c[str(k)]
        total = 0
        for i in nums: 
            total += i
            c[str(total)]-=1
            output += c[str(total+k)]
        return output
