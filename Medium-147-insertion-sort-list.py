# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next != None:
            
            # 4 pointers: head, moving, back, front
            moving, back, front = head, head, head.next

            
            while back and back.next and front:

                # if front.val < back.val: (1) to beginning (2) to middle
                if front.val<back.val:
                    back.next = back.next.next
                    # (1) to beginning
                    if front.val<=head.val:
                        front.next = head
                        head, moving = front, front
                        front = back.next
                    # (2) to middle
                    else: 
                        while moving.next.val<front.val:
                            moving = moving.next
                        new = moving.next
                        moving.next = front
                        front.next = new
                        front = back.next
                        moving = head
                        

                # if front.val >= back.val: back and front move 1 step
                else:
                    back, front = back.next, front.next

        return head
            
        
        
