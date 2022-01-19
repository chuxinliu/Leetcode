# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow,fast=head,head
        try:
            while fast.next:
                slow, fast = slow.next, fast.next.next
                if slow==fast:
                    while slow!=head:
                        head,slow=head.next, slow.next
                    return head
        except:
            return None
        
