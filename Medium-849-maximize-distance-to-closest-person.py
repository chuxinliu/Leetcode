class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n=len(seats)
        s=0
        zeros=[]
        if seats[0]==0:
            for i in range(1,n):
                if seats[i]==1:
                    s=i
                    zeros.append(2*i-1)
                    break
        if s+1<n:
            for i in range(s+1,n):
                if seats[i]==0:
                    if seats[i-1]==1: # this is a first zero
                        n_zeros=1
                        s=0
                    if seats[i-1]==0: # this is a continuing zero
                        n_zeros+=1
                        if i==n-1: # and also the last element
                            n_zeros=2*n_zeros-1
                            zeros.append(n_zeros)
                # this is a first 1
                if seats[i]==1 and seats[i-1]==0:
                    zeros.append(n_zeros)
        
        zeros = sorted(zeros)
        return ceil(zeros[-1]/2)
