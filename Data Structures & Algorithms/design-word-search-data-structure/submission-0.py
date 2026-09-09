class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        for c in word:
            if c not in self.children:
                self.children[c] = WordDictionary()
            self = self.children[c]
        self.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.word
            if word[i] == ".":
                for l in root.children.values():
                    if dfs(i + 1, l): 
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(i + 1, root.children[word[i]])
        return dfs(0, self)