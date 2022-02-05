# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        k = len(lists)
        
        #######################################################################
        # when k<2
        if k==0: return None
        if k==1: return lists[0]
        
        #######################################################################
        # when k>=2
        
        ### I use a sorted **temp** list to remember values that their indexes
        temp = []
        for i in range(0, k):
            if lists[i]:
                temp.append([lists[i].val,i])
        temp = sorted(temp)
        
        ### initiate first node of output
        pointer = ListNode()
        prehead = pointer
        
        while temp:
            i = temp[0][1] # i is the index at lists
            pointer.next = lists[i]
            pointer = pointer.next
            lists[i] = lists[i].next
            
            ### if temp is longer than 1, pop the first element, otherwise: break
            if len(temp)==1: break
            else: temp.pop(0)

            if lists[i]:
                number_to_be_insert = lists[i].val
                j = 0 # j is the index at temp
                l_temp = len(temp)
                while number_to_be_insert>=temp[j][0]:
                    j+=1
                    if j==l_temp: break
                temp.insert(j, [number_to_be_insert,i])

        return prehead.next
        
