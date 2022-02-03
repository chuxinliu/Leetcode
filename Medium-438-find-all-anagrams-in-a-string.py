class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        i, j = 0, len(p) # two pointers for the sliding window
        window, cp = collections.Counter(s[:len(p)]), collections.Counter(p)
        
        output = []
        while j<=len(s):
            if window == cp: 
                output.append(i)
            
            # (1) take i out of the window
            window[s[i]]-=1
            if window[s[i]]<0: window.pop(s[i]) # if i doesn't belong, pop it
            
            # (2) put j into the window
            if j<len(s): window[s[j]]+=1
            
            # slide the window pointers
            i, j = i+1, j+1
            
        return output
                    
