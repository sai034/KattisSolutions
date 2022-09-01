#	N-sum
#https://open.kattis.com/problems/nsum
n=int(input())
sum = 0
for number in input().split():
    sum += int(number)
print(sum)
