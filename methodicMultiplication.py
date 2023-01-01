#Methodic Multiplication
#https://open.kattis.com/problems/methodicmultiplication

s1 = input().count("S")
s2 = input().count("S")
s = s1 * s2
s = "S(" * s + "0" + ")" * s
print(s)
