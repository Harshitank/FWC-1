#include <stdio.h>
#include "stock.h"

void sell(int qty)
{
    if(getstock() >= qty)
    {
        deletestock(qty);
        printf("Sale successful!\n");
    }
    else
    {
        printf("Not enough stock to sell!\n");
    }
}
