from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def plot_pca(X, y):
    pca = PCA(n_components=2)
    X_transformed = pca.fit_transform(X)

    plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y, edgecolor='k', s=100, cmap='viridis')
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.title("PCA of Iris Dataset")
    plt.show()

plot_pca(X, y)
