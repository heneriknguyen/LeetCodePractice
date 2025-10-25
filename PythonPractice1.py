from typing import List

#LeetCode 217: Contains Duplicate

class Solution:
    def containDuplie(self, nums: List[int]) -> bool:
    
        # for i in range(len[nums]):
        #     for j in range(i+1, len[nums]):
        #         prevNum = nums[i]
        #         currentNum = nums[j]
        #         if prevNum == currentNum:
        #             return True
        
        # return False
    
        duplicate = {}
        for number in nums:
            if number not in duplicate:
                duplicate[number] = 1
            else:
                duplicate[number] += 1
                return True
            
            return False
            
            
            