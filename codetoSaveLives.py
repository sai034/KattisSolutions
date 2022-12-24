#	Code to Save Lives
#https://open.kattis.com/problems/codetosavelives

n=int(input())
for i in range(n):
    m= int(input().replace(" ", ""))
    k= int(input().replace(" ", ""))
    s = m+k
    sum=" ".join(list(str(s)))
    print(sum)
