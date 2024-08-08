
#include <stdio.h>
int main() {
    int number, digit;
    int frequency[10] = {0}; 
    printf("Enter a number: ");
    scanf("%d", &number);
    if (number < 0) {
        number = -number;
    }
    while (number != 0) {
        digit = number % 10;    
        frequency[digit]++; 
        number /= 10;           
    }
    printf("Digit frequencies:\n");
    for (int i = 0; i < 10; ++i) {
        if (frequency[i] > 0) {
            printf("Digit %d: %d\n", i, frequency[i]);
        }
    }
    return 0;
}
