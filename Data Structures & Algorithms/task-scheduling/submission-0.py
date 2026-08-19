import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        time = 0
        max_heap = []

        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1

        for key, value in freq.items():
            heapq.heappush(max_heap, -value)

        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count != 0:
                    cooldown.append((count, time + n))

            if cooldown and cooldown[0][1] == time:
                count, available_time = cooldown.popleft()
                heapq.heappush(max_heap, count)
        return time

        
            

        


        