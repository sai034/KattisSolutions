#	Honeycomb Walk
#https://open.kattis.com/problems/honey

a= [0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]
n=int(input())
for i in range(n):
    l=int(input())
    print(a[l-1])
