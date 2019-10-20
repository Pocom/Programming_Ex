class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        run = True
        for item in s:
            # count = count + 1 if item != ' ' else 0
            if item != ' ':
                if not run:
                    run = True
                    count = 1
                else:
                    count += 1
            elif item == ' ' and run:
                run = False
        return count


t = Solution()
print(t.lengthOfLastWord('ajfak  akf af la knalkf l'))