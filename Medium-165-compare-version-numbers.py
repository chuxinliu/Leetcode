class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:  
        def get_values(v):
            val, n = [], ""
            for i in range(len(v)):
                if v[i]==".": 
                    val.append(int(n))
                    n = ""
                else:
                    n += v[i]
                    if i == len(v)-1: val.append(int(n))
            return val
        
        val1, val2 = get_values(version1), get_values(version2)
        n1, n2 = len(val1),len(val2)
        val1 += [0]*max(0, n2-n1)
        val2 += [0]*max(0, n1-n2)
        
        for i in range(len(val1)):
            if val1[i]>val2[i]: return 1
            if val1[i]<val2[i]: return -1

        return 0
