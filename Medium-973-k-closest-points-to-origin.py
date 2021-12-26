class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # create a list of pairs of point's index and its distance**2
        list_index_dist = []        
        for i in range(len(points)):
            index_dist = []
            index_dist.append(points[i][0]**2+points[i][1]**2)
            index_dist.append(i)
            list_index_dist.append(index_dist)
        
        # sort the pairs by distance
        sorted_list_index_dist = sorted(list_index_dist)

        # retrieve the points for the first k smallest distance**2
        output = []
        i=0
        while k>0:
            index = sorted_list_index_dist[i][1]
            output.append(points[index])
            i+=1
            k-=1
        
        return output
        
