from heapq import heappush,heappop
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        heap = []
        heappush(heap,(1,beginWord))

        visited = set()
        visited.add(beginWord)
        while(heap):
            word = heappop(heap)
            if word[1] == endWord:
                return word[0]
            for i in range(len(word[1])):
                for letter in letters:
                    newword = word[1][:i]+letter+word[1][i+1:]
                    if newword in wordset and newword not in visited:
                        visited.add(newword)
                        heappush(heap,(1+word[0],newword))
        return 0
            
            