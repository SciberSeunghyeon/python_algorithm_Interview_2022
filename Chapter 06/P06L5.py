class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:  
            #two indices left and right are the elements to be checked, hence not checked yet.
            #start checking from {left}, {right} indices.
            while left >= 0 and right <= ln - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]  #returns longest possible palindrome, expanded from initial s[left + 1:right]
        
        ln = len(s)
        
        if ln <= 1 or s == s[::-1]:
            return s
        
        answer = ''
        for i in range(ln - 1):
            answer = max(answer, expand(i, i+1), expand(i, i+2), key = len)
            
        return answer

print(Solution.longestPalindrome(Solution, "dfpabapd"))