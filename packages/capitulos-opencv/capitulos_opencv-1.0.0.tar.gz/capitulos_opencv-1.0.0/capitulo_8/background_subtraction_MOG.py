import cv2
import numpy as np

def background_subtraction_video(scaling_factor=0.5):
    """Función para realizar la sustracción de fondo con MOG2."""
    # Inicializa el objeto de captura de video
    cap = cv2.VideoCapture(0)  # Cambia el índice si no detecta la cámara

    if not cap.isOpened():
        print("No se puede acceder a la cámara.")
        return

    # Crea el objeto del sustractor de fondo
    bgSubtractor = cv2.createBackgroundSubtractorMOG2()

    history = 100  # Factor para controlar el rate de aprendizaje

    while True:
        # Captura el frame redimensionado
        frame = get_frame(cap, scaling_factor)
        if frame is None:
            break

        # Aplica la sustracción de fondo al frame
        mask = bgSubtractor.apply(frame, learningRate=1.0/history)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Muestra el resultado
        cv2.imshow('Input Frame', frame)
        cv2.imshow('Moving Objects MOG', mask & frame)

        # Salir al presionar ESC
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def get_frame(cap, scaling_factor=0.5):
    """Captura y redimensiona el frame."""
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame.")
        return None
    return cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)