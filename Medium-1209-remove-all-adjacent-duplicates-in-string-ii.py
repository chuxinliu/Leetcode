class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        output, last, i, count = [], "", 0, 0
        while i<len(s):
            letter = s[i]
            output.append(letter)
            if letter == last: 
                count+=1
                if count == k:
                    for w in range(k):
                        output.pop()
                    if len(output)>0:
                        last, count = output[-1], 0
                        for j in range(len(output)):
                            if output[len(output)-j-1]==last: count+=1
                            else: break
                    else: last, count = "", 0
            else: last, count = letter, 1
            i+=1
        
        return ''.join(output)
