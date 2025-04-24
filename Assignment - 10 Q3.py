import numpy as np
N = 10

cartesian_points = np.random.randint(-10, 11, size=(N, 2))
print("Cartesian coordinates (integers):")
print(cartesian_points)

x = cartesian_points[:, 0]
y = cartesian_points[:, 1]

r = np.sqrt(x**2 + y**2)          
theta = np.arctan2(y, x)            

polar_points = np.column_stack((r, theta))

print("\nPolar coordinates (r, theta in radians):")
print(polar_points)
