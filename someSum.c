#	Some Sum
#https://open.kattis.com/problems/somesum

#include<stdio.h>
int main(){
int N;
scanf("%d",&N);
if(N%2!=0){
    printf("Either");
}
else if(N%2==0&&N%4!=0){
   printf("Odd");
}
else if(N%4==0){
printf("Even");
}
return 0;
}
