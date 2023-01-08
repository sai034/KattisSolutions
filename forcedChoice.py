#	Forced Choice
#https://open.kattis.com/problems/forcedchoice

n, s, ns = list(map(int, input().split()))
for _ in range(ns):
    n, *c = list(map(int, input().split()))
    if s in c:
        print("KEEP")
    else:
        print("REMOVE")
