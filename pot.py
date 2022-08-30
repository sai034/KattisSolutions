# Pot
# https://open.kattis.com/problems/pot

s=int(input())
final=0
for i in range(s):
    n=int(input())
    x=(n//10)**(n%10)
    final=final+x
print(final)
