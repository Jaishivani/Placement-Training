#include <stdio.h>
void convertToUppercase(char str[]) {
    int i = 0;
    while (str[i] != '\0') {  
        if (str[i] >= 'a' && str[i] <= 'z') {  
            str[i] = str[i] - 32;  
        }
       i++;
    }
}
int main() {
    char str[] = "artificial intelligence and machine learning";  
    convertToUppercase(str);
    printf("Uppercase String: %s", str);
}
