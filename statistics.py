#	Statistics
#https://open.kattis.com/problems/statistics

case=0
while True:
    case=case+1
    try:
        a,*b=list(map(int,input().split()))
    except EOFError:
        break
    minimum=min(b)
    maximum=max(b)
    range=maximum-minimum
    print("Case {}: {} {} {}".format(case,minimum,maximum,range))
