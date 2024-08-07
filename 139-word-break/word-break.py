class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		wordsSet = set(wordDict)
		temp = [True] + [False] * len(s)

		for i in range(len(s)):
			if temp[i]:
				for j in range(i+1, len(s)+1):
					if s[i:j] in wordsSet:
						temp[j] = True

		return temp[-1]