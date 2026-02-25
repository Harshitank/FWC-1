#include <stdio.h>
#include <string.h>

int main() {
    char str[100], sub[100];
    int i, j, count = 0;

    printf("Enter main string: ");
    scanf("%s", str);

    printf("Enter substring: ");
    scanf("%s", sub);

    int len1 = strlen(str);
    int len2 = strlen(sub);

    for(i = 0; i <= len1 - len2; i++) {
        for(j = 0; j < len2; j++) {
            if(str[i + j] != sub[j]) {
                break;
            }
        }
        if(j == len2) {
            count++;
        }
    }

    printf("Occurrences = %d", count);

    return 0;
}
