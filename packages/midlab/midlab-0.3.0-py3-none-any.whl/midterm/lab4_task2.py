class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

def find_words(board, dictionary):
    def dfs(i, j, node, path, visited):
        if node.is_end:
            found_words.add(path)
        
        for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                char = board[ni][nj]
                if char in node.children:
                    visited.add((ni, nj))
                    dfs(ni, nj, node.children[char], path + char, visited)
                    visited.remove((ni, nj))

    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    m, n = len(board), len(board[0])
    found_words = set()
    
    for i in range(m):
        for j in range(n):
            char = board[i][j]
            if char in trie.root.children:
                dfs(i, j, trie.root.children[char], char, {(i, j)})
    
    return found_words

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]
dictionary = {"START", "NOTE", "SAND", "STONED"}

result = find_words(board, dictionary)
print("Found words:", result)