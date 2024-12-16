import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
class SimpleNeuralNetwork:
    def __init__(self, learning_rate=0.01, epochs=100, random=1):

        self.learning_rate = learning_rate
        self.epochs = epochs
        self.bobot = None
        self.bias = None
        np.random.seed(random)

    def train(self, x_latih, y_latih):

        # Inisialisasi bobot dan bias
        self.bobot = np.random.randn(x_latih.shape[1], 1)  # Bobot untuk jumlah fitur input
        self.bias = np.zeros((1, 1))  # Bias scalar

        # Pelatihan untuk jumlah epoch yang ditentukan
        for epoch in range(self.epochs):
            # Forward pass: Perkalian bobot dan input, ditambah bias
            output = np.dot(x_latih, self.bobot) + self.bias

            # Hitung error (selisih prediksi dengan target)
            error = y_latih - output

            # Backpropagation: Gradien dari error terhadap bobot dan bias
            d_weights = -2 * np.dot(x_latih.T, error) / x_latih.shape[0]
            d_bias = -2 * np.sum(error) / x_latih.shape[0]

            # Update bobot dan bias menggunakan gradien descent
            self.bobot -= self.learning_rate * d_weights
            self.bias -= self.learning_rate * d_bias

    def evaluate(self, x_uji, y_uji):
        prediksi = np.dot(x_uji, self.bobot) + self.bias
        mae = mean_absolute_error(y_uji, prediksi)
        mse = mean_squared_error(y_uji, prediksi)
        r2 = r2_score(y_uji, prediksi)
        return mae, mse, r2

    def predict(self, x_input):

        if self.bobot is None or self.bias is None:
            raise ValueError("Model belum dilatih. Gunakan metode 'train' terlebih dahulu.")

        return np.dot(x_input, self.bobot) + self.bias
