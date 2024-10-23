import cv2
import numpy as np

def background_subtraction_video(scaling_factor=0.5, camera_index=0):
    """Aplica sustracción de fondo utilizando un video en tiempo real."""
    # Inicializamos la captura de video
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise ValueError(f"No se pudo acceder a la cámara en el índice {camera_index}")

    # Creamos el objeto de sustracción de fondo
    bg_subtractor = cv2.bgsegm.createBackgroundSubtractorGMG()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    while True:
        # Leemos el cuadro actual y lo redimensionamos
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame del video.")
            break

        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        # Aplicamos la sustracción de fondo al frame
        mask = bg_subtractor.apply(frame)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Mostramos los frames de entrada y la máscara de objetos en movimiento
        cv2.imshow('Input Frame', frame)
        cv2.imshow('Moving Objects', mask)

        # Verificamos si el usuario presiona la tecla ESC
        if cv2.waitKey(30) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
