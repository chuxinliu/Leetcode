class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        ln = list(num)
        
        while k>0:
            
            # when there is no need to proceed
            if len(ln)<=k: return '0'
            
            # find the first largest number to pop
            i = 0
            while i<len(ln)-1:
                # found the first largest
                if int(ln[i])>int(ln[i+1]): 
                    ln.pop(i)
                    k-=1
                    break
                # not the largest yet, keep moving
                else: 
                    i+=1
                    if i==len(ln)-1: 
                        ln.pop()
                        k-=1
            # if any leading zeros after poping 
            while ln[0]=='0':
                ln.pop(0)
                if not ln: return '0'
                
        return ''.join(ln)Me
