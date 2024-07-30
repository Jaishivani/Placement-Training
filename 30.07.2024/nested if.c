#include <stdio.h>

int main() {
    char marital_status, gender;
    int age;

    printf("Enter marital status (M/U), gender (M/F), and age: ");
    scanf(" %c %c %d", &marital_status, &gender, &age);

    if (marital_status == 'M' || 
        (marital_status == 'U' && ((gender == 'M' && age > 30) || (gender == 'F' && age > 25)))) {
        printf("It is Valid.\n");
    } else {
        printf("It is Not Valid.\n");
    }

    return 0;
}
