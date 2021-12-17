# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer = l1
        add = 0
        
        while pointer and l2:
            if pointer.val + l2.val + add < 10:
                pointer.val = pointer.val + l2.val + add
                add = 0
            else:
                pointer.val = pointer.val + l2.val + add - 10
                add = 1
            
            if pointer.next == None and l2.next!=None:
                back = pointer
            if pointer.next == None and l2.next==None:
                end = pointer

            pointer, l2 = pointer.next, l2.next
        
        try:
            back.next = l2
            pointer = l2
        except:
            a=0
        
        while pointer:
            if pointer.val + add < 10:
                pointer.val = pointer.val + add
                add = 0
            else:
                pointer.val = pointer.val + add - 10
                add = 1
            
            if pointer.next == None:
                end = pointer
                
            pointer = pointer.next
        
       
        try:
            if add == 1 and end!=None:
                new = ListNode(1)
                new.next = None
                end.next = new
        except:
            a=0

        return l1
        
