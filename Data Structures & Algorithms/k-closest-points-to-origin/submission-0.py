import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        for point in points:
            x = point[0]
            y = point[1]

            distance = (x * x) + (y * y)
            heapq.heappush(max_heap, (-distance, point))

        while len(max_heap) > k:
            distance, point = heapq.heappop(max_heap)
        while max_heap:
            distance, point = heapq.heappop(max_heap)
            result.append(point)
        return result