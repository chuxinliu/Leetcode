class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        letters, idx = "abcdefghijklmnopqrstuvwxyz", []
        for l in letters:
            start, end = len(s), -1
            for i in range(len(s)):
                if s[i] == l: start, end = min(start, i), max(end, i)
            if start<len(s): idx.append([start, end])
            
        if len(s)==1: return [1]
        
        sidx = sorted(idx)
        end, pidx = sidx[0][1], []
        for i in sidx:
            if i[0]>end: 
                pidx.append(end)
                end = i[1]
            else: end = max(end, i[1])
        pidx.append(len(s)-1)            
        end, output = -1, []
        for i in pidx:
            output.append(i-end)
            end = i
        return output
        
                
                
        
                    
                    
        
