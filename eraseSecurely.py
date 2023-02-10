#	Erase Securely
#https://open.kattis.com/problems/erase

n = int(input())
b = input()
a = input()
if n % 2 == 0:
    ab = b
else:
    ab = b
    ab = ab.replace("1", "2")
    ab = ab.replace("0", "1")
    ab = ab.replace("2", "0")
if a == ab:
    print("Deletion succeeded")
else:
    print("Deletion failed")
