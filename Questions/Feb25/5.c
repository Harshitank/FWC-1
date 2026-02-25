#include <stdio.h>

int main() {
    int arr[100], n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    if(arr[0] == arr[n-1])
        printf("Same\n");
    else
        printf("Not Same\n");

    return 0;
}
