class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def checker(x,y):
            return 0 <= x < len(image) and 0 <= y < len(image[0])
        visited = set()
        key = image[sr][sc]

        def dfs(i, j):
            if not checker(i, j) or (i,j) in visited:
                return
            if image[i][j] == key:
                visited.add((i,j))
                image[i][j] = color
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
        dfs(sr,sc)
        return image
