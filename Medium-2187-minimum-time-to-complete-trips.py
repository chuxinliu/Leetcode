class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        st  = sorted(time)
        
        # Bi-section Search
        small, big = st[0], st[0]*totalTrips
        
        while True:
            
            t = floor(0.5*(small+big))
            
            # calculate total trips within time t
            trips = 0
            for i in st:
                if i<=t: trips += floor(t/i)
                else: break
                    
            # adjust upper and lower bounds
            if trips<totalTrips:
                if small == t: small += 1
                else: small = t          
            elif trips==totalTrips: 
                if small == t: return t
                else: big = t 
            else: 
                if big == t: return t
                big = t
