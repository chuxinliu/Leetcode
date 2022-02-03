class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        zero, one = 0,0
        for i in nums:
            if i==1: one+=1
            else: zero+=1
        
        score = [[one, 0]]
        left, right = 0, one
        for i in range(len(nums)):
            if nums[i] == 0 :
                left += 1
            else:
                right -= 1
            score.append([left+right, i+1])
        
        sscore = sorted(score)
        m = sscore[-1][0]
        
        output = []
        for i in score:
            if i[0]==m:
                output.append(i[1])
                
        return output
        
