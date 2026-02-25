#include <stdio.h>

int main() {
    int i;

    for(i = 1; i <= 50; i++) {
        if(i % 5 == 0) {
            printf("%d ", i);
        }
    }

    return 0;
}
