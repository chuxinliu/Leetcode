# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next==None:
            return True
        
        else:
            # 4 pointers: fast, slow, front, back
            # fast moves 2 steps a time, slow moves 1 step a time
            # slow makes reverse linked list at the same time
            
            slow, fast = head, head.next
            back, front = None, head.next
            
            try:
                while fast.next:
                    fast = fast.next.next
                    slow.next = back
                    back = slow
                    slow = front
                    front = front.next
            except:
                fast = fast
                
            if fast!=None: 
                slow.next = back
                while slow and front:
                    if front.val != slow.val:
                        return False
                    else:
                        front, slow = front.next, slow.next
                if front == None and slow==None:
                    return True
            if fast == None:
                while back and front:
                    if back.val!=front.val:
                        return False
                    else:
                        back, front = back.next, front.next
                if back==None and front==None:
                    return True
 
