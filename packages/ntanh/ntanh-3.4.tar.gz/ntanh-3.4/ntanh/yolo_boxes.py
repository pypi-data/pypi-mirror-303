def xyxy_to_yolo_str(obj_class, x1, y1, x2, y2, imH, imW):
    # Tọa độ trung tâm
    x_center = (x1 + x2) / 2 / imW
    y_center = (y1 + y2) / 2 / imH
    # Chiều rộng và chiều cao
    width = (x2 - x1) / imW
    height = (y2 - y1) / imH

    # Tạo chuỗi YOLO: "class x_center y_center width height"
    yolo_str = f"{obj_class} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

    return yolo_str


def yolo_str_to_xyxy(yolo_str, imH, imW):
    """Chuyển đổi yolo string sang box xyxy

    x1,y1,x2,y2 = ntanh.yolo_str_to_xyxy(yolo_str, imH, imW)

    Args:
        yolo_str (string with id): '0 0.195312 0.416667 0.234375 0.416667'
        imH (int/float): Cao ảnh
        imW (int/float): Rộng ảnh

    Returns:
        int: objclass, x_min, y_min, x_max, y_max hoặc id, x1, y1, x2, y2
    """
    # Tách chuỗi YOLO thành các giá trị
    yolo_data = yolo_str.split()
    obj_class = yolo_data[0]  # Lớp đối tượng (class)
    x_center = float(yolo_data[1])
    y_center = float(yolo_data[2])
    width = float(yolo_data[3])
    height = float(yolo_data[4])

    # Chuyển từ YOLO sang tọa độ góc
    x_min = (x_center - width / 2) * imW
    x_max = (x_center + width / 2) * imW
    y_min = (y_center - height / 2) * imH
    y_max = (y_center + height / 2) * imH

    return int(obj_class), int(x_min), int(y_min), int(x_max), int(y_max)


def YoloCrop(image, yolo_str="0 0.496094 0.772135 0.527344 0.453125", Delta_Expand=0):
    imH, imW = image.shape[:2]
    id, x1, y1, x2, y2 = yolo_str_to_xyxy(yolo_str=yolo_str, imH=imH, imW=imW)
    d = Delta_Expand
    y1, y2,  x1, x2= y1-d,y2+d, x1-d,x2+d
    image = image[y1:y2, x1:x2]
    return image


if __name__ == "__main__":
    # Convert bbox to Yolo và ngược lại:
    class img:
        shape = (600, 800, 3)

    x1 = 50
    y1 = 100
    x2 = 200
    y2 = 300
    imH, imW = img.shape[:2]
    obj_class = 0

    yolo_str = xyxy_to_yolo_str(obj_class, x1, y1, x2, y2, imH, imW)
    print(yolo_str)  # "0 0.156250 0.333333 0.187500 0.333333"

    # yolo_str = "0 0.195312 0.416667 0.234375 0.416667"
    yolo_str = "0 0.156250 0.333333 0.187500 0.333333"
    imH, imW = img.shape[:2]

    obj_class, x1, y1, x2, y2 = yolo_str_to_xyxy(yolo_str, imH, imW)
    print(obj_class, x1, y1, x2, y2)  # 0 62 125 249 375
