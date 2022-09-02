#	Judging Moose
#https://open.kattis.com/problems/judgingmoose

#include<stdio.h>
int main(){
int l,r,x;
scanf("%d %d",&l,&r);
if (l==r && l!=0 && r!=0){
    x=l+r;
    printf("Even %d",x);
}
else if(l>r||l<r){
    if (l>r){
      x=2*l;
     printf("Odd %d",x);
    }
    else if(l<r){
      x=2*r;
    printf("Odd %d",x);

    }
}
else {
    printf("Not a moose");
}
    return 0;
}
