import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class SimpleNeuralNetwork:
    def __init__(self, learning_rate=0.01, epochs=100, optimizer='SGD', random=1):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.optimizer = optimizer  # Tambahkan optimizer sebagai parameter
        self.bobot = None
        self.bias = None
        self.momentum_v = 0  # Variabel untuk Momentum
        self.m_t, self.v_t = 0, 0  # Variabel untuk Adam
        self.t = 0  # Iterasi untuk Adam
        np.random.seed(random)

    def train(self, x_latih, y_latih):
        # Inisialisasi bobot dan bias
        self.bobot = np.random.randn(x_latih.shape[1], 1)  # Bobot untuk jumlah fitur input
        self.bias = np.zeros((1, 1))  # Bias scalar
        
        beta1 = 0.9  # Faktor Momentum untuk Adam
        beta2 = 0.999  # Faktor RMSprop untuk Adam
        epsilon = 1e-8  # Untuk menghindari pembagian dengan nol

        # Pelatihan untuk jumlah epoch yang ditentukan
        for epoch in range(self.epochs):
            # Forward pass: Perkalian bobot dan input, ditambah bias
            output = np.dot(x_latih, self.bobot) + self.bias

            # Hitung error (selisih prediksi dengan target)
            error = y_latih - output

            # Backpropagation: Gradien dari error terhadap bobot dan bias
            d_weights = -2 * np.dot(x_latih.T, error) / x_latih.shape[0]
            d_bias = -2 * np.sum(error) / x_latih.shape[0]

            # Pembaruan bobot berdasarkan optimizer
            if self.optimizer == 'SGD':
                # Stochastic Gradient Descent (SGD)
                self.bobot -= self.learning_rate * d_weights
                self.bias -= self.learning_rate * d_bias

            elif self.optimizer == 'Momentum':
                # Momentum-based Gradient Descent
                self.momentum_v = 0.9 * self.momentum_v + self.learning_rate * d_weights
                self.bobot -= self.momentum_v
                self.bias -= self.learning_rate * d_bias

            elif self.optimizer == 'Adam':
                # Adam Optimizer
                self.t += 1
                self.m_t = beta1 * self.m_t + (1 - beta1) * d_weights
                self.v_t = beta2 * self.v_t + (1 - beta2) * (d_weights ** 2)

                # Bias correction
                m_t_hat = self.m_t / (1 - beta1 ** self.t)
                v_t_hat = self.v_t / (1 - beta2 ** self.t)

                # Update bobot dan bias
                self.bobot -= self.learning_rate * m_t_hat / (np.sqrt(v_t_hat) + epsilon)
                self.bias -= self.learning_rate * d_bias  # Bias tidak menggunakan Adam

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
