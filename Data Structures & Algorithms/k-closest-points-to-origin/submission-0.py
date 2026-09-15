import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_heap = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(dis_heap, [distance, point])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(dis_heap)[1])
        
        return res