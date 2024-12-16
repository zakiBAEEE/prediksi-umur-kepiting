import tkinter as tk
from tkinter import messagebox
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
from mode.mode_input_manual import start_manual_input_mode # Impor mode_input_manual
from mode.mode_input_csv import predict_csv

def open_csv_input_mode():
    # Implementasikan mode input CSV di sini
    pass

def main():
    # Inisialisasi window Tkinter
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

    button_csv = tk.Button(root, text="Input CSV", font=label_font, command=predict_csv)
    button_csv.pack(pady=10)

    root.mainloop()

# Menambahkan pengecekan __name__ untuk memastikan bahwa kode di bawah hanya dijalankan saat file ini dieksekusi langsung
if __name__ == "__main__":
    main()
