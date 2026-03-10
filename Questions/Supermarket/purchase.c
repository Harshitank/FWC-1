#include <stdio.h>
#include "stock.h"

#define MAXSTOCK 100

void purchase(int qty)
{
    if(getstock() + qty <= MAXSTOCK)
    {
        addstock(qty);
        printf("Purchase successful!\n");
    }
    else
    {
        printf("Stock room full! Cannot purchase.\n");
    }
}
