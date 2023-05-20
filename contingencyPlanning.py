#	Contingency Planning
#https://open.kattis.com/problems/contingencyplanning

n= int(input())
m=1
if n > 11:
    print('JUST RUN!!')
else:
    for i in range(2, n+1):
        m =m*i
    c = m
    for i in range(1, n):
        m =m// i
        c =c+ m
    print(c)
