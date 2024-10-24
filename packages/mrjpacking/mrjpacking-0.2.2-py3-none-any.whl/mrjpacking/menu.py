import shutil
import pyfiglet
# from colorama import Fore, Style

def display_menu():
    try:
        # Tạo khung cho menu
        border = "*" * 30
        print("\n" + border)
        print("Chọn một công cụ:")
        print("1. Đóng hàng")
        print("2. Tìm mã vận đơn")
        print("3. Xóa đơn quá 30 ngày")
        print("4. Đơn quét được trong ngày")
        # print("5. Xóa bộ nhớ đệm")
        print("5. Bấm số 5 để thoát chương trình")
        print(border)

        choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
        return choice
    except KeyboardInterrupt:
        print()
    

def print_title():
    # Lấy chiều rộng terminal
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    # Tạo tiêu đề "TIKTOK SHOP" dưới dạng ASCII art
    ascii_title = pyfiglet.figlet_format("TIKTOK SHOP")

    # Chia từng dòng của tiêu đề để căn giữa từng dòng một
    ascii_lines = ascii_title.splitlines()

    # Tạo dòng viền ngang với chiều rộng của terminal
    border_line = '*' * terminal_width

    # In viền trên
    print(border_line)

    # In từng dòng của ASCII art và căn giữa
    for line in ascii_lines:
        # Tính toán khoảng trắng để căn giữa dòng
        padding = (terminal_width - len(line)) // 2
        print(' ' * padding + line)

    # In viền dưới
    print(border_line)

    # Thêm chữ kí ở góc phải
    signature = "Justin Nguyen"
    # signature = Fore.RED + "Justin Nguyen" + Style.RESET_ALL
    signature_start = terminal_width - len(signature)
    print(' ' * signature_start + signature)


