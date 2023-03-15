#	Blueberry Waffle
#https://open.kattis.com/problems/blueberrywaffle

r, f = map(int, input().split())
p=[round(f/r)%2]
if p==[0]:
    print("up")
else:
    print("down")
