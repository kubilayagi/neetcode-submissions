class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            cord = ord(c) - ord('a')
            if not node.children[cord]:
                node.children[cord] = TrieNode()
            node = node.children[cord]
        node.wordEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for i, c in enumerate(word):
            cord = ord(c) - ord('a')
            if not node.children[cord]:
                return False
            node = node.children[cord]
        return node.wordEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i, c in enumerate(prefix):
            cord = ord(c) - ord('a')
            if not node.children[cord]:
                return False
            node = node.children[cord]
        return True
        