#	Digit Product
#https://open.kattis.com/problems/sifferprodukt

x=input()
while len(x)>1:
    y=1
    for i in x:
        if i!='0':
            y=y*int(i)
        x=str(y)
print(x)
