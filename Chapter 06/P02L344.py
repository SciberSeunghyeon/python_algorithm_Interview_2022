#Problem 02 Leetcode 344
s = ["H","a","n","n","a","h"]

ln = len(s)
for i in range(ln // 2):
    s[i], s[ln-1 - i] = s[ln-1 - i], s[i]

print(s)