#	Billiard
#https://open.kattis.com/problems/billiard

#include <stdio.h>
#include <math.h>
#define PI 3.1415926535897932384626433832795028841971693993751
int main()
{
    int a,b,s,m,n;
    while(1)
    {
        scanf("%d %d %d %d %d",&a,&b,&s,&m,&n);
        if (a==0 && b==0 && s==0 && m==0 && n==0) 
        break;
        double X = a * m;
        double Y = b * n;
        double total = sqrt(X * X + Y * Y);
        double v = total / s;
        double a = 180.0 * acos(X / total) / PI;
        printf("%.2f %.2f\n", a, v);
    }
    return 0;
}
