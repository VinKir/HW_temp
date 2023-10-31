import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 4, 100)
y = [math.log(i) if i>0 else 0 + math.cos(i) for i in x]

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
