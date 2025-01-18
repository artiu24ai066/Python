import math
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

points = []
print("Enter 10 3-D points (x y z format):")
for i in range(10):
    point = tuple(map(float, input(f"Point {i+1}: ").split()))
    points.append(point)

nearest_neighbors = []
for i, point in enumerate(points):
    nearest_distance = float('inf')
    nearest_point = None
    for j, other_point in enumerate(points):
        if i != j:  
            distance = euclidean_distance(point, other_point)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = other_point
    nearest_neighbors.append((point, nearest_point))

print("\nNearest Neighbors:")
for point, neighbor in nearest_neighbors:
    print(f"Point: {point} -> Nearest Neighbor: {neighbor}")
