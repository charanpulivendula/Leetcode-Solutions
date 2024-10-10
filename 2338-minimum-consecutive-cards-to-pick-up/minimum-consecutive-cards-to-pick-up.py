class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visited = set()
        mini = float('inf')
        i = 0
        j = 0
        while(i<len(cards) and j<len(cards)):
            if cards[j] in visited:
                while(visited and cards[j] in visited):
                    visited.remove(cards[i])
                    i+=1
                visited.add(cards[j])
                j+=1
                mini = min(mini,len(visited)+1)

            else:
                visited.add(cards[j])
                j+=1

        return mini if mini!=float('inf') else -1