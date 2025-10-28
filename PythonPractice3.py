
#LeetCode 58: Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for word in s:
            length = len(word)
        return length