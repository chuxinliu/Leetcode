class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n=len(plantTime)
        combine_Time = []
        for i in range(n):
            combine_Time.append([growTime[i],plantTime[i]])
        
        sorted_growTime = sorted(combine_Time)
        sum_plantTime = sum(plantTime)
        output = sum(plantTime) + sorted_growTime[0][0]
        
        for i in range(1,n):
            sum_plantTime -= sorted_growTime[i][1]
            min_growTime = sorted_growTime[i][0]
            output = max(output, sum_plantTime + min_growTime)
        
        return output
