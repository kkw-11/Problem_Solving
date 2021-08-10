class TrieNode():
    def __init__(self, key, data=None):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

    def starts_with(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


t = Trie()
t.insert("apple")

print(t.starts_with("a"))