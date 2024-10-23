import cv2
import numpy as np

def get_all_contours(img):
    """Extrae todos los contornos de la imagen."""
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def smoothen_contours(image_path, epsilon_factor=0.02):
    """Suaviza los contornos encontrados en la imagen."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"No se pudo cargar la imagen: {image_path}")

    contours = get_all_contours(img)

    # Iteramos sobre cada contorno y aplicamos la aproximación poligonal
    for contour in contours:
        epsilon = epsilon_factor * cv2.arcLength(contour, True)  # Factor de suavizado
        approx = cv2.approxPolyDP(contour, epsilon, True)  # Aproximación poligonal

        # Dibujamos los contornos suavizados sobre la imagen
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

    return img  # Devolvemos la imagen procesada
