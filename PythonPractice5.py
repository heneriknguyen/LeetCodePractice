
#LeetCode 844: Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:   
        s_stack = []
        t_stack = []

        for letter in s:
            if letter != '#':
                s_stack.append(letter)
            else:
                if s_stack:
                    s_stack.pop()

        for letter in t:
            if letter != '#':
                t_stack.append(letter)
            else:
                if t_stack:
                    t_stack.pop()
        
        return s_stack == t_stack
        

