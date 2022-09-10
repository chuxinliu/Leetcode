class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
        n = len(properties)
        
        # sort descending by attack, O(nlogn)
        sp1 = sorted(properties, reverse = True)
        
        # sort ascending by defense if same attack, O(nlogn)
        sp2 = []
        attack = sp1[0][0]
        same_attack_properties = []
        for i in range(n):
            if sp1[i][0] == attack:
                same_attack_properties.append(sp1[i])
            else:
                sp2.extend(sorted(same_attack_properties, key = lambda x: x[1], reverse = False))
                attack = sp1[i][0]
                same_attack_properties = [sp1[i]]
        sp2 = sp2 + sorted(same_attack_properties, key = lambda x: x[1], reverse = False)
       
        # count number of property that has smaller defense and the maximum defense before it, O(n)
        max_d = sp2[0][1]
        output = 0
        for i in range(n):
            d = sp2[i][1]
            if d<max_d:
                output+=1
            max_d = max(max_d, d)
        
        return output
        
        
        
