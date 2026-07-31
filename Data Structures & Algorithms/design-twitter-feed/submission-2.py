from collections import defaultdict
from heapq import heapify, heappush, heappop

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        h = []
        followees = self.followMap[userId]
        for f in followees:
            if f == userId:
                continue
            h += self.tweetMap[f]
        h += self.tweetMap[userId] 
        heapify(h)
        i = 0
        while i < 10 and h:
            time, tweet = heappop(h)
            news_feed.append(tweet)
            i += 1
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)