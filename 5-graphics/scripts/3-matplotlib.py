# Standard way of loading matplotlib.

# Load numpy and matplotlib manually
import numpy as np
import matplotlib.pyplot as plt

# Generate data to plot
time = np.linspace(0.0, 10.0, 100)
height = np.exp(-time/3.0)*np.sin(time*3)

# Basic plotting with title, labels and ranges 
# plt.figure()
plt.plot(time, height, 'm-^')
plt.plot(time, 0.3*np.sin(time*3), 'b-')

plt.legend(['damped', 'constant amplitude'], loc='upper right')
plt.xlabel('Time (s)')
plt.show()

