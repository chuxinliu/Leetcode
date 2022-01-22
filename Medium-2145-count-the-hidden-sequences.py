class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n,small,big,x = len(differences),0,0,0
        for i in range(n):
            x+=differences[i]
            small,big=min(small,x),max(big,x)
            
        if (upper-lower)-(big-small)+1>0: return (upper-lower)-(big-small)+1
        else: return 0
