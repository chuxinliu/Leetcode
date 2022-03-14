class Solution:
    def simplifyPath(self, path: str) -> str:
        
        i, n, word, stack = 1, len(path), '', []
        while i<n:
            if path[i]!='.' and path[i]!='/': word+=path[i]
            elif path[i]=='.':
                if path[i-1:min(i+2, n)]=='/./' or path[i-1:n]=='/.':i+=1
                elif path[i-1:min(i+3,n)]=='/../' or path[i-1:n]=='/..':
                    if stack: stack.pop()
                    i+=2
                else: word+=path[i]
            else:
                if word:
                    stack.append(word)
                    word = ''
            i+=1
                
            if i==n and word: stack.append(word)
                
        output = ''
        if not stack: return '/'
        for i in stack:
            output += ('/'+i)
        return output
