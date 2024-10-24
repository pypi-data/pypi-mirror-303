from setuptools import setup, find_packages

setup(
    name='mrjpacking',
    version='0.2.4',
    description='Theo dõi đóng gói sản phẩm sàn thương mại điện tử',
    long_description=open('README.md', encoding='utf-8').read(),
    author='Justin Nguyễn',
    author_email='duchuy_1997@hotmail.com',
    packages=find_packages(),
    install_requires=[  # Danh sách các thư viện phụ thuộc
        'pyfiglet',
        'colorama',
        'keyboard',
        'numpy',
        'opencv-python',
        'pygame',
        'pyzbar',
        'timedelta'
    ],
    python_requires='>=3.6',  # Phiên bản Python yêu cầu
    entry_points={
        'console_scripts': [
            'mrjpacking=mrjpacking.main:main',  # Thay 'main:main' bằng tên file và hàm khởi động của bạn
        ],
    },
)