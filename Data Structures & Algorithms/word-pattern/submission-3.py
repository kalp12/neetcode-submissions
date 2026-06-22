class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(' ')
        if len(pattern) != len(word):return False
        wordTochar = {}
        charToword = {}
        for p,w in zip(pattern, word):
            if p in charToword and charToword[p] != w: return False
            if w in wordTochar and wordTochar[w] != p: return False
            charToword[p] = w
            wordTochar[w] = p

        return True