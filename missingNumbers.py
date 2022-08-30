# Missing Numbers
# https://open.kattis.com/problems/missingnumbers

n=int(input())
vs=[]
for i in range(1,n+1):
   v=int(input())
   vs.append(v)
if(len(vs)==vs[-1]):
     print("Good job")
else:

    for i in range(1,vs[-1]+1):
          if i not in  vs:
              print(i)
