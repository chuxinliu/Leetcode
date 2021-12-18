class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        # Step 1: convert n into an array of 10 digits, find number of digits that' smaller than n
        array = []
        r = n
        for i in range(0,10):
            d = 10**(9 - i)
            array.append((r//d))
            r = r % d
        # Step 2: number of digits thats above, equal, or below n's each digit
        arr_above, arr_equal, arr_below = [],[],[]
        for i in range(0,10):
            above, equal, below = 0, 0, 0
            for j in range(0, len(digits)):
                if int(digits[j])>array[i]:
                    above += 1
                if int(digits[j])<array[i]:
                    below += 1
                if int(digits[j])==array[i]:
                    equal = 1
            arr_above.append(above)
            arr_equal.append(equal)
            arr_below.append(below)
        
        
        # Step 3: count all below the highest digit
        output,i,leng = 0, 0, len(digits)
        while array[i]==0:
            i += 1
        k=i
        while i<9:
            output = output + leng**(9-i)
            i += 1
            
        # Step 4: deal with the remaining
        output = output + arr_below[k]*(leng**(9-k))
        
        if arr_equal[k] == 1:
            q=k+1
            while q<10:
                output = output+arr_below[q]*(leng**(9-q))
                if arr_equal[q]==1:
                    q=q+1
                else:
                    q=99
            if q==10:
                output+=1

        return output
