#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    // Set PB0–PB3 (Arduino D8–D11) as OUTPUT
    DDRB |= (1<<PB0) | (1<<PB1) | (1<<PB2) | (1<<PB3);

    while(1)
    {
        for(uint8_t i = 0; i < 10; i++)
        {
            // Clear lower 4 bits
            PORTB &= 0xF0;

            // Send BCD number to 7447
            PORTB |= (i & 0x0F);

            _delay_ms(1000);
        }
    }
}
