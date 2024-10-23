# archivo: main.py

import tkinter as tk
from tkinter import messagebox
from . import augmented_reality_piramide

def ejecutar_subtema(subtema):
    """Ejecuta el subtema seleccionado."""
    try:
        if subtema == "augmented_reality":
            augmented_reality_piramide.ejecutar_tracker()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrarVentana():
    """Muestra la ventana principal con los botones de subtemas."""
    ventana = tk.Tk()
    ventana.title("Ejecutar Subtemas")

    btn_ar_tracker = tk.Button(ventana, text="Augmented Reality Tracker",
                                command=lambda: ejecutar_subtema("augmented_reality"))
    btn_ar_tracker.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    mostrarVentana()
