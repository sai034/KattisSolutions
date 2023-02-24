#	The Deal of the Day
#https://open.kattis.com/problems/thedealoftheday

def pro(d,k):
    if k==0:
        return 1
    elif len(d)<k:
        return 0
    elif len(d)==k:
        s=1
        for i in d:
            s=s*i
        return s
    return d[0]*pro(d[1:],k-1)+pro(d[1:],k)
n=list(map(int,input().split()))
m=int(input())
print(pro(n,m))
