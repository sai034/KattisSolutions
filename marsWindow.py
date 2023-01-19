#	Mars Window
#https://open.kattis.com/problems/marswindow

n=int(input())
p=((n-2017)*12-4)%26
if p<12:
    print("yes")
else:
    print("no")
