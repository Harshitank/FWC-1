; Simple NAND example for ATmega328P
; No include file used

.org 0x0000
rjmp start

; Register definitions
.equ DDRB  = 0x04
.equ PORTB = 0x05
.equ PINB  = 0x03

.equ DDRD  = 0x0A
.equ PORTD = 0x0B
.equ PIND  = 0x09

start:

    ; Set PB0 as output
    ldi r16, 0x01
    out DDRB, r16

loop:

    ; Read inputs from PD2 and PD3
    in r17, PIND

    ; Mask PD2 and PD3
    andi r17, 0b00001100

    ; If both bits high → AND = 1
    cpi r17, 0b00001100
    breq both_high

    ; Otherwise NAND = 1
    ldi r18, 0x01
    out PORTB, r18
    rjmp loop

both_high:
    ; NAND = 0
    ldi r18, 0x00
    out PORTB, r18
    rjmp loop
