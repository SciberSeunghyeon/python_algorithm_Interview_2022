paragraph = "a, a, a, a, b,b,b,c, c"
banned = []

import string
import collections

new_paragraph = ''
for char in paragraph:
  if char in [',', '.', '!']:
    char = ' '
  new_paragraph += char
  
str_list = new_paragraph.lower().split()
pd_list = [word for word in str_list if not word in banned]
        
print(collections.Counter(pd_list).most_common(1)[0][0])