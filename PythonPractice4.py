
#LeetCode 9: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) # "1221"
        reverse_x = ""
        for i in range(len(x)-1, -1, -1):
            back_letter = x[i]
            reverse_x += back_letter

        if x == reverse_x:
            return True

        return False
                    
                    