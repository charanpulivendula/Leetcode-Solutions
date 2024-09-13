class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictionary = defaultdict(int)
        def sorter(word1,word2):
            if dictionary[word1]!=dictionary[word2]:
                return dictionary[word1]<dictionary[word2]
            else:
                return word1 < word2
        
        for word in words:
            dictionary[word]+=1
        result = sorted(dictionary.keys(),key = lambda word:(-dictionary[word],word))
        return result[:k]
             