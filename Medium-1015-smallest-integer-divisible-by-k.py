class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k%2==0 or k%5==0:
            return -1            
        
        i,n=1,1
        while i<10**5:
            if n%k==0:
                return i
            else:
                n=n*10+1
                i+=1
        return -1
        
