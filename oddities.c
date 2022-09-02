#	Oddities
#https://open.kattis.com/problems/oddities

#include<stdio.h>
int main(){
int n,i,temp;
scanf("%d",&n);
for(i=0;i<n;i++){
scanf("%d",&temp);
if(temp%2==0)
    printf("%d is even\n",temp);
else
    printf("%d is odd\n",temp);
}
return 0;
}
