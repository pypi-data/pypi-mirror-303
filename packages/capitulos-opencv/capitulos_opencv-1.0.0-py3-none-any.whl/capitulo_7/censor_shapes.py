import cv2
import numpy as np

def get_all_contours(img):
    """Extraer todos los contornos de la imagen."""
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def censor_shapes_in_image(image_path):
    """Aplica la censura de formas y retorna dos versiones de la imagen."""
    img = cv2.imread(image_path)
    img_orig = np.copy(img)
    input_contours = get_all_contours(img)
    solidity_values = []

    # Calcular el factor de solidez para cada contorno
    for contour in input_contours:
        area_contour = cv2.contourArea(contour)
        convex_hull = cv2.convexHull(contour)
        area_hull = cv2.contourArea(convex_hull)

        # Verificar si el área del convex hull es mayor que 0
        if area_hull > 0:
            solidity = float(area_contour) / area_hull
            solidity_values.append(solidity)
        else:
            print("Advertencia: Contorno con área de convex hull 0, se omitirá.")

    # Verificar si tenemos suficientes contornos para agrupar
    if len(solidity_values) < 2:
        raise ValueError("No se encontraron suficientes contornos válidos para agrupar.")

    # Clustering usando KMeans
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    solidity_values = np.array(solidity_values).reshape((len(solidity_values), 1)).astype('float32')
    _, labels, centers = cv2.kmeans(solidity_values, 2, None, criteria, 10, flags)

    closest_class = np.argmin(centers)
    output_contours = [input_contours[i] for i, label in enumerate(labels) if label == closest_class]

    # Dibujar los contornos censurados
    cv2.drawContours(img, output_contours, -1, (0, 0, 0), 3)

    # Aplicar censura en el original
    for contour in output_contours:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img_orig, [box], 0, (0, 0, 0), -1)

    return img, img_orig  # Retornamos ambas versiones
