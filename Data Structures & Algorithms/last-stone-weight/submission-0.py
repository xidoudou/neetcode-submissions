class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-i for i in stones]
        heapq.heapify(self.max_heap)
        while len(self.max_heap) > 1:
            n1 = - heapq.heappop(self.max_heap)
            n2 = - heapq.heappop(self.max_heap)
            if n1 > n2:
                heapq.heappush(self.max_heap, -(n1 - n2))
            elif n2 > n1:
                heapq.heappush(self.max_heap, -(n2 - n1))
        return - self.max_heap[0]
