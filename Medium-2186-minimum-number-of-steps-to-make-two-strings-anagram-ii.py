class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = collections.Counter(list(s)), collections.Counter(list(t))
        cd1, cd2 = cs-ct, ct-cs
        return cd1.total()+cd2.total()
