import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heap.append(num)

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return heap[0]