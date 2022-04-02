class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        val = 1
        for i in range(0, len(nums), 1):
            answer.append(val)
            val *= nums[i]
            
        val = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= val
            val *= nums[i]
            
        return answer

print(Solution.productExceptSelf(Solution, [1, 2, 3, 4]))

#Hey, as you know, reversing list is expensive(O n)