class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        shift = s
        for _ in range(len(s)):
            shift = shift[1:]+shift[0]
            if shift == goal:
                return True
        return False