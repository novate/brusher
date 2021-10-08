class Trie:

    def __init__(self):
        # character:next_tree
        self.children = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.children['*'] = None
        else:
            ch = word[0]
            if ch not in self.children:
                self.children[ch] = Trie()
            self.children[ch].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return '*' in self.children
        ch = word[0]
        if ch not in self.children:
            return False
        return self.children[ch].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        ch = prefix[0]
        if ch not in self.children:
            return False
        return self.children[ch].startsWith(prefix[1:])
