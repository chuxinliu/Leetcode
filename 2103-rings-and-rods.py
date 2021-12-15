class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        #separate rings into a list
        rings_list = []
        for letter in rings:
            l = str(letter)
            rings_list.append(l)
        
        #two pointer techniques: one is color, the other is number
        slow, fast = 0, 1
        R, G, B = [], [], []
        while slow<len(rings_list):
            if rings_list[slow]=="R":
                R.append(int(rings_list[fast]))
            if rings_list[slow]=="G":
                G.append(int(rings_list[fast]))
            if rings_list[slow]=="B":
                B.append(int(rings_list[fast]))
            slow += 2
            fast += 2
        
        S = set(R).intersection(set(G),set(B))
        n = len(S)
        
        return n


  
