class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        used = {}
        start = 0 # *left ptr*
        
        for now, char in enumerate(s): # now is *right ptr*
            #print(now, char)
        
            if char in used: start = max(used[char] + 1, start)
            used[char] = now
                
            max_length = max(max_length, now - start + 1)
            
        #print(max_length)
        return max_length
