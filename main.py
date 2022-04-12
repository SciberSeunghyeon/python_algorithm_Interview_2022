# from ~ import ~

param_1 = [73,74,75,71,69,72,76,73]
# Started at Tue Apr 12 23:13:42 KST 2022
# Finished at
"""
My Idea :
"""
"""
What I Learned :
"""


class Solution:
    @classmethod
    def function(cls, temperatures):  # Construct delta_stack
        answer_stack = []
        for i in range(len(temperatures) - 1):
            for j in range(i, len(temperatures)):
                success = False
                if temperatures[i] < temperatures[j]:
                    answer_stack.append(j - i + 1)
                    success = True
                    break
            if not success: answer_stack.append(0)
        answer_stack.append(0)
        return answer_stack


print(Solution.function(param_1))
