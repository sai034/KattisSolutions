#Grading
#https://open.kattis.com/problems/grading

A,B,C,D,E=list(map(int,input().split()))
n=int(input())
if n>=A:
  print("A")
elif n>=B:
  print("B")
elif n>=C:
  print("C")
elif n>=D:
  print("D")
elif n>=E:
  print("E")
else:
  print("F")
