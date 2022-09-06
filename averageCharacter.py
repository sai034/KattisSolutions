#	Average Character
#https://open.kattis.com/problems/averagecharacter

n=str(input())
sum=0
for i in n:
    o=ord(i)
    sum=sum+o
print(chr(sum//len(n)))
