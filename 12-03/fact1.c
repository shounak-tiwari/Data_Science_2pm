#include<stdio.h>
int factorial(int num){
    int fact = 1;
    for (int i = 1; i <=num; i++)
    {
        fact = fact*i;
    }
    return fact;
}
int main(){
    int accp = factorial(10);
    printf("The factorial of number is : %d",accp);
    printf("The factorial of number is : %d",factorial(5));
}