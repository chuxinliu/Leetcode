class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        si = sorted(intervals)
        start, end = si[0][0], si[0][1]
        
        output = len(si)
        wi = 0
        for i in range(1, len(si)):
            if si[i][1]<=end: output-=1
            else:
                wi = i
                end = si[i][1]
                if si[i][0]==start: output-=1
                else: start = si[i][0]

        return output
