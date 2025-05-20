from collections import defaultdict,deque
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweetfeed = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetfeed.append((userId,tweetId))
        self.users[userId].add(userId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 0
        for person,tweetId in reversed(self.tweetfeed):
            if count >= 10:
                return res
            if person in self.users[userId]:
                res.append(tweetId)
                count+=1
            
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