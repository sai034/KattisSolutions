# Greetings!
# https://open.kattis.com/problems/greetings2

n=str(input())
s=""
v=""
for i in n:
    if i=='e':
        s='e'.join(i)
        v='e'.join(n)
        v=v.replace('e',"",1)
print(v)
