# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        positive = list(filter(lambda x: x>0,nums))
        negative = list(filter(lambda x: x<0,nums))
        min_p = abs(0-min(positive))
        max_n = abs(0-max(negative))
        return min(min_p,max_n)
        
