class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        sliding window: 2 pointers
        '''
        
        n1, n2 = len(s1), len(s2)
        cs1 = collections.Counter(list(s1))
        
        ## (1) find the first pointer
        for i in range(n2):
            if cs1[s2[i]]>0:
                p1 = i
                break
            if i == n2-1: return False
        
        ## (2) second pointer
        p2 = p1+n1
        
        ## (3) sliding the window while reading at index i
        i = p1
        while p2<=n2:
            while i<p2:
                if cs1[s2[i]]>0: 
                    cs1[s2[i]]-=1
                    i+=1
                    if i == p2: return True
                else:
                    cs1[s2[p1]]+=1
                    p1, p2 = p1+1, p2+1
                    break 
        
        return False
