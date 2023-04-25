#	International Dates
#https://open.kattis.com/problems/internationaldates

s1,s2,s3=map(int,input().split('/'))
if s1>12:
    print("EU")
elif s2>12:
    print("US")
else:
    print("either")
