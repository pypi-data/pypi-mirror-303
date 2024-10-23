import cv2
import numpy as np

def segment_image(file_path):
    """Segmenta la imagen usando el algoritmo GrabCut."""
    # Cargar la imagen desde el archivo
    img_orig = cv2.imread(file_path)
    img = img_orig.copy()

    # Definir un rectángulo alrededor del área a segmentar (ajustar según necesites)
    rect = (50, 50, img.shape[1] - 100, img.shape[0] - 100)

    # Inicializar máscaras y modelos de fondo/primer plano
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Ejecutar el algoritmo GrabCut
    cv2.grabCut(img_orig, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Crear la máscara final y aplicarla a la imagen original
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img_output = img_orig * mask2[:, :, np.newaxis]

    return img_output
