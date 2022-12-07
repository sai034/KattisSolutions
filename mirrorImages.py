#	Mirror Images
#https://open.kattis.com/problems/mirror

n=int(input())
for i in range(1,n+1):
    m,l=map(int,input().split())
    rows=[]
    for j in range(1,m+1):
        k=str(input())
        row=k[::-1]
        rows.append(row)
    rows = rows[::-1]
    print("Test {}".format(i))
    for row in rows:
        print("".join(row))
