# from ~ import ~

param_1 = [73,74,75,71,69,72,76,73]
# Started at Tue Apr 12 23:13:42 KST 2022
# Suspended at Wed Apr 13 00:00:26 KST 2022 47 min elapsed.
# Finished at Wed Apr 13 01:00:10
"""
My Idea : for each index, search to the end till warm point(index) appears.
"""
"""
What I Learned :
I. Initializing. 
We can initilize answer as [0] * length(T), so that we don't have to push 0 if answer doesn't appear.
take this approach as... The *DEFAULT Outcome* is 0(impossible), and we change it to answer(date diff) only if we found answer.
I think I'd better memorize this approach and code snippet //answer = [0] * len(T)//.

II. Usage of stack.
while stack and T[i] > T[stack[-1]]:
    day = stack.pop()
    answer[day] = i - day
stack.append(i)

var i is current index, and we check for processible days from stack.
and for each day, we update the answer as many as possible at current index.
checking stack emptiness prevents index error by shortcircuiting.

I'd better memorize...
while stack and T[i] > T[stack[-1]]:
and
(stack check)
(push current val to stack)
order.
"""

""" #literally, delicious spagetti code
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
 """
def old_sol(T):
    answer = []
    for i in range(len(T) - 1):
        found = False
        for j in range(i+1, len(T)):
            if T[i] < T[j]:
                answer[i] = j - i
                break
        if not found: answer.append(0)
    answer.append(0)    
    return answer

def old_sol_withpointI(T):
    answer = [0] = len(T)
    for i in range(len(T) - 1):
        for j in range(i+1, len(T)):
            if T[i] < T[j]:
                answer[i] = j - i
                break
    return answer

def sol(T):
    answer = [0] * len(T)
    stack = []

    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]: 
            #Processing all days(indices) able at this point(i).
            #checking for stack prevents IndexOutOfRange by shortcircuiting.
            pop = stack.pop()
            answer[pop] = i - pop
        stack.append(i)
    return answer
             


print(sol(param_1))
