class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        # count total number of seats
        seats = [i for i, x in enumerate(corridor) if corridor[i] == "S"]
        if len(seats)%2==1 or len(seats)<2: return 0
        if len(seats)==2: return 1
        
        # for every 2 seats, find number of plants between
        i, count_s = 0, 0
        count_p = []
        while i < len(corridor):
            if corridor[i]=='S':
                count_s += 1
                i+=1
                if count_s==2:
                    p = 0
                    if i<len(corridor):
                        while corridor[i]=='P':     
                            p+=1
                            i+=1
                            if i>=len(corridor):
                                break
                    count_p.append(p)
                    count_s = 0
            else: 
                i+=1
        
        # calculate total number of division
        total = 1
        for j in range(len(count_p)-1):
            total = total * (count_p[j]+1)
        return total % (10**9 + 7)
