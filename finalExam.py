#	Final Exam
#https://open.kattis.com/problems/finalexam2

n = int(input())
p = input()
c = 0
for i in range(n - 1):
    l = str(input())
    if p == l:
        c =c+ 1
    p = l
print(c)
