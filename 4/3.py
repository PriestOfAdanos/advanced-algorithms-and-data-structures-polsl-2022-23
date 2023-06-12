import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def pca(X, num_components):
    # 1. Compute the mean
    mean = np.mean(X, axis=0)
    
    # 2. Center the data
    X_centered = X - mean
    
    # 3. Compute the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)
    
    # 4. Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # 5. Sort the eigenvectors by eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # 6. Select the top principal components
    principal_components = sorted_eigenvectors[:, :num_components]
    
    # 7. Project the data onto the principal components
    X_pca = np.dot(X_centered, principal_components)
    
    return X_pca

def plot_pca(X_pca, y):
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, edgecolor='k', s=100, cmap='viridis')
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.title("PCA of Iris Dataset (Implemented from Scratch)")
    plt.show()

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform PCA
X_pca = pca(X, num_components=2)

# Plot the transformed data
plot_pca(X_pca, y)
