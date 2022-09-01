#	Tri
#https://open.kattis.com/problems/tri

#include<stdio.h>
int main(){
int m,n,p;
scanf("%d %d %d",&m,&n,&p);
if(m+n==p){
    printf("%d+%d=%d",m,n,p);
}
else if(m-n==p){
 printf("%d-%d=%d",m,n,p);
}
else if(m*n==p){
    printf("%d*%d=%d",m,n,p);
}
else if(m/n==p){
    printf("%d/%d=%d",m,n,p);
}
else if(m==n+p){
    printf("%d=%d+%d",m,n,p);
}
else if(m==n-p){
    printf("%d=%d-%d",m,n,p);
}
else if(m==n/p){
    printf("%d=%d/%d",m,n,p);
}
else if(m==n*p){
    printf("%d=%d*%d",m,n,p);
}
return 0;
}
