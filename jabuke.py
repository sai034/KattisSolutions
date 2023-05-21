#Jabuke
#https://open.kattis.com/problems/jabuke

def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
d = area(x1, y1, x2, y2, x3, y3)
print("%.1lf" % d)
t = int(input())
c = 0
for i in range(t):
    x, y = map(int, input().split())
    if area(x1, y1, x2, y2, x, y) + area(x1, y1, x3, y3, x, y) + area(x3, y3, x2, y2, x, y) == d:
        c =c+ 1
print(c)
