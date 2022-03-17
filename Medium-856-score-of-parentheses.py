class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        if not s: return 0
        
        s2 = s[0:2]
        if s2=='()': return 1 + self.scoreOfParentheses(s[2:])
        if s2=="((":
            i, p = 0, 0
            while i<len(s):
                if s[i]=='(': p+=1
                else: p-=1
                if p==0: return 2*self.scoreOfParentheses(s[1:i])+self.scoreOfParentheses(s[i+1:])
                i+=1
