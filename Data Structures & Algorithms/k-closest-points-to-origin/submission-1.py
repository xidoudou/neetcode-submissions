class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = x ** 2 + y ** 2
            heapq.heappush(heap, (dis, x, y))
        res =[]

        for _ in range(k):
            dis, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res

