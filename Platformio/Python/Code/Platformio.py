import numpy as np
import matplotlib.pyplot as plt

A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

Qa = A & (~B & 1)
Qb = A & (~B & 1)
Qc = A & (~B & 1)
Qd = (~A & 1) | B

print("A B | Qa Qb Qc Qd")

for i in range(4):
    print(A[i],B[i],"|",Qa[i],Qb[i],Qc[i],Qd[i])

plt.plot(range(4),Qa,marker='o',label="Qa")
plt.plot(range(4),Qd,marker='o',label="Qd")

plt.xlabel("Input Combination")
plt.ylabel("Output")
plt.title("Circuit Output Comparison")
plt.legend()
plt.grid()

plt.savefig("graph2.jpg")
plt.show()