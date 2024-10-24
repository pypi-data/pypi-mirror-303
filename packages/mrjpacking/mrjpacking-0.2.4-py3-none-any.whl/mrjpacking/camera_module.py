import cv2

def init_camera():
    try:
        # Khởi tạo camera với chỉ số 0 (thường là camera mặc định)
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Dùng CAP_DSHOW để ngăn lỗi xuất hiện trên Windows
        if not cap.isOpened():
            raise Exception("Không thể mở camera, kiểm tra lại kết nối hoặc thiết bị.")
        return cap
    except Exception as e:
        print(f"\nLỗi: {e}")  # In ra lỗi tùy chỉnh khi không tìm thấy camera
        return None  # Trả về None nếu không thể khởi tạo camera

def release_camera(cap):
    cap.release()

def read_frame(cap):
    ret, frame = cap.read()
    return ret, frame
