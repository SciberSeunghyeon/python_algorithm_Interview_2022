class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  #[] is casted to False in boolean spot
            return 0
        #preprocessing is important to improve performance

        answer = 0
        ln = len(height)
        #How can we reduce n^2 to n? being smart?

        left, right = 0, ln - 1
        left_max, right_max = 0, 0

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(
                right_max, height[right])

            if left_max <= right_max:
                answer += left_max - height[left]  #"Processing" one cell!
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1
        #Why one cell per loop, and one step per loop?

        return answer