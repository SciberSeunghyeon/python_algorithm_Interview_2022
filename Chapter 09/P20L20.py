# Started at Tue Apr  5 23:38:38 KST 2022
# Finished at Wed Apr  6 00:19:56 KST 2022
"""
My Idea : Why do we learn algorithms, SH? So we can gain insights of the problem, and learn to make up solutions.
Python List is a perfect implementation of Stack ADT
"""
"""
What I Learned : Python doesn't have switch-case syntax. it can be substituted with if-else syntax or DICTIONARY.
"""

param_1 = "]]"


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False #preproc. it can be useless w.r.t. inputs.

        stack = []
        parentheses_dict = {')':'(', '}':'{', ']':'['}

        for elem in s:
            if elem in ('(', '{', '['):
                stack.append(elem)
            else:
                if (not stack) or parentheses_dict[elem] != stack.pop(): return False
                #(No stack content to pair with element) or (stack content doesn't match with element)
                # elem = ), stack.pop() -> None or {, [ #Missed Point

        if stack:
            return False
        else:
            return True

print(Solution.isValid(Solution, param_1))