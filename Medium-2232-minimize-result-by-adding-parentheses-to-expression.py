class Solution:
    def minimizeResult(self, expression: str) -> str:
        
        n1 = 0
        for i in expression:
            if i!="+": n1+=1
            else: break
        n2 = len(expression)-n1-1
        s1, s2 = expression[:n1], expression[n1+1:]
        
        output = []
        for i in range(n1):
            for j in range(n2):
                new_e = expression[:i]+'('+expression[i:(n1+2+j)]+')'+expression[(n1+2+j):]
                if s1[:i]=='': first = 1
                else: first = int(s1[:i])
                if s2[j+1:]=='': last = 1
                else: last = int(s2[j+1:])
                middle1,middle2 = int(s1[i:]), int(s2[:j+1])
                total = first*(middle1+middle2)*last
                output.append([total, new_e])
        
        so = sorted(output)
        return so[0][1]
