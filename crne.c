#Crne
#https://open.kattis.com/problems/crne

#include <stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    unsigned long long h = (unsigned long long)(n>>1);
    printf("%llu\n", n&1 ? (h+1)*(h+2) : (h+1)*(h+1));
    return 0;
}
