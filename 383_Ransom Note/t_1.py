class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for ran in ransomNote:
            if ran in magazine:
                magazine.pop(magazine.index(ran))
            else:
                return False
        return True
