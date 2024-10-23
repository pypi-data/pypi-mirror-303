import cv2
import numpy as np

drawing = False
def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt, img_orig, img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        top_left_pt, bottom_right_pt = (x_init, y_init), (x, y)
        img[y_init:y, x_init:x] = 255 - img_orig[y_init:y, x_init:x]
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt, bottom_right_pt = (x_init, y_init), (x, y)
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 2)
        rect_final = (x_init, y_init, x - x_init, y - y_init)
        remove_object(img_orig, rect_final)

def compute_energy_matrix(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    return cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

def compute_energy_matrix_modified(img, rect_roi):
    energy_matrix = compute_energy_matrix(img)
    x, y, w, h = rect_roi
    energy_matrix[y:y + h, x:x + w] = 0
    return energy_matrix

def find_vertical_seam(energy):
    """Encuentra la costura vertical de menor energía en la matriz de energía."""
    rows, cols = energy.shape

    # Matriz para guardar las energías acumuladas
    cumulative_energy = np.zeros((rows, cols), dtype=np.float64)
    # Matriz para guardar la posición de la costura
    edge_to = np.zeros((rows, cols), dtype=np.int32)

    # Inicializamos la primera fila con la misma energía
    cumulative_energy[0, :] = energy[0, :]

    # Rellenar las matrices cumulative_energy y edge_to
    for i in range(1, rows):
        for j in range(cols):
            # Verificar las posiciones vecinas válidas para evitar out-of-bounds
            left = cumulative_energy[i - 1, j - 1] if j > 0 else np.inf
            up = cumulative_energy[i - 1, j]
            right = cumulative_energy[i - 1, j + 1] if j < cols - 1 else np.inf

            # Elegir la mínima energía acumulada de los vecinos
            min_energy = min(left, up, right)

            # Guardar la energía acumulada mínima
            cumulative_energy[i, j] = energy[i, j] + min_energy

            # Guardar la posición del vecino con menor energía
            if min_energy == left:
                edge_to[i, j] = j - 1
            elif min_energy == up:
                edge_to[i, j] = j
            else:
                edge_to[i, j] = j + 1

    # Inicializar el arreglo para la costura vertical de menor energía
    seam = np.zeros(rows, dtype=np.int32)

    # Encontrar la posición mínima en la última fila
    seam[-1] = np.argmin(cumulative_energy[-1, :])

    # Recorrer hacia atrás para reconstruir la costura
    for i in range(rows - 2, -1, -1):
        seam[i] = edge_to[i + 1, seam[i + 1]]

    return seam

def remove_vertical_seam(img, seam):
    rows, cols = img.shape[:2]
    new_img = np.zeros((rows, cols - 1, 3), dtype=np.uint8)
    for row in range(rows):
        new_img[row, :, :] = np.delete(img[row, :, :], seam[row], axis=0)
    return new_img

def add_vertical_seam(img, seam):
    rows, cols = img.shape[:2]
    new_img = np.zeros((rows, cols + 1, 3), dtype=np.uint8)
    for row in range(rows):
        col = seam[row]
        new_img[row, :col, :] = img[row, :col, :]
        new_img[row, col + 1:, :] = img[row, col:, :]
        new_img[row, col, :] = (img[row, col - 1, :] + img[row, col, :]) // 2
    return new_img

def remove_object(img, rect_roi):
    num_seams = rect_roi[2] + 10
    energy = compute_energy_matrix_modified(img, rect_roi)
    for _ in range(num_seams):
        seam = find_vertical_seam(img, energy)
        img = remove_vertical_seam(img, seam)
        energy = compute_energy_matrix(img)
    return img

def remove_element(file_path):
    global img, img_orig
    img_input = cv2.imread(file_path)
    img = np.copy(img_input)
    img_orig = np.copy(img_input)

    cv2.namedWindow('Input')
    cv2.setMouseCallback('Input', draw_rectangle)
    print('Draw a rectangle around the object to be removed. Press ESC to finish.')

    while True:
        cv2.imshow('Input', img)
        if cv2.waitKey(10) == 27:  # ESC key to exit
            break

    cv2.destroyAllWindows()

    img_seam = np.copy(img)  # Image after seam carving
    img_output = add_vertical_seam(img_seam, find_vertical_seam(img, compute_energy_matrix(img)))

    return img_input, img_seam, img_output
