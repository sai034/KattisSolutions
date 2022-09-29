#Heart Rate
#https://open.kattis.com/problems/heartrate

n=int(input())
for i in range(0,n):
    b,p=input().split()
    bpm=60*int(b)/float(p)
    miabpm=bpm-60/float(p)
    maabpm=bpm+60/float(p)
    print(miabpm,bpm,maabpm)
