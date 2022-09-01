#	Echo Echo Echo
#https://open.kattis.com/problems/echoechoecho

#include<stdio.h>
int main(){
    int i;
    char name[15];
gets(name);

for(i=0;i<3;i++){
    printf("%s\t",name);
}


return 0;
