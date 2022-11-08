#	Stopwatch
#https://open.kattis.com/problems/stopwatch

ni=int(input())
running=True
lt=int(input())
total=0
for i in range(1,ni):
    n=input()
    N=int(n)
    if not running:
        running=True
        lt=N
    else:
        running=False
        total=total+(N-lt)
if running:
    print("still running")
else:
    print(total)
