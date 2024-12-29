class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        wordset = set(bank)
        if endGene not in wordset:
            return -1
        letters = "ACGT"
        heap = []
        heappush(heap,(0,startGene))

        visited = set()
        visited.add(startGene)
        while(heap):
            word = heappop(heap)
            if word[1] == endGene:
                return word[0]
            for i in range(len(word[1])):
                for letter in letters:
                    newword = word[1][:i]+letter+word[1][i+1:]
                    if newword in wordset and newword not in visited:
                        visited.add(newword)
                        heappush(heap,(1+word[0],newword))
        return -1