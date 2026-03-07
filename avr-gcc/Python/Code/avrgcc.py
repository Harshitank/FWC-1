import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,1,0,0])
B = np.array([1,0,1,0])
C = np.array([0,0,0,1])

F = A & (~B & 1) & (~C & 1)

print("A B C | F")

for i in range(4):
    print(A[i], B[i], C[i], "|", F[i])

plt.plot(range(4),F,marker='o')

plt.xlabel("Option Number")
plt.ylabel("F Output")
plt.title("Output of Logic Function")
plt.grid()

plt.show()