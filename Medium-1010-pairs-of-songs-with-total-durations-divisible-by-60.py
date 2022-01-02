class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        residue60 = [0]*60
        for i in time:
            r = i%60
            residue60[r] += 1
            
        output = 0
        if residue60[0]>1:
            output+=residue60[0]*(residue60[0]-1)/2
        for i in range(1,30):
            output += residue60[i]*residue60[60-i]
        if residue60[30]>1:
            output+=residue60[30]*(residue60[30]-1)/2
        
        return output
            
            
        
