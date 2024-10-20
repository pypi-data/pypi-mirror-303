import numpy as np

class LinearRegression:
    def __init__(self, x, y):
        self.data = x
        self.label = y
        self.m = 0  # Pente
        self.b = 0  # Ordonnée à l'origine
        self.n = len(x)

    def fit(self, epochs, lr):
        # Implémentation de la descente de gradient
        for i in range(epochs):
            y_pred = self.m * self.data + self.b
            
            # Calcul des dérivées par rapport aux paramètres
            D_m = (-2 / self.n) * sum(self.data * (self.label - y_pred))
            D_b = (-2 / self.n) * sum(self.label - y_pred)  

            # Mise à jour des paramètres
            self.m -= lr * D_m
            self.b -= lr * D_b  

    def predict(self, inp):
        y_pred = self.m * inp + self.b
        return y_pred
