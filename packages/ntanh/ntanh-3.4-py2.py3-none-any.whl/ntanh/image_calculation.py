import cv2
import numpy as np

from ntanh.yolo_boxes import YoloCrop


def calculate_luminance(image, Lumen_coefficient=1.0):
    """
    Hàm tính độ sáng trung bình từ một ảnh đầu vào.

    :param image_path: Đường dẫn tới ảnh.
    :return: Độ sáng trung bình.
    """

    # Chuyển đổi ảnh sang không gian màu YUV
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # Kênh Y chứa độ sáng
    luminance_channel = yuv_image[:, :, 0]

    # Tính độ sáng trung bình
    average_luminance = np.mean(luminance_channel)

    return average_luminance * Lumen_coefficient


if __name__ == "__main__":
    RUN=1
    # Lumen calculation: ---------------------------------------------------------------------
    if RUN==1:
        coverYolo_str = "0 0.496094 0.772135 0.527344 0.453125"

        # Ví dụ
        image_path = (
            r"H:\DATA\Cam360SmartGate\Training_data_from_DUY\_Train\11_10\6\6_1\frame000000.jpg"
        )
        # Đọc ảnh
        image = cv2.imread(image_path)

        image = YoloCrop(image, coverYolo_str, Delta_Expand=0)
        luminance = calculate_luminance(image)        
        print(f"{luminance:0.4f} (luminance)")

        cv2.imshow("Before", image)
        # Ví dụ
        image_path = r"F:\Training_data_from_DUY\_Train\11_10\6\6_1\frame000000.jpg"
        # Đọc ảnh
        image = cv2.imread(image_path)
        image = YoloCrop(image, coverYolo_str, Delta_Expand=0)
        luminance = calculate_luminance(image)
        print(f"After {luminance:0.4f} (lumen)")
        cv2.imshow("after", image)
        cv2.waitKey(0)
    # End Lumen calculation: ---------------------------------------------------------------------
    if RUN==2:
        pass
