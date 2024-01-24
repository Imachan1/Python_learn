import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()

_______________________________________________________________________________________

def f(x):
    return 3 + 2*x - x**2
x_values = np.linspace(1, 3, 100)
y_values = f(x_values)

plt.plot(x_values, y_values, label='$f(x) = 3 + 2x - x^2$')
plt.fill_between(x_values, y_values, color='skyblue', alpha=0.4, label='Area under the curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
