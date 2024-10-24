import cv2
import time

def detect_motion(cap, min_area=500):
    """
    Phát hiện chuyển động bằng cách so sánh sự thay đổi giữa khung hình hiện tại và khung hình trước.
    """
    ret, frame1 = cap.read()
    if not ret:
        return False

    ret, frame2 = cap.read()
    if not ret:
        return False

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    diff = cv2.absdiff(gray1, gray2)

    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            return True

    return False
