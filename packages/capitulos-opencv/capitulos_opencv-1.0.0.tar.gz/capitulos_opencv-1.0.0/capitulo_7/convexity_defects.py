import cv2
import numpy as np

def get_all_contours(img):
    """Extrae todos los contornos de la imagen."""
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def detect_convexity_defects(image_path):
    """Detecta defectos de convexidad en los contornos y retorna la imagen procesada."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"No se pudo cargar la imagen: {image_path}")

    # Iterar sobre los contornos y detectar defectos de convexidad
    for contour in get_all_contours(img):
        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)

        if defects is None:
            continue  # Omitimos contornos sin defectos

        # Dibujar los defectos de convexidad
        for i in range(defects.shape[0]):
            start_defect, end_defect, far_defect, _ = defects[i, 0]
            start = tuple(contour[start_defect][0])
            end = tuple(contour[end_defect][0])
            far = tuple(contour[far_defect][0])

            cv2.circle(img, far, 5, [128, 0, 0], -1)  # Dibujar un círculo en el defecto
            cv2.drawContours(img, [contour], -1, color=(0, 0, 0), thickness=3)  # Dibujar el contorno

    return img  # Devolver la imagen procesada
