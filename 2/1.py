import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))

def nearest_neighbor(train_data, train_labels, test_point):
    min_distance = float('inf')
    nearest_label = None

    for i, train_point in enumerate(train_data):
        distance = euclidean_distance(test_point, train_point)
        if distance < min_distance:
            min_distance = distance
            nearest_label = train_labels[i]

    return nearest_label

def nearest_neighbor_algorithm(train_data, train_labels, test_data):
    return [nearest_neighbor(train_data, train_labels, test_point) for test_point in test_data]

# Example usage
train_data = [[1, 1], [2, 2], [3, 3], [4, 4]]
train_labels = [0, 0, 1, 1]
test_data = [[1.5, 1.5], [3.5, 3.5]]

predicted_labels = nearest_neighbor_algorithm(train_data, train_labels, test_data)
print(f"train_data : {train_data}")
print(f"train_labels: {train_labels}")
print(f"test_data: {test_data}")
print(f"predicted_labels: {predicted_labels}")  # Output: [0, 1]
input()