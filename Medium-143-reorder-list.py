# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # exception solution
        if head.next == None:
            return head
        
        # Step 1: create a reverse list for the second half
        
        #-----------------------
        # 2 pointers: slow, fast
        slow, fast = head, head.next
        
        try:
            while fast.next.next!=None:
                slow, fast = slow.next, fast.next.next
        except:
            fast=fast
        
        back, curr, front = None, slow.next, slow.next.next
        slow.next = None
        while front:
            curr.next = back
            back,curr,front=curr,front,front.next
        curr.next = back

        #-----------------------
        #Step 2: combine 2 lists
        
        # 4 pointers: b1,b2,f1,f2
        b1, f1 = head, head.next
        b2, f2 = curr, curr.next
              
        try:
            while b1:
                b1.next = b2
                if f1:
                    b2.next = f1
                b1, f1 = f1, f1.next
                b2, f2 = f2, f2.next
        except:
            print("Happy!")
