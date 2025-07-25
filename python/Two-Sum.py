# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index1 == index2:
                  continue  
                elif nums[index1] + nums[index2] == target:
                    return [index1, index2]

solution = Solution()

result = solution.twoSum([1,2,3], 5)

print(result)