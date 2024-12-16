import tkinter as tk
from tkinter import messagebox
import numpy as np
from jaringanSarafTiruan import SimpleNeuralNetwork  # Import fungsi prediksi dari model Anda
import joblib

# Load model yang telah disimpan menggunakan joblib
try:
    model = joblib.load('Machine Learning/model')
except FileNotFoundError:
    raise Exception("Model file not found! Make sure the model file exists in the correct path.")

try:
    scaler_fitur_data = joblib.load('Machine Learning/scaler_fiturData')
    scaler_label_data = joblib.load('Machine Learning/scaler_labelData')
except FileNotFoundError:
    raise Exception("Scaler file not found! Make sure the scaler file exists in the correct path.")


# Fungsi untuk mendapatkan prediksi
def predict(features):
    """Menerima array fitur sebagai input dan mengembalikan hasil prediksi."""
    prediction = model.predict(features)
    return prediction.tolist()[0]  # Mengembalikan hasil sebagai float

# Fungsi untuk mengirim data input dan mendapatkan prediksi
def get_prediction():
    try:
        # Ambil input dari entry fields
        length = float(entry_length.get())
        diameter = float(entry_diameter.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        shucked_weight = float(entry_shucked_weight.get())
        viscera_weight = float(entry_viscera_weight.get())
        shell_weight = float(entry_shell_weight.get())

        # Ambil input dari radio button
        sex = var_sex.get()

        # Data input untuk dikirim ke fungsi predict
        features = np.array([[
            length, diameter, height, weight, 
            shucked_weight, viscera_weight, shell_weight,
            int(sex == 'f'), int(sex == 'i'), int(sex == 'm')
        ]])

         # Normalisasi input menggunakan scaler
        features_normalized = scaler_fitur_data.transform(features)

        # Panggil fungsi predict dan dapatkan hasilnya
        prediction_normalized = predict(features_normalized)

        prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])

        # final_prediction = prediction_denormalized[0][0]


        label_result.config(text=f"Predicted Value: {prediction_denormalized}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))

# Initialize Tkinter window
root = tk.Tk()
root.title("Prediction App")
root.geometry("400x600")  # Menambahkan ukuran lebih tinggi untuk input tambahan

# Labels and entry fields for features
label_length = tk.Label(root, text="Length")
label_length.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)

label_diameter = tk.Label(root, text="Diameter")
label_diameter.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_diameter = tk.Entry(root)
entry_diameter.grid(row=1, column=1, padx=10, pady=5)

label_height = tk.Label(root, text="Height")
label_height.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1, padx=10, pady=5)

label_weight = tk.Label(root, text="Weight")
label_weight.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_weight = tk.Entry(root)
entry_weight.grid(row=3, column=1, padx=10, pady=5)

# Input baru: Shucked Weight
label_shucked_weight = tk.Label(root, text="Shucked Weight")
label_shucked_weight.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_shucked_weight = tk.Entry(root)
entry_shucked_weight.grid(row=4, column=1, padx=10, pady=5)

# Input baru: Viscera Weight
label_viscera_weight = tk.Label(root, text="Viscera Weight")
label_viscera_weight.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_viscera_weight = tk.Entry(root)
entry_viscera_weight.grid(row=5, column=1, padx=10, pady=5)

# Input baru: Shell Weight
label_shell_weight = tk.Label(root, text="Shell Weight")
label_shell_weight.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_shell_weight = tk.Entry(root)
entry_shell_weight.grid(row=6, column=1, padx=10, pady=5)

# Radio buttons for categorical feature (Sex)
label_sex = tk.Label(root, text="Sex")
label_sex.grid(row=7, column=0, padx=10, pady=5, sticky="w")

var_sex = tk.StringVar(value='f')  # Default value

radio_sex_f = tk.Radiobutton(root, text="Female", variable=var_sex, value='f')
radio_sex_f.grid(row=7, column=1, sticky="w")
radio_sex_i = tk.Radiobutton(root, text="Infant", variable=var_sex, value='i')
radio_sex_i.grid(row=8, column=1, sticky="w")
radio_sex_m = tk.Radiobutton(root, text="Male", variable=var_sex, value='m')
radio_sex_m.grid(row=9, column=1, sticky="w")

# Predict button
button_predict = tk.Button(root, text="Predict", command=get_prediction)
button_predict.grid(row=10, column=0, columnspan=2, pady=20)

# Result Label
label_result = tk.Label(root, text="Prediction result will appear here", wraplength=300)
label_result.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
