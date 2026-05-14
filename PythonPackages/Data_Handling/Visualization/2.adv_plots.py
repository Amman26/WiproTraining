import matplotlib.pyplot as plt
import numpy as np


# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# First subplot
ax1.plot(x, y1, color='blue', label='Sine')
ax1.set_title('Sine Function')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()

# Second subplot
ax2.plot(x, y2, color='red', label='Cosine')
ax2.set_title('Cosine Function')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# Show the plots
plt.tight_layout()
plt.show()