class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive, negative, output = [], [], []
        for i in nums:
            if i>0: positive.append(i)
            else: negative.append(i)
        for j in range(len(positive)):
            output.append(positive[j])
            output.append(negative[j])
        return output
