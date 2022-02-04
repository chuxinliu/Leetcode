class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff10 = 0
        diff = [0]
        for i in nums:
            if i==0: diff10 -=1
            else: diff10 +=1
            diff.append(diff10)
        
        dict_diff = {}
        max_len = 0
        for i in range(len(diff)):
            if str(diff[i]) not in dict_diff: dict_diff[str(diff[i])] = i
            else: max_len = max(max_len, i - dict_diff[str(diff[i])])
        return max_len
