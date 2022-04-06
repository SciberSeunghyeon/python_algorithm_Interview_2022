# from ~ import ~

# param_1 =

# Started at
# Finished at
"""
My Idea :
"""
"""
What I Learned : 2 try
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True  # preprocessing

        if nums[0] <= nums[-1]:  # assume monotone increase #not 2nd element, LAST element!
            curr = nums[0]
            for i in range(1, len(nums)):
                if curr > nums[i]: return False
                curr = nums[i]
            else:
                return True

        else:  # monotone decrease
            curr = nums[0]
            for i in range(1, len(nums)):
                if curr < nums[i]: return False
                curr = nums[i]
            else:
                return True