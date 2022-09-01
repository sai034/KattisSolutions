#	Cold-puter Science
#https://open.kattis.com/problems/cold

#include<stdio.h>
int main(){
int n,t,i,count=0;
scanf("%d",&n);
for(i=0;i<n;i++){
scanf("%d",&t);

if(t<0){
   count++;

}

}
printf("%d",count);
return 0;
}
