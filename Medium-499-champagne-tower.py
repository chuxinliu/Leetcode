class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[poured]]
        i = 0
        while i<=query_row:
            last_row = [0] + glasses[-1]+ [0]
            curr_row = []
            for j in range(len(last_row)-1):
                curr_row.append(0.5*(max(0,last_row[j]-1)+max(0, last_row[j+1]-1)))
            glasses.append(curr_row)
            i+=1
        return min(float(1), glasses[query_row][query_glass])
