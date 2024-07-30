#include <stdio.h>
void recursive_strcpy(char *dest, const char *src) {
    if (*src == '\0') {
        *dest = '\0';
    } else {
        *dest = *src;
        recursive_strcpy(dest + 1, src + 1);
    }
}
int main() {
    char str1[100], str2[100];
    printf("Enter first string: ");
    scanf("%99s", str1);
    printf("Enter second string: ");
    scanf("%99s", str2);
    recursive_strcpy(str2, str1);
    printf("After copy\nFirst string: %s\nSecond string: %s\n", str1, str2);
    return 0;
}
