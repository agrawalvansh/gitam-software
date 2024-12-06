# quadratic.py
import matplotlib.pyplot as plt
import input  # Import the data from input.py

# Read coefficients and x_values from input.py
a = input.a
b = input.b
c = input.c
x = input.x

# Calculate y values for each x
y = [a * (x**2) + b * x + c for x in x]

# Plot x vs y
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', color='b', label='y = ax² + bx + c')
plt.title('Quadratic Function: x vs y', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.show()