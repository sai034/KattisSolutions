#Half a Cookie
#https://open.kattis.com/problems/halfacookie

#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971693993751

int main()
{
    double r, x, y;
    while(scanf("%lf %lf %lf", &r, &x, &y) == 3)
    {
        double d;
        if ((d = x * x + y * y) >= r * r) 
        printf("miss\n");
        else
        {
            d = sqrt(d);
            double h = r - d;
            double s = r * r * acos((r - h)/r) - (r - h) * sqrt(2 * r * h - h * h);
            double c = PI * r * r;
            double r = c - s;
            if (r < s) 
            printf("%.7f %.7f\n", s, r);
            else 
            printf("%.7f %.7f\n", r, s);
        }
    }
    return 0;
}
