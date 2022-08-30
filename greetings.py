# Greetings!
# https://open.kattis.com/problems/greetings2

num=str(input())
s=""
v=""
for i in num:
    if i=='e':
        s='e'.join(i)
        v='e'.join(num)
        v=v.replace('e',"",1)
print(v)
