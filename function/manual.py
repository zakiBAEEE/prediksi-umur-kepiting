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

def cm_to_feet(cm):
    return cm / 30.48

def gram_to_ons(gram):
    return gram / 28.3495


def predict_manual(features):
    prediction = model.predict(features)
    return prediction.tolist()[0]  

def get_prediction_manual(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result):
    try:
        # KONVERSI SATUAN
        length = cm_to_feet(float(entry_length.get()))
        diameter = cm_to_feet(float(entry_diameter.get()))
        height = cm_to_feet(float(entry_height.get()))
        weight = gram_to_ons(float(entry_weight.get()))
        shucked_weight = gram_to_ons(float(entry_shucked_weight.get()))
        viscera_weight = gram_to_ons(float(entry_viscera_weight.get()))
        shell_weight = gram_to_ons(float(entry_shell_weight.get()))

        sex = var_sex.get()

        features = np.array([[length, diameter, height, weight,
                              shucked_weight, viscera_weight, shell_weight,
                              int(sex == 'f'), int(sex == 'i'), int(sex == 'm')]])

        features_normalized = scaler_fitur_data.transform(features)

        prediction_normalized = predict_manual(features_normalized)

        prediction_denormalized = scaler_label_data.inverse_transform([prediction_normalized])

        final_prediction = prediction_denormalized[0][0]
        label_result.config(text=f"Umur Kepiting: {final_prediction:.1f} Bulan")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")
    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))