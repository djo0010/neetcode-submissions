import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            rock1 = heapq.heappop(heap)
            rock2 = heapq.heappop(heap)
            if -rock1 > -rock2:
                brokenRock = rock1 - rock2
                heapq.heappush(heap, brokenRock)
            elif -rock1 < -rock2:
                brokenRock = rock2 - rock1
                heapq.heappush(heap, brokenRock)
            print(heap)

        if len(heap) == 0:
            return 0

        return -heap[0]