# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head!=None:
            
            # 2 pointers, 1 extra memory to remember the start of even
            odd, even, start_even = head, head.next, head.next
            
            # point odd and even 2 nodes away, and then move 1 node
            while odd.next!=None and even.next!=None:
                odd.next=odd.next.next
                even.next=even.next.next
                odd, even = odd.next, even.next
            
            #finally, point odd to start of even
            odd.next = start_even
        
        return head
