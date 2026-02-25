#include <stdio.h>

int main() {
    char str[100];
    int n, i;

    printf("Enter string: ");
    scanf("%s", str);

    printf("Enter number of characters to remove: ");
    scanf("%d", &n);

    for(i = n; str[i] != '\0'; i++) {
        printf("%c", str[i]);
    }

    return 0;
}
