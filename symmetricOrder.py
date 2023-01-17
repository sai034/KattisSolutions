#	Symmetric Order
#https://open.kattis.com/problems/symmetricorder

n = 1
while(True):
    names = int(input())
    if names == 0:
        break
    s = []
    for i in range(names):
        if i%2 == 0:
            s.insert(int(i/2),input())
        else:
            s.insert(len(s)-int((i/2)), input())
    print("SET", n)
    n+=1
    for j in s:
        print(j)
