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
    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle): return 0

        haystack_idx = 0
        needle_len = len(needle)

        while haystack_idx <= len(haystack) - needle_len:
            if haystack[haystack_idx:haystack_idx + needle_len] == needle: return haystack_idx
            haystack_idx += 1
            # When using while loop (on behalf of|in lieu of) for loop, Don't forget to increment loop variable by yourself

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle): return 0

        needle_len = len(needle)

        for haystack_idx in range(len(haystack) - needle_len + 1):
            if haystack[haystack_idx:haystack_idx + needle_len] == needle: return haystack_idx
        return -1