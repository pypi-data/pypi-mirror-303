import cv2
from .constants import frame_width, frame_height

def capture_label(frame):
    detector = cv2.QRCodeDetector()
    data, vertices, _ = detector.detectAndDecode(frame)
    if vertices is not None and data:
        vertices = vertices.astype(int)
        (x, y, w, h) = cv2.boundingRect(vertices)
        if check_within_frame((x, y, w, h)):
            return data
    return None

def check_within_frame(box):
    (x, y, w, h) = box
    return x >= 0 and y >= 0 and (x + w) <= frame_width and (y + h) <= frame_height
