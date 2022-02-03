class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Step 1: turn a 4-sum problem into 2-sum proble
        n = len(nums1)
        sum12, sum34 = [], []
        for i in range(0, n):
            for j in range(0, n):
                sum12.append(nums1[i]+nums2[j])
                sum34.append(nums3[i]+nums4[j])
        sum12, sum34 = sorted(sum12), sorted(sum34)
        
        # Step 2: search from different ends
        output = 0
        # sum12 starts from smallest, sum34 starts from largest
        i , j = 0, n**2-1 
        while i<n**2 and j>=0:
            count12, count34 = 0, 0
            target = -sum12[i]
            while sum12[i]==-target: 
                count12+=1
                i+=1
                if i>=n**2: break
            while sum34[j]>target:
                j-=1
                if j<0: break
            while sum34[j]==target:
                count34+=1
                j-=1
                if j<0: break
            output += count12*count34
        
        return output
        
    
