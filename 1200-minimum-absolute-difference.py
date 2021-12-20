class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr_sorted = sorted(arr)
        arr_diff = []
        for i in range(1, len(arr_sorted)):
            arr_diff.append((arr_sorted[i]-arr_sorted[i-1]))
        
        # find minimum absolute difference
        mad = min(arr_diff)
        
        output = []
        for i in range(0, len(arr_diff)):
            if arr_diff[i]==mad:
                new = [arr_sorted[i], arr_sorted[i+1]]
                output.append(new)
        return output
