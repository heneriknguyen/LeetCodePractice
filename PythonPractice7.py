
#LeetCode 66: Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        temp = ""
        for digit in digits:
            temp = temp + str(digit)
        
        intTemp = int(temp) + 1
        temp = str(intTemp)
        for digit in temp:
            answer.append(int(digit))

        return answer