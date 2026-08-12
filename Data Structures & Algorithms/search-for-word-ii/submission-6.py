class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Using a Trie Nodes + backtrack
        root = TrieNode()
        # We add all words into a trie node
        for w in words:
            root.addWord(w)
        
        ROWS,COLS = len(board), len(board[0])
        res, path = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or c < 0 or r>= ROWS or 
                c >= COLS or (r,c) in path or
                board[r][c] not in node.children): # ie The letter we are on now is not used for any of the words in words
                return
            path.add((r,c))
            node = node.children[board[r][c]] # move our pointer deeper into our trie node
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            path.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)

