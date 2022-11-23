#	Avion
#https://open.kattis.com/problems/avion

b=list()
for i in range(5):
    bi=input()
    if "FBI" in bi:
        b.append(str(i+1))
if b:
    print(" ".join(b))
else:
    print("HE GOT AWAY!")
