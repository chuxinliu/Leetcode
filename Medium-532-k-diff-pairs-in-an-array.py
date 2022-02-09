class Solution(object):    
    def findPairs(self, nums, k):
        
        output = 0
        n = len(nums)
        
        if n>1:
            snums = sorted(nums)
            
            # first pointer: i
            i = 0
            # second pointer: j
            for f in range(1, n):
                if snums[f]>=snums[0]:
                    j = f
                    break

            while j<n:
                # (1) if satify, add 1 to output, move both pointers
                if snums[i]+k==snums[j]:
                    output += 1
                    i, j = i+1, j+1
                    while j<n:
                        if snums[j]==snums[j-1]: j+=1
                        else: break
                    while i<=j and i<n:
                        if snums[i]==snums[i-1]: i+=1
                        else: break
                    if i==j: j+=1
                
                # (2) if small, move back pointer
                elif snums[i]+k<snums[j]:
                    i += 1
                    while i<=j and i<n:
                        if snums[i]==snums[i-1]: i+=1
                        else: break
                    if i==j: j+=1
                
                # (3) if large, move front pointer
                else:
                    j += 1
                    while j<n:
                        if snums[j]==snums[j-1]: j+=1
                        else: break
        
        return output
                    
       
