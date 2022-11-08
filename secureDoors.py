#	Secure Doors
#https://open.kattis.com/problems/securedoors

n=int(input())
p=set()
for i in range(n):
    s=str(input())
    if s[0]=='e' and s[1]=='n':
        if s[6::] in p:
            print(s[6::],"entered (ANOMALY)")
        else:
            print(s[6::],"entered")
        p.add(s[6::])

    elif s[0]=='e' and s[1]=='x':
       if s[5::] in p:
           print(s[5::],"exited")
           p.remove(s[5::])
       else:
           print(s[5::],"exited (ANOMALY)")
