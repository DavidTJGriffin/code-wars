# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = set(nums)
        for i in unique_nums:
            nums_counter = nums.count(i)
            if nums_counter > n/2:
                return i

solution = Solution()

result = solution.majorityElement([2,2,1,1,1,2,2])

print(result)