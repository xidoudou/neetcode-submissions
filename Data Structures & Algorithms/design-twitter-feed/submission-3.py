class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list) # userId -> [count, tweetID]
        self.followeemap = defaultdict(set) # userId -> set of followeeID
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        for followee in self.followeemap[userId]:
            if followee in self.tweetmap:
                index = len(self.tweetmap[followee]) - 1
                count, tweetId = self.tweetmap[followee][index]
                minHeap.append([count, tweetId, followee, index -1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index -1])
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeemap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeemap[followerId]:
            self.followeemap[followerId].remove(followeeId)
        
