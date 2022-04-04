class Solution:
    def swapNodes(self, head, k):
        pk, pnk = self.toidx(head, k), self.toidx(head, self.getleng(head)-k+1)
        pk.val, pnk.val = pnk.val, pk.val
        return head
    
    def getleng(self, head): 
        leng = 0
        while head:
            leng+=1
            head = head.next
        return leng
    
    def toidx(self, head, j):
        p = head
        while j>1:
            p = p.next
            j-=1
        return p
