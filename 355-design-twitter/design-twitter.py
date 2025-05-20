from collections import defaultdict,deque
from heapq import heappush,heappop
class Twitter:

    def __init__(self):
        self.counter = 0
        self.users = defaultdict(set)
        self.tweetfeed = defaultdict(deque)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].add(userId)
        self.tweetfeed[userId].appendleft((self.counter,tweetId))
        self.counter+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        followees = self.users[userId]
        count = 0
        for followee in followees:
            for count,tweetId in list(self.tweetfeed[followee])[:10]:
                heappush(heap,(-count,tweetId))

        feedcount = 0
        heaplength = len(heap)
        while(feedcount<min(10,heaplength)):
            res.append(heappop(heap)[1])
            feedcount+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        # self.users[followerId].add(followerId)
        # self.users[followerId].add(followeeId)
        # self.users[followeeId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)