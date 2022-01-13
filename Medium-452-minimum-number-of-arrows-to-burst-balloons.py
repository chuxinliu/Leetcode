class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # sort ballons by the end point
        points.sort(key=lambda s: s[1])
        
        # pop the right end
        i, arrow, n = 0,0,len(points)
        while i<n:
            pop = points[i][1]
            arrow+=1
            # skip those that are pop at the same time
            while points[i][0]<=pop:
                i+=1
                if i==n:
                    break
                    
        return arrow
