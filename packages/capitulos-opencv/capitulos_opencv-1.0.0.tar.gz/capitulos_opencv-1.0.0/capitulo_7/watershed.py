import numpy as np
import cv2

def apply_watershed(image_path):
    """Aplica el algoritmo Watershed para segmentar la imagen."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"No se pudo cargar la imagen: {image_path}")

    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicamos un umbral binario inverso con Otsu
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Eliminación de ruido mediante apertura morfológica
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)

    # Área segura de fondo
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Área segura de primer plano
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Encontrar región desconocida (resta entre fondo y primer plano)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Etiquetado de los componentes conectados
    _, markers = cv2.connectedComponents(sure_fg)

    # Sumamos 1 a las etiquetas para que el fondo seguro no sea 0, sino 1
    markers = markers + 1

    # Marcamos las regiones desconocidas con 0
    markers[unknown == 255] = 0

    # Aplicamos el algoritmo watershed
    markers = cv2.watershed(img, markers)

    # Dibujamos las fronteras encontradas
    img[markers == -1] = [255, 255, 255]

    return img, sure_bg, sure_fg, thresh  # Retornamos las imágenes para mostrarlas
