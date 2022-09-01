#	Honour Thy (Apaxian) Parent
#https://open.kattis.com/problems/apaxianparent
i = str(input())
s = i.split()
Y = s[0]
P = s[1]
if Y[-1]=='e':
    print(Y+'x'+P)

elif 'ex' in Y:
    print(Y+P)

elif Y.endswith('a'):
     y=Y[:-1].rstrip()
     print(y+'ex'+P)

elif Y.endswith('i'):
    s=Y[:-1].rstrip()
    print(s+'ex'+P)

elif Y.endswith('o'):
    b=Y[:-1].rstrip()
    print(b+'ex'+P)

elif Y.endswith('u'):
    c=Y[:-1].rstrip()
    print(c+'ex'+P)

else:
    print(Y+'ex'+P)
