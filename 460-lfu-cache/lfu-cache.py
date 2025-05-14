class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  
        self.freq_map = defaultdict(OrderedDict)  
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, freq = self.cache[key]
        del self.freq_map[freq][key]

        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        self.freq_map[freq + 1][key] = None
        self.cache[key] = (value, freq + 1)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # promote frequency
            return

        if self.size >= self.capacity:
            lfu_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
            self.size -= 1

        self.cache[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1
        self.size += 1