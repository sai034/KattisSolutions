#Mumble Rap
#https://open.kattis.com/problems/mumblerap

import re
p = [input(), input()][1]
print(max(map(int, re.findall('\d+', p))))
