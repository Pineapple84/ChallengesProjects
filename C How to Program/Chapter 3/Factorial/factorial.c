/* Find factorial of number input */

#include <stdio.h>

int main()
{
    int i;
    int number;
    int fact = 1;
    
    printf("Enter number: ");
    scanf("%d", &number);
    
    for (i = 1; i <= number; i++) {
      fact = fact * i;
    }
    
    printf("%d", fact);
    
    return 0;
}
