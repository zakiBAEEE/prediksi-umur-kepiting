import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import joblib
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork


# Load model dan scaler
model = joblib.load('Machine_Learning/model_baru')
scaler_fitur_data = joblib.load('Machine_Learning/scaler_fiturData')
scaler_label_data = joblib.load('Machine_Learning/scaler_labelData')

def cm_to_feet(cm):
    return cm / 30.48

def gram_to_ons(gram):
    return gram / 28.3495

# Fungsi prediksi untuk file CSV
def predict_csv():
    try:
        # Dialog untuk memilih file CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return  # Jika user membatalkan pilihan file

        # Baca file CSV
        df = pd.read_csv(file_path)

        # Pastikan kolom input sesuai
        required_columns = ['Length', 'Diameter', 'Height', 'Weight',
                            'Shucked Weight', 'Viscera Weight', 'Shell Weight',
                            'Sex_F', 'Sex_I', 'Sex_M']
        if not all(col in df.columns for col in required_columns):
            messagebox.showerror("Error", "File CSV tidak memiliki kolom yang sesuai.")
            return
        
        df['Length'] = df['Length'].apply(cm_to_feet)
        df['Diameter'] = df['Diameter'].apply(cm_to_feet)
        df['Height'] = df['Height'].apply(cm_to_feet)
        df['Weight'] = df['Weight'].apply(gram_to_ons)
        df['Shucked Weight'] = df['Shucked Weight'].apply(gram_to_ons)
        df['Viscera Weight'] = df['Viscera Weight'].apply(gram_to_ons)
        df['Shell Weight'] = df['Shell Weight'].apply(gram_to_ons)

        # Normalisasi fitur
        features = df[required_columns].values
        features_normalized = scaler_fitur_data.transform(features)

        # Prediksi menggunakan model
        predictions_normalized = model.predict(features_normalized)
        predictions_denormalized = scaler_label_data.inverse_transform(predictions_normalized.reshape(-1, 1))

        # Tambahkan hasil prediksi ke DataFrame
        df['Umur'] = predictions_denormalized.flatten()

        # Simpan hasil ke file baru
        save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV Files", "*.csv")],
                                                 initialfile="predicted_results.csv")
        if save_path:
            df.to_csv(save_path, index=False)
            messagebox.showinfo("Success", f"Hasil prediksi berhasil disimpan di:\n{save_path}")
        else:
            messagebox.showwarning("Warning", "Penyimpanan dibatalkan.")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")


