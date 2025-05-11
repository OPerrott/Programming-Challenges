#include <stdio.h>


void swap(int *a, int *b);



int main()
{
    int a = 1;
    int b = 2;

    printf("A is %d, B is %d\n", a, b);
    swap(&a, &b);
    printf("A is %d, B is %d\n", a, b);
}


void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}