class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    # try every child, recurse on the rest of the word
                    return any(dfs(j + 1, child) for child in node.children.values())
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.endOfWord

        return dfs(0, self.root)  