import tkinter as tk
from tkinter import messagebox
import requests

# Initialize Tkinter window
root = tk.Tk()
root.title("Prediction App")
root.geometry("400x400")  # Menambahkan ukuran lebih lebar dan tinggi

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

label_age = tk.Label(root, text="Age")
label_age.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(root)
entry_age.grid(row=4, column=1, padx=10, pady=5)

# Radio buttons for categorical feature (Sex)
label_sex = tk.Label(root, text="Sex")
label_sex.grid(row=5, column=0, padx=10, pady=5, sticky="w")

var_sex = tk.StringVar(value='f')  # Default value

radio_sex_f = tk.Radiobutton(root, text="Female", variable=var_sex, value='f')
radio_sex_f.grid(row=5, column=1, sticky="w")
radio_sex_i = tk.Radiobutton(root, text="Infant", variable=var_sex, value='i')
radio_sex_i.grid(row=6, column=1, sticky="w")
radio_sex_m = tk.Radiobutton(root, text="Male", variable=var_sex, value='m')
radio_sex_m.grid(row=7, column=1, sticky="w")

# Predict button
button_predict = tk.Button(root, text="Predict", command="")
button_predict.grid(row=8, column=0, columnspan=2, pady=20)

root.mainloop()
