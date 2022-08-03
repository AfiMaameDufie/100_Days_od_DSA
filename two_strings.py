'''
    Two Sum

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
    

    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
            
# Time : O(n**2)
# Space : O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         Create empty hashmap
        hashmap = {}
#     Create for loop to go through nums for each element 
        for i in range(len(nums)):
#         Check if the current elements complement is available and return the element and the complement 
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


# Complexity Analysis

# Time complexity: O(n)O(n). We traverse the list containing nn elements only once. Each lookup in the table costs only O(1)O(1) time.

# Space complexity: O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.