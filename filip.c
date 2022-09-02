#	Filip
#https://open.kattis.com/problems/filip

#include<stdio.h>
int main(){
int A,B,rev1=0,rev2=0,rem;
scanf("%d",&A);
scanf("%d",&B);
while(A!=0)
{
 rem=A%10;
 rev1=(rev1*10)+rem;
 A=A/10;
}


while(B!=0)
{
    rem=B%10;
    rev2=(rev2*10)+rem;
    B=B/10;

}
if(rev1>rev2)
{
    printf("%d",rev1);
}
else if(rev1<rev2)
{
    printf("%d",rev2);
}
return 0;
}
