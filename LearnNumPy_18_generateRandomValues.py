import numpy as np

# Set seed
np.random.seed(1)

# Generate 3 random integers b/w 1 and 10
print(np.random.randint(0, 11, 3))

# Draw 3 numbers from a normal distribution with mean 1.0 and std 2.0
print(np.random.normal(1.0, 2.0, 3))
