# import tkinter as tk
# from tkinter import messagebox
# from tkinter import font
# import numpy as np
# from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
# import joblib

# # Load model yang telah disimpan menggunakan joblib
# try:
#     model = joblib.load('Machine_Learning/model')
# except FileNotFoundError:
#     raise Exception("Model file not found! Make sure the model file exists in the correct path.")

# try:
#     scaler_fitur_data = joblib.load('Machine_Learning/scaler_fiturData')
#     scaler_label_data = joblib.load('Machine_Learning/scaler_labelData')
# except FileNotFoundError:
#     raise Exception("Scaler file not found! Make sure the scaler file exists in the correct path.")


# # Fungsi untuk mendapatkan prediksi
# def predict(features):
#     """Menerima array fitur sebagai input dan mengembalikan hasil prediksi."""
#     prediction = model.predict(features)
#     return prediction.tolist()[0]  # Mengembalikan hasil sebagai float


# # Fungsi untuk mengirim data input dan mendapatkan prediksi
# def get_prediction():
#     try:
#         # Ambil input dari entry fields
#         length = float(entry_length.get())
#         diameter = float(entry_diameter.get())
#         height = float(entry_height.get())
#         weight = float(entry_weight.get())
#         shucked_weight = float(entry_shucked_weight.get())
#         viscera_weight = float(entry_viscera_weight.get())
#         shell_weight = float(entry_shell_weight.get())

#         # Ambil input dari radio button
#         sex = var_sex.get()

#         # Data input untuk dikirim ke fungsi predict
#         features = np.array([[length, diameter, height, weight,
#                               shucked_weight, viscera_weight, shell_weight,
#                               int(sex == 'f'), int(sex == 'i'), int(sex == 'm')]])

#         # Normalisasi input menggunakan scaler
#         features_normalized = scaler_fitur_data.transform(features)

#         # Panggil fungsi predict dan dapatkan hasilnya
#         prediction_normalized = predict(features_normalized)

#         prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])

#         # Update label result
#         final_prediction = prediction_denormalized[0][0]
#         label_result.config(text=f"Umur Kepiting: {final_prediction:.1f} Bulan")

#         # Clear semua input field setelah prediksi
#         entry_length.delete(0, tk.END)
#         entry_diameter.delete(0, tk.END)
#         entry_height.delete(0, tk.END)
#         entry_weight.delete(0, tk.END)
#         entry_shucked_weight.delete(0, tk.END)
#         entry_viscera_weight.delete(0, tk.END)
#         entry_shell_weight.delete(0, tk.END)
#         var_sex.set('f')


#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
#     except Exception as e:
#         messagebox.showerror("Prediction Error", str(e))


# # Initialize Tkinter window
# root = tk.Tk()
# root.title("Prediction Umur Kepiting")
# root.geometry("500x500")  # Menambahkan ukuran lebih tinggi untuk input tambahan

# # Styling
# title_font = font.Font(family="Helvetica", size=17, weight="bold")
# label_font = font.Font(family="Arial", size=13, )
# result_font = font.Font(family="Arial", size=14, weight="bold")

# # Title
# title_label = tk.Label(root, text="Prediksi Umur Kepiting", font=title_font, fg="Black")
# title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# # Labels and entry fields for features
# inputs = [
#     ("Length", 1), ("Diameter", 2), ("Height", 3),
#     ("Weight", 4), ("Shucked Weight", 5), ("Viscera Weight", 6), ("Shell Weight", 7)
# ]

# entries = {}
# for text, row in inputs:
#     label = tk.Label(root, text=text, font=label_font)
#     label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
#     entry = tk.Entry(root, font=label_font)
#     entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
#     entries[text] = entry

# # Assign to specific variables
# entry_length = entries["Length"]
# entry_diameter = entries["Diameter"]
# entry_height = entries["Height"]
# entry_weight = entries["Weight"]
# entry_shucked_weight = entries["Shucked Weight"]
# entry_viscera_weight = entries["Viscera Weight"]
# entry_shell_weight = entries["Shell Weight"]

# # Radio buttons for categorical feature (Sex)
# label_sex = tk.Label(root, text="Sex", font=label_font)
# label_sex.grid(row=8, column=0, padx=10, pady=5, sticky="e")

# var_sex = tk.StringVar(value='f')  # Default value

# frame_sex = tk.Frame(root)
# frame_sex.grid(row=8, column=1, pady=5, sticky="w")
# tk.Radiobutton(frame_sex, text="Female", variable=var_sex, value='f', font=label_font).pack(side="left", padx=10)
# tk.Radiobutton(frame_sex, text="Infant", variable=var_sex, value='i', font=label_font).pack(side="left", padx=5)
# tk.Radiobutton(frame_sex, text="Male", variable=var_sex, value='m', font=label_font).pack(side="left", padx=5)

# # Fungsi efek hover
# def on_enter(event):
#     button_predict.config(bg="red", fg="white")  # Ubah warna tombol saat hover

# def on_leave(event):
#     button_predict.config(bg="blue", fg="white")  # Kembali ke warna semula

