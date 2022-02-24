class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        4 pointers approach: back, p1, p2, front
        '''
        
        root = ListNode(0, head)
        
        try:
            back, p1, p2 = root, head, head.next
            while p1 and p2: 
                front, back.next = p2.next, p2
                p2.next, back = p1, p1
                p1 = front
                back.next = p1
                if p1: p2 = p1.next
                else: p2 = None
        except:
            return root.next
        
        return root.next

        
