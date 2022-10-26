#https://open.kattis.com/problems/tarifa

x=int(input())
n=int(input())
s=0
va=0
sa=0
for i in range(0,n):
  v=int(input())
  s=(x-v)
  va=s+va
  sa=va+x
print(sa)
