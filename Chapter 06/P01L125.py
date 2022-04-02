#Problem 01 Leetcode 125

import string

s = "Seunghyeon Bang"

s = s.lower()

lis = [letter for letter in s if letter in string.ascii_lowercase or letter in string.digits]
ln = len(lis)
print(lis))

for i in range(ln // 2):
  if lis[i] != lis[ln-1 - i]:
    print(False)
print(True)