import numpy as np
import matplotlib.pyplot as plt

A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

AND = A & B
OR  = A | B


A_not = ~A & 1

NAND = ~(A & B) & 1
XNOR = ~(A ^ B) & 1
XOR  = A ^ B

print("A B | AND OR NAND XOR XNOR")
for i in range(4):
    print(A[i], B[i], "|", AND[i], OR[i], NAND[i], XOR[i], XNOR[i])

plt.plot(range(4), AND, marker='o', label="AND")
plt.plot(range(4), OR, marker='o', label="OR")
plt.plot(range(4), NAND, marker='o', label="NAND")

plt.xlabel("Input Combination")
plt.ylabel("Output")
plt.title("Logic Gate Outputs")
plt.legend()
plt.grid()

plt.show()