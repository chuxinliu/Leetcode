class Solution:
    def minPartitions(self, n: str) -> int:
        
        m=0
        # simply find the largest number in this string
        for i in n:
            k = int(i)
            if k>m:
                m=k
            # if finds 9, finish the program early!
            if m==9:
                return 9
        return m
        
