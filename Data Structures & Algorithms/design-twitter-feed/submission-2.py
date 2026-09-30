class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmp = defaultdict(list)       # [count, follw]
        self.followmp = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmp[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followmp[userId].add(userId)
        for followeeId in self.followmp[userId]:
            if followeeId in self.tweetmp:
                idx = len(self.tweetmp[followeeId]) - 1
                count, tweetId = self.tweetmp[followeeId][idx]
                minHeap.append([count, tweetId, followeeId, idx - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetmp[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx - 1])
        return res
 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmp[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmp[followerId]:
            self.followmp[followerId].remove(followeeId)