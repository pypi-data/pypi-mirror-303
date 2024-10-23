import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from . import background_subtraction_GMG
from . import background_subtraction_MOG
from . import colorspace_tracking
from . import object_tracker
from capitulo_7.watershed import apply_watershed
from . import feature_tracking

def ejecutar_subtema(subtema):
    """Ejecuta el subtema seleccionado."""
    try:
        if subtema == "background_subtraction_GMG":
            background_subtraction_GMG.background_subtraction_video(scaling_factor=0.5)
        elif subtema == "background_subtraction_MOG":
            background_subtraction_MOG.background_subtraction_video(scaling_factor=0.5)
        elif subtema=="color_detector":
            colorspace_tracking.color_detector()
        elif subtema=="feature_tracking":
            feature_tracking.track_features()
        elif subtema=="object_tracker":
            object_tracker.run_object_tracker()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_imagen(img, title):
    """Muestra una imagen en una nueva ventana."""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im_pil)

    top = tk.Toplevel()
    top.title(title)
    lbl_img = tk.Label(top, image=imgtk)
    lbl_img.image = imgtk  # Referencia para evitar garbage collection
    lbl_img.pack()

def mostrarVentana():
    """Muestra la ventana principal con los botones de subtemas."""
    ventana = tk.Tk()
    ventana.title("Ejecutar Subtemas")

    btn_bg_subtraction = tk.Button(ventana, text="Background Subtraction GMG", 
                                    command=lambda: ejecutar_subtema("background_subtraction_GMG"))
    btn_mog_subtraction = tk.Button(ventana, text="Background Subtraction MOG", 
                                command=lambda: ejecutar_subtema("background_subtraction_MOG"))
    btn_colorspace = tk.Button(ventana, text="Color Detector", 
                                command=lambda: ejecutar_subtema("color_detector"))
    btn_track_features = tk.Button(ventana, text="Treack features", 
                                command=lambda: ejecutar_subtema("feature_tracking"))
    btn_object_tracker = tk.Button(ventana, text="Object Tracker", 
                                command=lambda: ejecutar_subtema("object_tracker"))

    btn_bg_subtraction.pack(pady=10)
    btn_mog_subtraction.pack(pady=10)
    btn_colorspace.pack(pady=10)
    btn_track_features.pack(pady=10)
    btn_object_tracker.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    mostrarVentana()
