class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output=[]
        for i in queries:
            p = 0
            x1,x2,d2 = i[0],i[1],i[2]**2
            for j in points:
                if (x1-j[0])**2+(x2-j[1])**2<=d2:
                    p+=1
            output.append(p)
        return output
