#include <stdio.h>

int main() {
    int i, previous = 0;

    for(i = 1; i <= 5; i++) {
        printf("Current Number: %d\n", i);
        printf("Sum: %d\n\n", i + previous);
        previous = i;
    }

    return 0;
}
