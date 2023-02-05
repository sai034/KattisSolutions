#	Class Field Trip
#https://open.kattis.com/problems/classfieldtrip

def remove(q):
    return q.replace(" ", "")
def listToString(st):
    str1 = " "
    return (str1.join(st))
s1=str(input())
s2=str(input())
s=s1+s2
st=sorted(s)
q=listToString(st)
print(remove(q))
