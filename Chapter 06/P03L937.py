logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero", "let2 art can", "let7 art can"]

import string

let = []
dig = []

for log in logs:
  if log.split(' ')[1][0] in string.ascii_lowercase:
    let.append((log.split(' ')[0], ' '.join(log.split(' ')[1:])))
  else:
    dig.append(log)

let.sort(key = lambda x : (x[1], x[0])) 
#sort() sorts the list of tuples in this way : it first sorts according to 1st element, and sorts to 2nd when tied

print( [ident + ' ' + content for ident, content in let] + dig )