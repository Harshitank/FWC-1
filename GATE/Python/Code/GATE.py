import numpy as np
import matplotlib.pyplot as plt

def NAND(a,b):
    return 1 - (a & b)

X = np.array([0,0,1,1])
Y = np.array([0,1,0,1])

Z = []

print("X Y | Z")

for i in range(4):

    x = X[i]
    y = Y[i]

    A = NAND(x,y)
    B = NAND(x,A)
    C = NAND(y,A)
    z = NAND(B,C)

    Z.append(z)

    print(x,y,"|",z)

Z = np.array(Z)

plt.plot(range(4),Z,marker='o')
plt.xlabel("Input Combination")
plt.ylabel("Output Z")
plt.title("XOR Gate Output")
plt.grid()
plt.show()