"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 3 pointers: p1 reaches child, p2 goes next, p3 follows child
        p1 = head
        while p1!=None:
            try:
                while p1.child==None:
                    p1 = p1.next
            except:
                return head
            p2,p3 = p1.next,p1.child
            p1.next,p3.prev,p1.child = p3,p1,None
            while p3.next!=None:
                p3=p3.next
            if p2!=None:
                p3.next, p2.prev = p2, p3
