class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        if not words: return []

        def helper(w):
            w = w.lower()

            l1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
            l2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
            l3 = {"z", "x", "c", "v", "b", "n", "m"}
            l = []

            if w[0] in l1:
                l = l1
            elif w[0] in l2:
                l = l2
            elif w[0] in l3:
                l = l3

            for s in w:
                if s not in l:
                    return False

            return True

        ret = []
        for word in words:
            if helper(word):
                ret.append(word)

        return ret
