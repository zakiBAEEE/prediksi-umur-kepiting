from flask import Flask, request, jsonify
import joblib
import numpy as np
from jaringanSarafTiruan import SimpleNeuralNetwork
app = Flask(__name__)

#DATA INPUT BLM DINORMALISASI WOII
# Load model yang telah disimpan menggunakan joblib
try:
    model = joblib.load('Machine Learning/model')
except FileNotFoundError:
    raise Exception("Model file not found! Make sure 'pengetahuan' is in the same directory.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Pastikan permintaan berisi JSON
        data = request.get_json()  # Mengambil data JSON dari permintaan

        # Ambil data input dari JSON
        length = float(data['length'])
        diameter = float(data['diameter'])
        height = float(data['height'])
        weight = float(data['weight'])
        shucked_weight = float(data['shucked_weight'])
        viscera_weight = float(data['viscera_weight'])
        shell_weight = float(data['shell_weight'])
        sex = data['sex']  # Menangani sex sebagai string

        # Konversi 'sex' menjadi fitur numerik (misalnya, Female=0, Male=1, Infant=2)
        if sex == 'female':
            sex_f = 1
            sex_m = 0
            sex_i = 0
        elif sex == 'male':
            sex_f = 0
            sex_m = 1
            sex_i = 0
        else:
            sex_f = 0
            sex_m = 0
            sex_i = 1

        # Gabungkan input menjadi array fitur
        features = np.array([[length, diameter, height, weight, shucked_weight, viscera_weight, shell_weight, sex_f, sex_i, sex_m]])

        # Lakukan prediksi
        prediction = model.predict(features)

        # Convert prediction result to a list so it can be serialized to JSON
        prediction_list = prediction.tolist()

        # Kirim hasil prediksi kembali ke frontend
        return jsonify(predicted_value=prediction_list[0])

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
