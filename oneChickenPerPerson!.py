#	One Chicken Per Person!
#https://open.kattis.com/problems/onechicken

p,c=map(int,input().split())
pie=c-p
if pie==1:
    print("Dr. Chaz will have",pie,"piece of chicken left over!")
elif pie>0:
    print("Dr. Chaz will have",pie,"pieces of chicken left over!")
elif pie==-1:
    print("Dr. Chaz needs",(-pie) ,"more piece of chicken!")
elif pie<0:
    print("Dr. Chaz needs",(-pie) ,"more pieces of chicken!")
