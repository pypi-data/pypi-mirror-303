import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from . import image_segmentation  # Importamos la lógica de segmentación desde otro archivo
from . import censor_shapes
from . import convexity_defects
from . import smoothen_contour_polygon
from . import watershed

def cargar_imagen(metodo):
    """Cargar una imagen desde un archivo y ejecutar el método indicado."""
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            if metodo == "segment":  # Ejecutamos el método de segmentación
                img_output = image_segmentation.segment_image(file_path)
                mostrar_imagen(img_output, "Imagen Segmentada")
            elif metodo == "censor_shapes":
                censored_img, original_with_boxes = censor_shapes.censor_shapes_in_image(file_path)
                mostrar_imagen(censored_img, "Imagen Censurada")
                mostrar_imagen(original_with_boxes, "Imagen con Contornos Censurados")
            elif metodo == "convexity_defects":
                img_defects = convexity_defects.detect_convexity_defects(file_path)
                mostrar_imagen(img_defects, "Defectos de Convexidad")
            elif metodo == "smoothen_contours":
                img_smooth = smoothen_contour_polygon.smoothen_contours(file_path)
                mostrar_imagen(img_smooth, "Contornos Suavizados")
            elif metodo == "watershed":
                img_result, bg, fg, thresh = watershed.apply_watershed(file_path)
                mostrar_imagen(img_result, "Resultado Watershed")
                mostrar_imagen(bg, "Fondo Seguro")
                mostrar_imagen(fg, "Primer Plano Seguro")
                mostrar_imagen(thresh, "Umbral")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def mostrar_imagen(img, title):
    """Mostrar la imagen en una nueva ventana."""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im_pil)

    top = tk.Toplevel()
    top.title(title)
    lbl_img = tk.Label(top, image=imgtk)
    lbl_img.image = imgtk  # Mantener referencia para evitar recolección de basura
    lbl_img.pack()

def mostrarVentana():
    """Mostrar la ventana principal de la aplicación."""
    ventana = tk.Tk()
    ventana.title("Segmentación de Imagen")

    btn_segment = tk.Button(ventana, text="Segmentar Imagen", command=lambda: cargar_imagen("segment"))
    btn_segment.pack(pady=10)
    btn_segment = tk.Button(ventana, text="Censurar Formas", command=lambda: cargar_imagen("censor_shapes"))
    btn_segment.pack(pady=10)
    btn_segment = tk.Button(ventana, text="Defectos de Convexidad", command=lambda: cargar_imagen("convexity_defects"))
    btn_segment.pack(pady=10)
    btn_segment = tk.Button(ventana, text="Contornos suavizados", command=lambda: cargar_imagen("smoothen_contours"))
    btn_segment.pack(pady=10)
    btn_segment = tk.Button(ventana, text="Cuenca", command=lambda: cargar_imagen("watershed"))
    btn_segment.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    mostrarVentana()
