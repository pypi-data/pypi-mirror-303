import cv2
import numpy as np

def overlay_vertical_seam(img, seam):
    img_seam_overlay = np.copy(img)
    x_coords, y_coords = np.transpose([(i,int(j)) for i,j in enumerate(seam)])
    img_seam_overlay[x_coords, y_coords] = (0,255,0)
    return img_seam_overlay

def compute_energy_matrix(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    return cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

def find_vertical_seam(img, energy):
    rows, cols = img.shape[:2]
    seam = np.zeros(rows)
    dist_to = np.zeros((rows, cols)) + float('inf')
    dist_to[0,:] = np.zeros(cols)
    edge_to = np.zeros((rows, cols))

    for row in range(rows-1):
        for col in range(cols):
            if col != 0 and dist_to[row+1, col-1] > dist_to[row, col] + energy[row+1, col-1]:
                dist_to[row+1, col-1] = dist_to[row, col] + energy[row+1, col-1]
                edge_to[row+1, col-1] = 1
            if dist_to[row+1, col] > dist_to[row, col] + energy[row+1, col]:
                dist_to[row+1, col] = dist_to[row, col] + energy[row+1, col]
                edge_to[row+1, col] = 0
            if col != cols-1 and dist_to[row+1, col+1] > dist_to[row, col] + energy[row+1, col+1]:
                dist_to[row+1, col+1] = dist_to[row, col] + energy[row+1, col+1]
                edge_to[row+1, col+1] = -1

    seam[rows-1] = np.argmin(dist_to[rows-1, :])
    for i in reversed(range(rows-1)):
        seam[i] = seam[i+1] + edge_to[i+1, int(seam[i+1])]

    return seam

def remove_vertical_seam(img, seam):
    rows, cols = img.shape[:2]
    for row in range(rows):
        for col in range(int(seam[row]), cols-1):
            img[row, col] = img[row, col+1]
    return img[:, :-1]

def reduce_image(img_path, num_seams):
    img_input = cv2.imread(img_path)
    img = np.copy(img_input)
    img_overlay_seam = np.copy(img_input)

    for i in range(num_seams):
        energy = compute_energy_matrix(img)
        seam = find_vertical_seam(img, energy)
        img_overlay_seam = overlay_vertical_seam(img_overlay_seam, seam)
        img = remove_vertical_seam(img, seam)
        print('Number of seams removed =', i+1)

    return img_input, img_overlay_seam, img