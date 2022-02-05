class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        # find all possible ways 
        ways = []
        if targetSeconds<100:
            ways.append(str(targetSeconds))
            if targetSeconds>=60:
                str_m = "1"
                s = targetSeconds - 60
                str_s = str(s)
                if s<10:
                    str_s = "0" + str_s
                ways.append(str_m+str_s)
        else:
            m1 = targetSeconds // 60
            s1 = targetSeconds - m1*60
            str_m1 = str(m1)
            str_s1 = str(s1)
            if s1<10:
                str_s1 = "0" + str_s1
            ways.append(str_m1+str_s1)
            if s1<40:
                m2 = m1-1
                s2 = s1+60
                ways.append(str(m2)+str(s2))
        
        # get total cost for all ways
        total_cost = []
        for w in ways:
            if len(w)<5: # check if it is less than 5 digits
                cost = 0
                start = str(startAt)
                for n in w:
                    if n!=start:
                        cost += moveCost+pushCost
                        start = n
                    else:
                        cost += pushCost
                total_cost.append(cost)
        
        return min(total_cost)
