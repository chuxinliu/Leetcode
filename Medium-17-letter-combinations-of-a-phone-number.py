class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        adict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                 "6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
        
        output = []
        for i in digits:  
            if not output: 
                for j in adict[i]:
                    output.append(j)
            else: 
                n1, n2 = len(output), len(adict[i])
                output = output * n2
                for j in range(n2):
                    for w in range(n1):
                        idx = j*n1 + w
                        output[idx] = output[idx]+adict[i][j]
        
        return output
