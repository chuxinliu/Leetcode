class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [nums]
        
        pset = [nums]
        while pset:
            pset2=[]
            for p in pset:
                n = len(p)
                for i in range(n):
                    copy_p = p.copy(). # make a copy
                    copy_p.pop(i)      # drop one number
                    if copy_p not in output:
                        output.append(copy_p)
                        pset2.append(copy_p)
            pset = pset2
                
        return output    
                
            
        
