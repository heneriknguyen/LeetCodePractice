
#LeetCode 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for letter in s:
            if letter not in anagram:
                anagram[letter] = 1
            else:
                anagram[letter] += 1
            
        for letter in t:
            if letter not in anagram:
                return False
            else:
                anagram[letter] -= 1
                
        for key, value in anagram.items():
            if value != 0:
                return False
            
        return True
    
            