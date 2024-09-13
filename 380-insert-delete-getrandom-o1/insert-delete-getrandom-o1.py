from random import randint,choice
class RandomizedSet:

    def __init__(self):
        self.RandomSet = set()

    def insert(self, val: int) -> bool:
        if val not in self.RandomSet:
            self.RandomSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.RandomSet:
            self.RandomSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(list(self.RandomSet))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()