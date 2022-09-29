#	Cpr-nummer
#https://open.kattis.com/problems/cprnummer

i = str(input())
d1=i[0]
d2=i[1]
m1=i[2]
m2=i[3]
y1=i[4]
y2=i[5]
da=i[6]
k1=i[7]
k2=i[8]
k3=i[9]
k4=i[10]
D=(int(d1)*4)+(int(d2)*3)+(int(m1)*2)+(int(m2)*7)+(int(y1)*6)+(int(y2)*5)+(int(k1)*4)+(int(k2)*3)+(int(k3)*2)+(int(k4)*1)
if D%11==0:
    print('1')
elif D!=0:
    print('0')
