class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        current = self
        
        for char in word:
            if char not in current.children:
                current.children[char] = PrefixTree()
            current = current.children[char]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        current = self

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        current = self

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        
        