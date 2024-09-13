class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        rows = len(board)
        cols = len(board[0])
        
        # Check if word has more characters than board
        if rows*cols < len(word):
            return False

        # Define a helper function to check if a word exists starting at a given position
        def check(i, j, k):
            # Check if the index is out of bounds or the character does not match
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            
            # If we have reached the end of the word, return True
            if k == len(word) - 1:
                return True
            
            # Mark the current position as visited by replacing it with a space character
            temp = board[i][j]
            board[i][j] = ' '
            
            # Check if the rest of the word exists in any of the adjacent positions
            found = check(i-1, j, k+1) or check(i+1, j, k+1) or check(i, j-1, k+1) or check(i, j+1, k+1)
            
            # Backtrack: Restore the original character at the current position
            board[i][j] = temp
            
            # Return the result of the search
            return found
        
        # Check each starting point for the full string using DFS, return true if found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, 0):
                    return True
        # Otherwise have checked each position and none of them will spell our word
        return False