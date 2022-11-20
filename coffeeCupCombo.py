#Coffee Cup Combo
#https://open.kattis.com/problems/coffeecupcombo

n=int(input())
l=input()
sum=0
for i in range(n):
    if "1" in l[max(0,i-2):i+1]:
        sum=sum+1
    else:
        continue
print(sum)
