#	Eligibility
#https://open.kattis.com/problems/eligibility

n=int(input())
for i in range(n):
    N, st, dob, c = input().split()
    if int(st[:4]) >= 2010:
        print(N, "eligible")
    elif int(dob[:4]) >= 1991:
        print(N, "eligible")
    elif int(c) > 40:
        print(N, "ineligible")
    else:
        print(N, "coach petitions")
