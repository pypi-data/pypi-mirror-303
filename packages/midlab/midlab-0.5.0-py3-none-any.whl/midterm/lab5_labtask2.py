def is_valid(x, y, visited):
    return 0 <= x < 4 and 0 <= y < 4 and not visited[x][y]

def dfs(board, word, x, y, visited, current):
    if len(current) == len(word):
        return current == word
    
    if not is_valid(x, y, visited) or board[x][y] != word[len(current)]:
        return False
    
    visited[x][y] = True
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for dx, dy in directions:
        if dfs(board, word, x+dx, y+dy, visited, current + board[x][y]):
            visited[x][y] = False
            return True
    
    visited[x][y] = False
    return False

def find_word(board, word):
    visited = [[False for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            if dfs(board, word, i, j, visited, ""):
                return True
    
    return False

def boggle_solver(board, dictionary):
    valid_words = []
    
    for word in dictionary:
        if find_word(board, word):
            valid_words.append(word)
    
    return valid_words

def iterative_deepening_boggle(board, dictionary, max_length):
    all_words = []
    
    for length in range(5, max_length + 1):
        words_of_length = [word for word in dictionary if len(word) == length]
        found_words = boggle_solver(board, words_of_length)
        all_words.extend(found_words)
        print(f"Words of length {length}: {found_words}")
    
    return all_words

# Example usage
board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

dictionary = ["START", "NOTE", "SAND", "STONED"]
max_length = 8

result = iterative_deepening_boggle(board, dictionary, max_length)
print("All valid words:", result)