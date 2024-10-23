# Archivo: gui_seam_carving.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from . import expand_image_by_seam_carving
from . import reduce_image_by_seam_carving
from . import remove_element_by_seam_carving
import numpy as np
# Asegúrate de que este archivo existe y está en el mismo directorio

def cargar_imagen(metodo):
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            if metodo == "expand":
                num_seams = 10  # Definir el número de seams que quieras añadir
                img_input, img_seam, img_output = expand_image_by_seam_carving.expand_image(file_path, num_seams)
                mostrar_imagen(img_output, "Imagen Expandida")
            # Comentamos las otras opciones por ahora, ya que no están implementadas
            elif metodo == "reduce":
                num_seams = 10
                img_input, img_seam, img_output = reduce_image_by_seam_carving.reduce_image(file_path, num_seams)
                mostrar_imagen(img_output, "Imagen Reducida")
            elif metodo == "remove":
                img_input, img_seam, img_output = remove_element_by_seam_carving.remove_element(file_path)

            mostrar_imagen(img_seam, "Imagen con Seam Overlay")

        except Exception as e:
            messagebox.showerror("Error", str(e))

def mostrar_imagen(img, title):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im_pil)
    
    top = tk.Toplevel()
    top.title(title)
    lbl_img = tk.Label(top, image=imgtk)
    lbl_img.image = imgtk  # Mantener referencia para evitar que sea eliminado por el garbage collector
    lbl_img.pack()

def mostrarVentana():
    ventana = tk.Tk()  # Cambiamos Toplevel por Tk para la ventana principal
    ventana.title("Procesar Imagen con Seam Carving")
    
    btn_expand = tk.Button(ventana, text="Expandir Imagen", command=lambda: cargar_imagen("expand"))
    btn_reduce = tk.Button(ventana, text="Reducir Imagen", command=lambda: cargar_imagen("reduce"))
    btn_remove = tk.Button(ventana, text="Eliminar Elemento", command=lambda: cargar_imagen("remove"))
    
    btn_expand.pack(pady=10)
    btn_reduce.pack(pady=10)
    btn_remove.pack(pady=10)
    
    ventana.mainloop()

if __name__ == "__main__":
    mostrarVentana()