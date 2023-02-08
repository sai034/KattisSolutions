#Proofs
#https://open.kattis.com/problems/proofs

def c(n):
    k = set()
    for i in range(n):
        l = input()
        if l[0] == '-':
            k.add(l[3:])
        else:
            p, q = l.split(' -> ')
            if all(j in k for j in p.split()):
                k.add(q)
            else:
                return i+1
    return 'correct'
print(c(int(input())))
