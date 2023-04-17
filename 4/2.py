from sklearn.cluster import KMeans

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

knn_centroids = KNNCentroids(k=3)
knn_centroids.fit(X_train, y_train)
predictions_centroids = knn_centroids.predict(X_test)
print(f"KNN Centroids accuracy: {accuracy_score(y_test, predictions_centroids)}")
