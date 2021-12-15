class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(str(s))
        
        if len(s_list)==1:
            return 1
        else:
            a,b,power,p=0,1,1,1
            while b<len(s_list):
                if s_list[a]==s_list[b]:
                    p+=1
                    power = max(power, p)
                else:
                    p=1
                a,b=a+1,b+1
            return power
        
        
