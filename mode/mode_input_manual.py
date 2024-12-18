import tkinter as tk
from Machine_Learning.jaringanSarafTiruan import SimpleNeuralNetwork
from function.manual import get_prediction_manual


def start_manual_input_mode():
    root = tk.Tk()
    root.title("Prediksi Umur Kepiting - Input Manual")
    root.geometry("500x600")  # Tinggi diperbesar agar layout lebih pas

    title_font = ("Helvetica", 17, "bold")
    label_font = ("Arial", 13)
    result_font = ("Arial", 14, "bold")

    title_label = tk.Label(root, text="Prediksi Umur Kepiting", font=title_font, fg="Black")
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    # List input dengan satuan feet dan ons
    inputs = [
        ("Length (Cm)", 1), ("Diameter (Cm)", 2), ("Height (Cm)", 3),
        ("Weight (Gram)", 4), ("Shucked Weight (Gram)", 5), ("Viscera Weight (Gram)", 6), ("Shell Weight (Gram)", 7)
    ]

    entries = {}
    for text, row in inputs:
        label = tk.Label(root, text=text, font=label_font)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, font=label_font)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        entries[text] = entry

    entry_length = entries["Length (feet)"]
    entry_diameter = entries["Diameter (feet)"]
    entry_height = entries["Height (feet)"]
    entry_weight = entries["Weight (ons)"]
    entry_shucked_weight = entries["Shucked Weight (ons)"]
    entry_viscera_weight = entries["Viscera Weight (ons)"]
    entry_shell_weight = entries["Shell Weight (ons)"]

    label_sex = tk.Label(root, text="Sex", font=label_font)
    label_sex.grid(row=8, column=0, padx=10, pady=5, sticky="e")

    var_sex = tk.StringVar(value='f')  # Default value

    frame_sex = tk.Frame(root)
    frame_sex.grid(row=8, column=1, pady=5, sticky="w")
    tk.Radiobutton(frame_sex, text="Female", variable=var_sex, value='f', font=label_font).pack(side="left", padx=10)
    tk.Radiobutton(frame_sex, text="Infant", variable=var_sex, value='i', font=label_font).pack(side="left", padx=5)
    tk.Radiobutton(frame_sex, text="Male", variable=var_sex, value='m', font=label_font).pack(side="left", padx=5)

    # Frame untuk tombol di tengah
    frame_buttons = tk.Frame(root)
    frame_buttons.grid(row=9, column=0, columnspan=2, pady=20)

    button_predict = tk.Button(frame_buttons, text="Predict", command=lambda: get_prediction_manual(entry_length, entry_diameter, entry_height, entry_weight, entry_shucked_weight, entry_viscera_weight, entry_shell_weight, var_sex, label_result), bg="blue", fg="white", font=label_font)
    button_predict.pack(side="left", padx=10)

    reset_button = tk.Button(
        frame_buttons, 
        text="Reset Field", 
        font=("Arial", 12), 
        bg="red", 
        fg="white",
        command=lambda: [entry.delete(0, tk.END) for entry in entries.values()]  # Menghapus semua entry
    )
    reset_button.pack(side="left", padx=10)

    label_result = tk.Label(root, text="Prediction result will appear here", font=result_font, fg="red", wraplength=400)
    label_result.grid(row=10, column=0, columnspan=2, pady=20)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()



