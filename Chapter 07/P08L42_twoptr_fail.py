height = [2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
answer = 0
ln = len(height)
#This problem has to be solved in O(n)

#Let's start with processing one index, from 1 to n-2
#determine two endpoints which contains water.

#twoptr
max_val = max(height)

left = 0
left_max = 0
right = ln - 1
right_max = 0

while left < right:
    left_max = max(left_max, height[left])
    answer += left_max - height[left]
    if not left_max == max_val:
        left += 1

    right_max = max(right_max, height[right])
    answer += right_max - height[right]
    if not right_max == max_val:
        right -= 1

print(answer)
# Why infinite loop?
# max 값이 복수가 되면 무한 루프에 걸릴 수밖에 없다.
# 내가 짠 코드는 포인터가 기둥에 도달하면 거기서 포인터를 묶어버리는 구조이다.
# 기둥이 두 개라면, left와 right가 두 개의 기둥에 걸려서
# 앞으로 영원히 나아가지 못한다. 무한 루프에 걸리게 됨.
