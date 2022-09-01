	#Help a PhD candidate out!
  #https://open.kattis.com/problems/helpaphd
  n=int(input())
for i in range(0,n):
    s=input()
    if s == "P=NP":
        print("skipped")
    else:
        num1,num2=s.split('+')
        Num1=int(num1)
        Num2=int(num2)
        print(Num1+Num2)
