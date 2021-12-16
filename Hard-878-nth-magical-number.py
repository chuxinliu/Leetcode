import numpy as np
class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # if one % the other == 0
        if a%b==0 or b%a==0:
            res = (n*min(a,b)) % (10**9 + 7) 
            return res
        
        # if one % the other != 0
        else:
            lcm = np.lcm(a, b)
            n_lcm = lcm/a + lcm/b - 1
            q = n // n_lcm
            r = n % n_lcm
            
            # if no remainder
            if r == 0:
                res = (q*lcm) % (10**9 + 7)
                return res
            
            # if remainder>0
            else: 
                i,j=1,1
                while r>1:
                    # 2 scenarios
                    if i*a<j*b:
                        i+=1
                    else:
                        j+=1
                    r-=1
                res = (q*lcm + min(i*a, j*b)) % (10**9 + 7)
                return res
            
