class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        sbeans = sorted(beans)
        outputset = []
        total = sum(sbeans)
        n = len(beans)
        for i in range(n):
            outputset.append(total - (n-i)*sbeans[i])
        return min(outputset)
