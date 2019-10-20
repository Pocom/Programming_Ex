class Solution:
    def longestWord(self, words) -> str:
        if not words: return ''
        list_word = []
        MAX = len(words[0])
        for word in words:
            if len(word) == 1:
                list_word.append(word)
            if len(word) > MAX:
                MAX = len(word)

        n = 2
        while n <= MAX:
            for word in words:
                if len(word) == n:
                    if word[:-1] in list_word:
                        list_word.append(word)
            n += 1

        MAX = list_word[-1]
        for word in list_word:
            if len(word) >= len(MAX) and word < MAX:
                MAX = word

        return MAX


t = Solution()
s = t.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print(s)
