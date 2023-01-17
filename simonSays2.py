#	Simon Says
#https://open.kattis.com/problems/simon

n=int(input())
for i in range(n):
    s=str(input())
    if s.__contains__("simon says "):
        print(s[10::].lstrip())
    else:
        print("")
