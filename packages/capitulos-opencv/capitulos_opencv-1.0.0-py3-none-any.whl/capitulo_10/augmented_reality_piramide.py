# archivo: augmented_reality_tracker.py

import cv2
import numpy as np
from . import pose_estimation

class Tracker:
    def __init__(self, capId=0, scaling_factor=0.8, win_name='Augmented Reality'):
        self.cap = cv2.VideoCapture(capId)
        self.rect = None
        self.win_name = win_name
        self.scaling_factor = scaling_factor
        self.tracker = pose_estimation.PoseEstimator()

        ret, frame = self.cap.read()
        self.frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        self.roi_selector = pose_estimation.ROISelector(win_name, self.frame, self.set_rect)
        self.overlay_vertices = np.float32([[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0], [0.5, 0.5, 4]])
        self.overlay_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4)]
        self.color_base = (0, 255, 0)
        self.color_lines = (0, 0, 0)

    def set_rect(self, rect):
        self.rect = rect
        self.tracker.add_target(self.frame, rect)

    def start(self):
        paused = False
        while True:
            if not paused or self.frame is None:
                ret, frame = self.cap.read()
                frame = cv2.resize(frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA)
                if not ret:
                    break

                self.frame = frame.copy()

            img = self.frame.copy()
            if not paused:
                tracked = self.tracker.track_target(self.frame)
                for item in tracked:
                    cv2.polylines(img, [np.int32(item.quad)], True, self.color_lines, 2)
                    for (x, y) in np.int32(item.points_cur):
                        cv2.circle(img, (x, y), 2, self.color_lines)

                    self.overlay_graphics(img, item)

            self.roi_selector.draw_rect(img, self.rect)
            cv2.imshow(self.win_name, img)
            ch = cv2.waitKey(1)
            if ch == ord(' '):
                paused = not paused
            if ch == ord('c'):
                self.tracker.clear_targets()
            if ch == 27:  # ESC key
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def overlay_graphics(self, img, tracked):
        x_start, y_start, x_end, y_end = tracked.target.rect
        quad_3d = np.float32([[x_start, y_start, 0], [x_end, y_start, 0], [x_end, y_end, 0], [x_start, y_end, 0]])
        h, w = img.shape[:2]
        K = np.float64([[w, 0, 0.5 * (w - 1)], [0, w, 0.5 * (h - 1)], [0, 0, 1.0]])
        dist_coef = np.zeros(4)

        ret, rvec, tvec = cv2.solvePnP(quad_3d, tracked.quad, K, dist_coef)
        verts = self.overlay_vertices * [(x_end - x_start), (y_end - y_start), -(x_end - x_start) * 0.3] + (x_start, y_start, 0)
        verts = cv2.projectPoints(verts, rvec, tvec, K, dist_coef)[0].reshape(-1, 2)

        verts_floor = np.int32(verts).reshape(-1, 2)
        cv2.drawContours(img, [verts_floor[:4]], -1, self.color_base, -3)

        for i, j in self.overlay_edges:
            pt1, pt2 = verts[i], verts[j]
            cv2.line(img, tuple(pt1.astype(int)), tuple(pt2.astype(int)), self.color_lines, 2)

# Función para inicializar y ejecutar el rastreador
def ejecutar_tracker():
    tracker = Tracker()
    tracker.start()
