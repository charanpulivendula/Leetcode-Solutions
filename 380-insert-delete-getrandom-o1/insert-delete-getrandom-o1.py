from random import choice
from collections import defaultdict
class RandomizedSet:
    def __init__(self):
        self.hashmap = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        val = self.hashmap[choice(list(self.hashmap.keys()))]
        return val
        # print(choice(self.hashmap.keys()))
        # val = self.hashmap[choice(self.hashmap.keys())]
        # # self.hashmap[val] = val
        # return val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()