#	Triple Texting
#https://open.kattis.com/problems/tripletexting

import textwrap, collections
p = str(input())
w= textwrap.wrap(p, len(p) // 3)
print(collections.Counter(w).most_common(1)[0][0])
