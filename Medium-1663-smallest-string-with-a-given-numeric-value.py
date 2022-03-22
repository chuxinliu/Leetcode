class Solution:
    def getSmallestString(self, n: int, k: int) ->str:
        mid, end, letters = (k-n)%25, (k-n)//25, 'abcdefghijklmnopqrstuvwxyz'
        if mid == 0: return 'a'*(n-end)+end*'z'
        return 'a'*(n-end-1)+letters[mid]+end*'z'
