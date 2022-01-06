class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        on_car = [0]*1000
        
        for i in trips:
            for j in range(i[1],i[2]):
                on_car[j] += i[0]
        
        max_on_car = max(on_car)
        
        return max_on_car<=capacity
