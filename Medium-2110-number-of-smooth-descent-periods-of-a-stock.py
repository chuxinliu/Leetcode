class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        
        # find length of list that are smooth descent
        arr = []
        psd = prices[0]
        k=1
        for i in range(1,n):
            if prices[i]+1==psd:
                k+=1
            else:
                if k!=1:
                    arr.append(k)
                k=1
            psd = prices[i]
        if k!=1:
            arr.append(k)
        
        # calculate output
        output = n
        for i in range(0,len(arr)):
            a = arr[i]-1
            a_max = 0
            while a>=0:
                a_max += a
                a-=1
            output += a_max
        
        return output
