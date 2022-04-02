class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        answer = []
        
        if ln < 3:
            return []
        
        nums.sort()
        
        for i in range(0, ln - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ln - 1
            while j < k:
                candidate = [nums[i], nums[j], nums[k]]
                summed = sum(candidate)
                if summed > 0:
                    k -= 1
                elif summed < 0:
                    j += 1
                else:
                    answer.append(candidate)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    
        return answer


nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(Solution, nums))