class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.children = [None] * 26
        self.populated = []

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            cord = ord(c) - ord('a')
            if not node.children[cord]:
                node.children[cord] = TrieNode()
                node.populated.append(cord)
            node = node.children[cord]
        node.wordEnd = True
        

    def search(self, word: str) -> bool:
        return self.searchHelper(0, word, self.root)

    def searchHelper(self, idx: int, word: str, node: TrieNode):
        if idx >= len(word):
            return node.wordEnd
        c = word[idx]
        cords2search = [ord(c) - ord('a')]
        if c == '.':
            cords2search = node.populated
        for cord in cords2search:
            if not node.children[cord]:
                return False
            if self.searchHelper(idx + 1, word, node.children[cord]):
                return True
        return False
            
            