# # Predict button
# button_predict = tk.Button(root, text="Predict", command=get_prediction, bg="blue", fg="white", font=label_font)
# button_predict.grid(row=9, column=0, columnspan=2, pady=20)

# # Bind event hover
# button_predict.bind("<Enter>", on_enter)  # Saat mouse masuk
# button_predict.bind("<Leave>", on_leave)  # Saat mouse keluar


# # Result Label (Centered)
# label_result = tk.Label(root, text="Prediction result will appear here", font=result_font, fg="red", wraplength=400)
# label_result.grid(row=10, column=0, columnspan=2, pady=20)

# # Center alignment
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.mainloop()



# mode_input_manual.py
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import numpy as np
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
import joblib

# Load model yang telah disimpan menggunakan joblib
try:
    model = joblib.load('Machine_Learning/model')
except FileNotFoundError:
    raise Exception("Model file not found! Make sure the model file exists in the correct path.")

try:
    scaler_fitur_data = joblib.load('Machine_Learning/scaler_fiturData')
    scaler_label_data = joblib.load('Machine_Learning/scaler_labelData')
except FileNotFoundError:
    raise Exception("Scaler file not found! Make sure the scaler file exists in the correct path.")


# Fungsi untuk mendapatkan prediksi
def predict(features):
    """Menerima array fitur sebagai input dan mengembalikan hasil prediksi."""
    prediction = model.predict(features)
    return prediction.tolist()[0]  # Mengembalikan hasil sebagai float


# Fungsi untuk mengirim data input dan mendapatkan prediksi
def get_prediction(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result):
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
        features = np.array([[length, diameter, height, weight,
                              shucked_weight, viscera_weight, shell_weight,
                              int(sex == 'f'), int(sex == 'i'), int(sex == 'm')]])

        # Normalisasi input menggunakan scaler
        features_normalized = scaler_fitur_data.transform(features)

        # Panggil fungsi predict dan dapatkan hasilnya
        prediction_normalized = predict(features_normalized)

        prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])

        # Update label result
        final_prediction = prediction_denormalized[0][0]
        label_result.config(text=f"Umur Kepiting: {final_prediction:.1f} Bulan")

        # Clear semua input field setelah prediksi
        entry_length.delete(0, tk.END)
        entry_diameter.delete(0, tk.END)
        entry_height.delete(0, tk.END)
        entry_weight.delete(0, tk.END)
        entry_shucked_weight.delete(0, tk.END)
        entry_viscera_weight.delete(0, tk.END)
        entry_shell_weight.delete(0, tk.END)
        var_sex.set('f')

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))


# Initialize Tkinter window for manual input mode
def start_manual_input_mode():
    root = tk.Tk()
    root.title("Prediction Umur Kepiting - Manual Input")
    root.geometry("500x500")

    # Styling
    title_font = font.Font(family="Helvetica", size=17, weight="bold")
    label_font = font.Font(family="Arial", size=13, )
    result_font = font.Font(family="Arial", size=14, weight="bold")

    # Title
    title_label = tk.Label(root, text="Prediksi Umur Kepiting", font=title_font, fg="Black")
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    # Labels and entry fields for features
    inputs = [
        ("Length", 1), ("Diameter", 2), ("Height", 3),
        ("Weight", 4), ("Shucked Weight", 5), ("Viscera Weight", 6), ("Shell Weight", 7)
    ]

    entries = {}
    for text, row in inputs:
        label = tk.Label(root, text=text, font=label_font)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, font=label_font)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        entries[text] = entry

    # Assign to specific variables
    entry_length = entries["Length"]
    entry_diameter = entries["Diameter"]
    entry_height = entries["Height"]
    entry_weight = entries["Weight"]
    entry_shucked_weight = entries["Shucked Weight"]
    entry_viscera_weight = entries["Viscera Weight"]
    entry_shell_weight = entries["Shell Weight"]

    # Radio buttons for categorical feature (Sex)
    label_sex = tk.Label(root, text="Sex", font=label_font)
    label_sex.grid(row=8, column=0, padx=10, pady=5, sticky="e")

    var_sex = tk.StringVar(value='f')  # Default value

    frame_sex = tk.Frame(root)
    frame_sex.grid(row=8, column=1, pady=5, sticky="w")
    tk.Radiobutton(frame_sex, text="Female", variable=var_sex, value='f', font=label_font).pack(side="left", padx=10)
    tk.Radiobutton(frame_sex, text="Infant", variable=var_sex, value='i', font=label_font).pack(side="left", padx=5)
    tk.Radiobutton(frame_sex, text="Male", variable=var_sex, value='m', font=label_font).pack(side="left", padx=5)

    # Predict button
    button_predict = tk.Button(root, text="Predict", command=lambda: get_prediction(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result), bg="blue", fg="white", font=label_font)
    button_predict.grid(row=9, column=0, columnspan=2, pady=20)

    # Result Label (Centered)
    label_result = tk.Label(root, text="Prediction result will appear here", font=result_font, fg="red", wraplength=400)
    label_result.grid(row=10, column=0, columnspan=2, pady=20)

    # Center alignment
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()