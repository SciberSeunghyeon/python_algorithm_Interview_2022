class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # My Solution
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

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Easier & intiuitive solution
        # Thanks to https://www.youtube.com/watch?v=wiGpQwVHdE0
        max_length = 0
        used = set()
        l = 0
        
        for r, char in enumerate(s):
            while char in used:
                used.remove(s[l])
                l += 1
            used.add(char)
            max_length = max(max_length, r-l+1)
        
        return max_length
