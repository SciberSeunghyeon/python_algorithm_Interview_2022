class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        used = {}
        start = 0
        
        for now, char in enumerate(s):
            print(now, char)
        
            if char in used: start = max(used[char] + 1, start)
            used[char] = now
                
            max_length = max(max_length, now - start + 1)
            
        print(max_length)