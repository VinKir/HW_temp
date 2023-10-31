import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2, 2, 50)
y = [math.sin(i) * math.cos(i) for i in x]

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
