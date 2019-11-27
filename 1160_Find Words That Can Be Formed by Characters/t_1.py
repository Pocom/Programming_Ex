class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans = 0
        for word in words:
            # for s in word:
            for s in set(word):
                if word.count(s) > chars.count(s):
                    break
            else:
                ans += len(word)

        return ans
