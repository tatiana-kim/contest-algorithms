#include <stdio.h>
#include <stdlib.h>

// TODO: change the way to solve this task
// reason: its not good to use the float numbers

int main()
{
    long long a, b, c;
    FILE* in_file = fopen("E/input.txt", "r");

    if (!in_file )
    {  
        printf("oops, file can't be read\n"); 
        exit(-1); 
    } 

    fscanf(in_file, "%lld %lld %lld", &a, &b, &c);

    long long m;
    long long sum = 2 * a + 3 * b + 4 * c;
    long long cnt = a + b + c;
    long long l = 0, r = cnt + 1;
    long double five = 5;
    // binary search
    while (l < r)
    {
        m = (l + r) / 2;
        if ((sum + five * m) / (cnt + m) < 3.5)
            l = m + 1;
        else
            r = m;
    }
    printf("%lld\n", l);
}
