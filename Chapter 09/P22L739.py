# from ~ import ~

param_1 =
# Started at Tue Apr 12 23:13:42 KST 2022
# Suspended at Wed Apr 13 00:00:26 KST 2022 47 min elapsed.
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
        print(temperatures, end=' <-temp_stack\n')
        delta_stack = []
        for i in range(len(temperatures) - 1):
            delta_stack.append(temperatures[i + 1] - temperatures[i])

        print(delta_stack, end = ' <-delta_stack\n')

        answer_stack = []

        for i in range(len(temperatures) - 2):
            reached_final = False
            sum_delta = delta_stack[i]
            elapsed_days = 1
            while not sum_delta > 0:
                i += 1
                if i == len(delta_stack):
                    answer_stack.append(0)
                    reached_final = True
                    break
                sum_delta += delta_stack[i]
                elapsed_days += 1
            if reached_final: break
            answer_stack.append(elapsed_days)
            # if index reached to final only to find warm day impossible.. we already appended 0, then not append

        if delta_stack[-1] > 0:  # Process temperatures[-2]
            answer_stack.append(1)
        else:
            answer_stack.append(0)

        answer_stack.append(0)  # Process temperatures[-1]

        return answer_stack


print(Solution.function(param_1))
