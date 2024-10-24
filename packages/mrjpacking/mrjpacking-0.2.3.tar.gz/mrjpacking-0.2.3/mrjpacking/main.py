import cv2
import time
from . import camera_module as camera
from . import file_management as file_manager
from . import qr_scanner as qr
from . import sound_module as sound
from . import overlay_module as overlay
from . import menu
from . import tracking_module as search
from . import motion_detector
from . import cache_cleaner
from . import display_tracking_id_on_frame
from .order_counter import count_orders_today


def main():
    try:
        # Chọn thư mục lưu trữ
        data_dir = file_manager.select_data_directory()  # Sử dụng hàm từ module file_management
        cache_dir = "__pycache__"

        # Hiển thị menu và xử lý lựa chọn
        while True:
            choice = menu.display_menu()

            if choice == '1':
                # Bắt đầu tiến trình đóng gói bình thường
                cap = camera.init_camera()
                # Kiểm tra nếu không khởi tạo được camera
                if cap is None:
                    continue  # Quay lại menu nếu không tìm thấy camera

                recording = False
                current_tracking_id = None
                writer = None
                last_motion_time = None

                while True:
                    ret, frame = camera.read_frame(cap)
                    if not ret:
                        break

                    # Hiển thị thời gian lên khung hình
                    frame_with_timestamp = overlay.overlay_datetime(frame.copy())

                    # Vẽ khung màu xanh lá cây lên khung hình có thời gian
                    frame_with_timestamp_and_green_frame = overlay.draw_green_frame(frame_with_timestamp)

                    frame_with_timestamp = overlay.overlay_datetime(frame.copy())
                    frame = overlay.draw_green_frame(frame)

                    # Quét mã QR từ khung hình (kiểm tra trước khi truyền vào hàm)
                    if frame_with_timestamp_and_green_frame is not None:
                        label_text = qr.capture_label(frame)
                        if label_text:
                            if not current_tracking_id or current_tracking_id != label_text:
                                print(f"Quét thành công đơn hàng: {label_text}")
                                if writer:
                                    writer.release()
                                    recording = False

                                # Sử dụng hàm lưu trữ từ module file_management
                                tracking_dir = file_manager.create_tracking_directory(data_dir, label_text)

                                # Lưu hình ảnh và video vào thư mục
                                image_filename, video_filename, writer = file_manager.save_files(tracking_dir, frame_with_timestamp, frame)
                                recording = True
                                current_tracking_id = label_text

                                last_motion_time = time.time()

                                sound.play_success_sound()
                    else:
                        print("Lỗi: Khung hình không hợp lệ.")

                    # Hiển thị mã vận đơn nếu đã quét thành công
                    if current_tracking_id:
                        frame_with_timestamp_and_green_frame = display_tracking_id_on_frame.display_tracking_id_on_frame(frame_with_timestamp_and_green_frame, current_tracking_id)

                    if recording:     
                        # Tạo một khung hình chỉ với ngày giờ và mã vận đơn, không có khung xanh
                        frame_for_recording = frame_with_timestamp.copy()  # Sử dụng khung hình gốc
                        frame_for_recording = overlay.overlay_datetime(frame_for_recording)  # Thêm ngày giờ vào khung hình
                        if current_tracking_id:
                            frame_for_recording = display_tracking_id_on_frame.display_tracking_id_on_frame(frame_for_recording, current_tracking_id)  # Thêm mã vận đơn

                        writer.write(frame_for_recording)  # Ghi khung hình vào video

                        # Kiểm tra phát hiện chuyển động 
                        if motion_detector.detect_motion(cap):
                            last_motion_time = time.time()

                        else:
                            # Kiểm tra nếu không phát hiện chuyển động quá 45s
                            if last_motion_time is not None and time.time() - last_motion_time > 45:
                                print("\nKhông phát hiện chuyển động trong 45s, dừng ghi hình.")
                                writer.release()
                                break

                    cv2.imshow('E-commerce Packing Process', frame_with_timestamp_and_green_frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                if writer:
                    writer.release()
                camera.release_camera(cap)
                cv2.destroyAllWindows()
                cache_cleaner.clear_cache(cache_dir)

            elif choice == '2':
                # Tìm kiếm mã vận đơn
                search.search_tracking_id(data_dir)

            elif choice == '3':
                # Xóa những đơn đã quá 30 ngày
                file_manager.ask_to_delete_old_folders(data_dir)

            elif choice == '4':
                # Đếm tổng đơn trong ngày
                count = count_orders_today(data_dir)
                print(f"\nTổng số đơn được quét trong ngày: {count}")

            # elif choice == "5":
            #     # Xóa bộ nhớ đệm
            #     cache_cleaner.clear_cache(cache_dir)

            elif choice == '5':
                # Thoát chương trình
                print("Hẹn gặp lại!!!")
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    except KeyboardInterrupt:
        print("\nDừng chương trình.")

if __name__ == "__main__":
     main()