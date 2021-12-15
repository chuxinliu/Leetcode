# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1==None:
            return list2
        if list2==None:
            return list1
        
        if list1!=None and list2!=None:
            
            # 3 steps:
            # find the small node, point to small, move pointer
            if list1.val <= list2.val:
                head = list1
                list1= list1.next
            else:
                head = list2
                list2= list2.next

            pointer = head

            # continue until when one list is over: 
            while list1!=None and list2!=None:
                if list1.val <= list2.val:
                    pointer.next = list1
                    list1= list1.next
                else:
                    pointer.next = list2
                    list2= list2.next
                pointer = pointer.next

            # point to the rest of the other list
            if list2==None:
                pointer.next = list1
            if list1==None:
                pointer.next = list2

            return head

        
