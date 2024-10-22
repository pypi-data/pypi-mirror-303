import numpy as np

from typing import List, Dict
from abc import ABC, abstractmethod
from scipy.spatial import distance_matrix

class Model(ABC):
    
    @abstractmethod
    def fit(self,X :np.ndarray, y :np.ndarray)->None:
        pass 
    @abstractmethod
    def predict(self,X :np.ndarray)-> np.ndarray:
        pass
    
class LinearRegression(Model):
    def __init__(self, fit_intercept: bool =False):
        self.fit_intercept = fit_intercept

    def fit(self,X :np.ndarray, y : np.ndarray):
        if self.fit_intercept:
            X = np.concatenate((np.array([1 for i in range(len(X))]).reshape(-1,1), X), axis=1)
        beta = np.linalg.inv(X.T @ X) @ X.T @ y
        return beta 
    
    def predict(self,X :np.ndarray, y :np.ndarray)-> np.ndarray:
        
        if self.beta is None:
            raise ValueError("Model is not fitted yet!")
        
        if self.fit_intercept:
            X = np.concatenate((np.array([1 for i in range(len(X))]).reshape(-1,1), X), axis=1)
            
        y_pred = X @ self.beta
        return y_pred

class KneighbourghRegression(Model):
    def __init__(self,K):
        self.K = K
        self.x_train = None
        self.y_train = None
        
    def fit(self,X :np.ndarray, y :np.ndarray):
        self.x_train = X
        self.y_train = y

    def predict(self,X :np.ndarray)-> np.ndarray:
        if self.x_train is None or self.y_train is None:
            raise ValueError("Model is not fitted yet!")
    
        # Calculer la matrice de distance entre les points de test et les points d'entraînement
        dists = distance_matrix(X, self.x_train)
        
        # Trouver les indices des K plus proches voisins pour chaque point de test
        k_nearest_indices = np.argsort(dists, axis=1)[:, :self.K]
        
        # Prédire la sortie en prenant la moyenne des étiquettes des K plus proches voisins
        y_pred = np.array([self.y_train[indices].mean() for indices in k_nearest_indices])
        
        return y_pred
