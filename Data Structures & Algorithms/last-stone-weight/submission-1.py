import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heap.append(-stone)

        heapq.heapify(heap)


        while len(heap) >= 2:
            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)

            if largest == second_largest:
                continue
            else:
                diff = abs(largest - second_largest)
                heapq.heappush(heap, -diff)

        return -heap[0] if heap else 0