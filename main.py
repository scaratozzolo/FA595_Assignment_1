import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.title("Graph of Sine and Cosine")
plt.xlabel("Radians")
plt.show()