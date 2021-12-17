# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head==None:
            return head
        
        if head.next==None:
            return head
        
        
        # find length and reminder
        l=0
        pointer = head
        while pointer:
            l+=1
            pointer=pointer.next
        
        rmd = k % l 
        
        if rmd == 0:
            return head
        
        # new linked list start at (l-rmd)
        n = l-rmd
        start=head
        while n>1:
            start=start.next
            n-=1
        end = start
        start = start.next
        end.next = None
        # start moves to original linked list's end
        pointer = start
        while pointer.next:
            pointer=pointer.next
        pointer.next = head
        return start
            
        
        
        
