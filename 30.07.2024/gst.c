#include <stdio.h>

int main() {
    int a,b,c;
    printf("Enter net price and original cost : ");
    scanf("%d%d",&a,&b);
    c=((a-b)*100)/b;
    printf("%d%%\n",c);
}
