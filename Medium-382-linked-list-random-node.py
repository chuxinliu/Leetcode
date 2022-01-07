# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        # count total number of nodes in linked list
        n = 0
        head = self.head
        pointer = head
        while pointer!=None:
            n+=1
            pointer=pointer.next
        
        # get a random number between 1 and n
        k = random.randint(1, n)
        # move to kth node
        while k>1:
            head = head.next
            k-=1
        
        return head.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
