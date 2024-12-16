
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import numpy as np
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
import joblib

try:
    model = joblib.load('Machine_Learning/model_baru')
except FileNotFoundError:
    raise Exception("Model file not found! Make sure the model file exists in the correct path.")

try:
    scaler_fitur_data = joblib.load('Machine_Learning/scaler_fiturData')
    scaler_label_data = joblib.load('Machine_Learning/scaler_labelData')
except FileNotFoundError:
    raise Exception("Scaler file not found! Make sure the scaler file exists in the correct path.")


def predict(features):
    """Menerima array fitur sebagai input dan mengembalikan hasil prediksi."""
    prediction = model.predict(features)
    return prediction.tolist()[0]  # Mengembalikan hasil sebagai float


def get_prediction(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result):
    try:
        length = float(entry_length.get())
        diameter = float(entry_diameter.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        shucked_weight = float(entry_shucked_weight.get())
        viscera_weight = float(entry_viscera_weight.get())
        shell_weight = float(entry_shell_weight.get())

        sex = var_sex.get()

        features = np.array([[length, diameter, height, weight,
                              shucked_weight, viscera_weight, shell_weight,
                              int(sex == 'f'), int(sex == 'i'), int(sex == 'm')]])

        features_normalized = scaler_fitur_data.transform(features)

        prediction_normalized = predict(features_normalized)

        prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])

        final_prediction = prediction_denormalized[0][0]
        label_result.config(text=f"Umur Kepiting: {final_prediction} Bulan")

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


def start_manual_input_mode():
    root = tk.Tk()
    root.title("Prediction Umur Kepiting - Manual Input")
    root.geometry("500x500")

    title_font = font.Font(family="Helvetica", size=17, weight="bold")
    label_font = font.Font(family="Arial", size=13, )
    result_font = font.Font(family="Arial", size=14, weight="bold")

    title_label = tk.Label(root, text="Prediksi Umur Kepiting", font=title_font, fg="Black")
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

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

    entry_length = entries["Length"]
    entry_diameter = entries["Diameter"]
    entry_height = entries["Height"]
    entry_weight = entries["Weight"]
    entry_shucked_weight = entries["Shucked Weight"]
    entry_viscera_weight = entries["Viscera Weight"]
    entry_shell_weight = entries["Shell Weight"]

    label_sex = tk.Label(root, text="Sex", font=label_font)
    label_sex.grid(row=8, column=0, padx=10, pady=5, sticky="e")

    var_sex = tk.StringVar(value='f')  # Default value

    frame_sex = tk.Frame(root)
    frame_sex.grid(row=8, column=1, pady=5, sticky="w")
    tk.Radiobutton(frame_sex, text="Female", variable=var_sex, value='f', font=label_font).pack(side="left", padx=10)
    tk.Radiobutton(frame_sex, text="Infant", variable=var_sex, value='i', font=label_font).pack(side="left", padx=5)
    tk.Radiobutton(frame_sex, text="Male", variable=var_sex, value='m', font=label_font).pack(side="left", padx=5)

    button_predict = tk.Button(root, text="Predict", command=lambda: get_prediction(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result), bg="blue", fg="white", font=label_font)
    button_predict.grid(row=9, column=0, columnspan=2, pady=20)

    label_result = tk.Label(root, text="Prediction result will appear here", font=result_font, fg="red", wraplength=400)
    label_result.grid(row=10, column=0, columnspan=2, pady=20)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()
