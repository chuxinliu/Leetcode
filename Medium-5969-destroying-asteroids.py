class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        sorted_ast = sorted(asteroids)

        for i in range(len(sorted_ast)):
            if mass<sorted_ast[i]:
                return False
            mass += sorted_ast[i]
        return True
        
