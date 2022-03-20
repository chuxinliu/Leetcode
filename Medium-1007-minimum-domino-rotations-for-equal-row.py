class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:          
        for i in range(6):
            t,b,f=0,0,0
            for j in range(len(tops)):
                if tops[j]!=i+1 and bottoms[j]!=i+1: f=1
                elif tops[j]!=i+1 and bottoms[j]==i+1: t+=1
                elif tops[j]==i+1 and bottoms[j]!=i+1: b+=1
            if f==0: return min(t,b)    
        return -1
