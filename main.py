import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import pandas as pd
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
import joblib

# Fungsi untuk load model dan scaler
def load_model_and_scalers():
    global model, scaler_fitur_data, scaler_label_data
    try:
        model = joblib.load('Machine_Learning/model')
        scaler_fitur_data = joblib.load('Machine_Learning/scaler_fiturData')
        scaler_label_data = joblib.load('Machine_Learning/scaler_labelData')
    except FileNotFoundError as e:
        messagebox.showerror("File Not Found", f"Error loading model or scaler files: {e}")
        exit()

# Fungsi untuk prediksi input manual
def get_prediction_manual():
    try:
        # Ambil input dari entry fields
        length = float(entry_length.get())
        diameter = float(entry_diameter.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        shucked_weight = float(entry_shucked_weight.get())
        viscera_weight = float(entry_viscera_weight.get())
        shell_weight = float(entry_shell_weight.get())
        sex = var_sex.get()

        # Data input untuk dikirim ke fungsi prediksi
        features = np.array([[length, diameter, height, weight, shucked_weight, viscera_weight, shell_weight,
                              int(sex == 'f'), int(sex == 'i'), int(sex == 'm')]])

        # Normalisasi input menggunakan scaler
        features_normalized = scaler_fitur_data.transform(features)

        # Panggil fungsi prediksi
        prediction_normalized = model.predict(features_normalized)
        prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])
        
        final_prediction = prediction_denormalized[0][0]
        label_result.config(text=f"Predicted Value: {final_prediction:.1f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))

# Fungsi untuk membuka file CSV dan melakukan prediksi
def upload_and_predict_csv():
    try:
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return  # Jika tidak ada file yang dipilih

        # Baca file CSV
        df = pd.read_csv(file_path)
        # Pastikan data memiliki kolom yang sesuai
        if not set(["Length", "Diameter", "Height", "Weight", "Shucked Weight", "Viscera Weight", "Shell Weight"]).issubset(df.columns):
            messagebox.showerror("CSV Error", "CSV file must contain the necessary columns.")
            return

        # Normalisasi fitur
        features = df[["Length", "Diameter", "Height", "Weight", "Shucked Weight", "Viscera Weight", "Shell Weight"]].values
        features_normalized = scaler_fitur_data.transform(features)
        
        # Prediksi untuk seluruh data
        predictions_normalized = model.predict(features_normalized)
        predictions_denormalized = scaler_label_data.inverse_transform([predictions_normalized])

        # Menambahkan hasil prediksi ke dataframe dan menyimpannya kembali
        df["Predicted Age"] = predictions_denormalized[0]
        output_file_path = file_path.replace(".csv", "_predicted.csv")
        df.to_csv(output_file_path, index=False)

        messagebox.showinfo("Predictions Saved", f"Predictions saved to {output_file_path}")
    except Exception as e:
        messagebox.showerror("CSV Error", f"An error occurred: {e}")

# Fungsi untuk beralih ke mode input manual
def show_manual_input_mode():
    clear_window()
    
    # Tambahkan semua elemen untuk mode input manual
    label_title.config(text="Mode Input Manual")
    
    label_length = tk.Label(root, text="Length", font=label_font)
    label_length.grid(row=1, column=0)
    entry_length = tk.Entry(root)
    entry_length.grid(row=1, column=1)
    
    label_diameter = tk.Label(root, text="Diameter", font=label_font)
    label_diameter.grid(row=2, column=0)
    entry_diameter = tk.Entry(root)
    entry_diameter.grid(row=2, column=1)
    
    # Add other entries for height, weight, etc.
    button_predict = tk.Button(root, text="Predict", command=get_prediction_manual)
    button_predict.grid(row=9, column=0, columnspan=2, pady=20)
    
    button_back = tk.Button(root, text="Back to Mode Selection", command=show_mode_selection)
    button_back.grid(row=10, column=0, columnspan=2)

# Fungsi untuk menampilkan pilihan mode prediksi
def show_mode_selection():
    clear_window()
    
    # Judul
    label_title.config(text="Pilih Mode Prediksi")

    # Tombol untuk Mode Input Manual
    button_manual = tk.Button(root, text="Mode Input Manual", command=show_manual_input_mode)
    button_manual.grid(row=1, column=0, columnspan=2, pady=10)

    # Tombol untuk Mode Input CSV
    button_csv = tk.Button(root, text="Mode Input CSV", command=upload_and_predict_csv)
    button_csv.grid(row=2, column=0, columnspan=2, pady=10)

# Fungsi untuk membersihkan window sebelum menampilkan mode baru
def clear_window():
    for widget in root.winfo_children():
        widget.grid_forget()

# Setup Tkinter window
root = tk.Tk()
root.title("Prediksi Umur Kepiting")
root.geometry("500x600")

# Font styles
label_font = ("Arial", 12)

# Label untuk judul
label_title = tk.Label(root, text="Pilih Mode Prediksi", font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=20)

# Mulai dengan menampilkan mode pilihan
show_mode_selection()

root.mainloop()
