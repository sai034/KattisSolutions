#	Number Fun
#https://open.kattis.com/problems/numberfun


#include<stdio.h>
int main(){
 int n,i=0;
 float a,b,c;
 scanf("%d",&n);
 while (i<n) {
 scanf("%f %f %f",&a,&b,&c);

 if(c==a+b||c==b+a)
  printf("Possible\n");
else if(c==a-b||c==b-a)
    printf("Possible\n");
else if(c==a*b||c==b*a)
    printf("Possible\n");
else if(c==a/b||c==b/a)
    printf("Possible\n");
else
    printf("Impossible\n");

    i++;
 }

return 0;
}
