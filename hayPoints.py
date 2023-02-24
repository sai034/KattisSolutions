#Hay Points
#https://open.kattis.com/problems/haypoints

n1, n2 = list(map(int, input().split()))
wte= {}
for i in range(n1):
    d = input().split()
    w = d[0]
    e = int(d[1])
    wte[w] = e
for j in range(n2):
    job = 0
    while True:
        l = input()
        if l == ".":
            break
        lets = l.split()
        for let in lets:
            if let in wte:
                job += wte[let]
    print(job)
