class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getmax(list_nums):
            
            if len(list_nums)==1:
                return list_nums[0]
            if len(list_nums)==2:
                return min(list_nums)*max(list_nums)+max(list_nums)
            
            if len(list_nums)>=3:
                max_coins= []
                for i in range(0,len(list_nums)):
                    if i==0:
                        coins=list_nums[i]*list_nums[i+1]
                    elif i==len(list_nums)-1:
                        coins=list_nums[i]*list_nums[i-1]
                    else:
                        coins=list_nums[i-1]*list_nums[i]*list_nums[i+1]
                    max_coins.append(coins)
                    left_bl = list_nums[0:i]+list_nums[i+1:]
                    max_coins.append(coins+getmax(left_bl))
                return max(max_coins)
        
        return getmax(nums)
