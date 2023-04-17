from sklearn.cluster import KMeans
import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
    
class KNNCentroids:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        self.centroids = self._compute_centroids()

    def _compute_centroids(self):
        kmeans = KMeans(n_clusters=self.k)
        kmeans.fit(self.X_train)
        return kmeans.cluster_centers_

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        distances = [euclidean_distance(x, centroid) for centroid in self.centroids]
        closest_centroid_index = np.argmin(distances)
        return self.y_train[closest_centroid_index]
        
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

knn_centroids = KNNCentroids(k=50)
knn_centroids.fit(X_train, y_train)
predictions_centroids = knn_centroids.predict(X_test)
print(f"KNN Centroids accuracy: {accuracy_score(y_test, predictions_centroids)}")
