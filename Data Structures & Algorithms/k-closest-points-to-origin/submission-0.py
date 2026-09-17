class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(self.heap, (dis, x, y))
        res =[]
        for _ in range(k):
            dis, x, y = heapq.heappop(self.heap)
            res.append([x,y])
        return res

