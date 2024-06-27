import matplotlib.pyplot as plt
import numpy as np

# Generate data for the normal distribution
x = np.linspace(-3, 3, 1000)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Generate random data
random_data = np.random.randn(1000)

# Create the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot the normal distribution and histogram
ax1.plot(x, y, label=r'$\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2} x^2}$', color='blue')
ax1.hist(random_data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
ax1.set_title(r'Normal Distribution and Random Data', fontsize=16)
ax1.set_xlabel(r'$x$', fontsize=14)
ax1.set_ylabel(r'$f(x)$', fontsize=14)
ax1.legend()

# Plot the scatter plot of random data
ax2.scatter(random_data, np.random.randn(1000), alpha=0.6, color='red')
ax2.set_xlabel(r'$x$', fontsize=14)
ax2.set_ylabel(r'$y$', fontsize=14)
ax2.set_title(r'Scatter Plot of Random Data', fontsize=16)

# Adjust layout and show plot
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
