#	Östgötska
#https://open.kattis.com/problems/ostgotska

w = input()
t = 0
l = w.split(' ')
for i in range(len(l)):
    if('ae' in l[i]):
        t += 1
if(t/len(l)>=40/100):
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
