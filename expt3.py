import numpy as np
import matplotlib.pyplot as plt

# Manually create data
np.random.seed(0)
# Features
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [2, 1], [3, 2], [4, 3], [5, 4], [1, 4], [2, 5], [3, 3], [4, 2]])
# Labels
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])

# Plot scatter patches
plt.figure(figsize=(5, 5))
for i in range(3):
    x_class = X[y == i]
    plt.plot(x_class[:, 0], x_class[:, 1], 'o-', label=f'Class {i}')
plt.title('Original Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
