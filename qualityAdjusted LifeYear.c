#	Quality-Adjusted Life-Year
#https://open.kattis.com/problems/qaly

#include<stdio.h>
int main(){
 float sum=0;
float N,q,y,i,n;

scanf("%f",&N);
for(i=0;i<N;i++){
scanf("%f %f",&q,&y);
n=q*y;
    sum=sum+n;
}
printf("%.3f",sum);
return 0;
}
