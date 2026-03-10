#include <stdio.h>
#include "stock.h"

int stock = 50;

void addstock(int qty)
{
    stock = stock + qty;
}

void deletestock(int qty)
{
    stock = stock - qty;
}

int getstock()
{
    return stock;
}
