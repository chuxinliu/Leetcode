class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        balls = []
        for i in range(len(boxes)):
            if boxes[i]=="1":
                balls.append(i)
                
        output=[]
        for i in range(len(boxes)):
            m=0
            for j in balls:
                m+=abs(j-i)
            output.append(m)
            
        return output
