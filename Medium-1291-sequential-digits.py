class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        output = []
        for a in range(len(str(low)),len(str(high))+1):
            for b in range(1,11-a):
                num = str(b)
                for c in range(b+1, b+a):
                    num += str(c)
                if int(num)>=low and int(num)<=high:
                    output.append(int(num))
        return output
