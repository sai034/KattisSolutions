#	Hissing Microphone
#https://open.kattis.com/problems/hissingmicrophone

#include<stdio.h>
#include<string.h>
int main(){
char a[10000];
int i, isHiss=0;
gets(a);
for (i=0;i<strlen(a) - 1;i++)
{
    if (a[i]=='s' && a[i+1]=='s')
    {
        isHiss = 1;

    }
}

if(isHiss)
{
    printf("hiss");
}
else
{
    printf("no hiss");
}

return 0;
}
