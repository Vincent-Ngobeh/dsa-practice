"""
Two Sum Problem
Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Optimal solution using a hash map.
    Time Complexity: O(n)
    Space Complexity: O(n)
    Args:

        nums: List of integers

        target: Target sum to find
    Returns:
        List containing indices of the two numbers that add up to target
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i    
    return []  # No solution found