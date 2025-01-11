import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Hauptfenster mit Scrollbar")

# Canvas erstellen, um das Scrollen zu ermöglichen
canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

# Scrollbar erstellen und an den Canvas binden
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Canvas mit der Scrollbar verbinden
canvas.configure(yscrollcommand=scrollbar.set)

# Frame erstellen, das alle Widgets enthält, die gescrollt werden sollen
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Einige Beispiel-Widgets hinzufügen, um den Scrollbereich zu füllen
for i in range(50):  # 50 Labels als Beispiel
    label = tk.Label(frame, text=f"Label {i+1}")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

# Das Scrollen anpassen, wenn sich der Inhalt ändert
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Die Größe des Hauptfensters anpassen
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Tkinter Schleife starten
root.mainloop()
