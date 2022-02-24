# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head:
            # get values, sort in a list
            values = []
            while head:
                values.append(head.val)
                head = head.next
            sv = sorted(values)
            
            # create a new linked-list with the right order of values
            root = ListNode()
            head = root
            for i in range(len(sv)):
                root.val = sv[i]
                if i<len(sv)-1:
                    root.next = ListNode()
                    root = root.next
        return head
