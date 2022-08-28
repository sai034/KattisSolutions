# Harshad Numbers
# https://open.kattis.com/problems/harshadnumbers

def isHarshadNumber(num):
    n=num
    rem=sum=0
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    if (num%sum==0):
        return True
    else:
        return False
def main():
    num=int(input())
    n=num
    while True:
        if(isHarshadNumber(n)):
            print(n)
            break
        else:
            n=n+1
main()
