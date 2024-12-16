# main.py
import tkinter as tk
from tkinter import messagebox
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
from mode_input_manual import start_manual_input_mode # Impor mode_input_manual



def open_csv_input_mode():
    # Implementasikan mode input CSV di sini
    pass

# Initialize Tkinter window
root = tk.Tk()
root.title("Pilih Mode Prediksi")
root.geometry("300x200")

# Styling
label_font = ("Arial", 14)

# Title
title_label = tk.Label(root, text="Pilih Mode Prediksi", font=label_font)
title_label.pack(pady=20)

# Buttons untuk memilih mode prediksi
button_manual = tk.Button(root, text="Input Manual", font=label_font, command=start_manual_input_mode)
button_manual.pack(pady=10)

button_csv = tk.Button(root, text="Input CSV", font=label_font, command=open_csv_input_mode)
button_csv.pack(pady=10)

root.mainloop()
