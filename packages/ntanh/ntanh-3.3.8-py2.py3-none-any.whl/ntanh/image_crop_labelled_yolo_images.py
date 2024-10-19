import os
from PIL import Image


def yolo_str_to_bbox(yolo_str, imH, imW):
    # Hàm chuyển từ tọa độ YOLO về (x_min, y_min, x_max, y_max)
    obj_class, x_center, y_center, width, height = map(float, yolo_str.split())
    x_min = int((x_center - width / 2) * imW)
    y_min = int((y_center - height / 2) * imH)
    x_max = int((x_center + width / 2) * imW)
    y_max = int((y_center + height / 2) * imH)
    return obj_class, x_min, y_min, x_max, y_max


def crop_image(image_path, yolo_str):
    # Mở ảnh và lấy kích thước ảnh
    img = Image.open(image_path)
    imW, imH = img.size

    # Lấy tọa độ crop từ YOLO
    _, x_min, y_min, x_max, y_max = yolo_str_to_bbox(yolo_str, imH, imW)

    # Crop ảnh
    cropped_img = img.crop((x_min, y_min, x_max, y_max))
    return cropped_img, imW, imH


def update_labels(
    label_path, x_min_crop, y_min_crop, new_imW, new_imH, old_imW, old_imH
):
    # Cập nhật file nhãn dựa trên ảnh đã crop
    new_labels = []
    with open(label_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            obj_class, x_center, y_center, width, height = map(float, line.split())

            # Tính tọa độ gốc của bounding box (theo ảnh ban đầu)
            old_x_min = (x_center - width / 2) * old_imW
            old_y_min = (y_center - height / 2) * old_imH
            old_x_max = (x_center + width / 2) * old_imW
            old_y_max = (y_center + height / 2) * old_imH

            # Điều chỉnh bounding box theo vùng đã crop
            new_x_min = max(0, old_x_min - x_min_crop)
            new_y_min = max(0, old_y_min - y_min_crop)
            new_x_max = min(new_imW, old_x_max - x_min_crop)
            new_y_max = min(new_imH, old_y_max - y_min_crop)

            # Bỏ qua các đối tượng không nằm trong vùng crop
            # if new_x_min < new_x_max and new_y_min < new_y_max:
            if 1:
                new_x_center = (new_x_min + new_x_max) / 2 / new_imW
                new_y_center = (new_y_min + new_y_max) / 2 / new_imH
                new_width = (new_x_max - new_x_min) / new_imW
                new_height = (new_y_max - new_y_min) / new_imH

                # Kiểm tra nếu tọa độ trung tâm nằm trong vùng hợp lệ
                # if 0 <= new_x_center <= 1 and 0 <= new_y_center <= 1:
                new_labels.append(
                        f"{int(obj_class)} {new_x_center:0.6f} {new_y_center:0.6f} {new_width:0.6f} {new_height:0.6f}"
                    )

    s = "\n".join(new_labels)
    return s


def update_labels0(label_path, x_min_crop, y_min_crop, new_imW, new_imH):
    # Cập nhật file nhãn dựa trên ảnh đã crop
    new_labels = []
    with open(label_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            obj_class, x_center, y_center, width, height = map(float, line.split())

            # Tính tọa độ mới theo ảnh đã crop
            new_x_center = (x_center * new_imW - x_min_crop) / new_imW
            new_y_center = (y_center * new_imH - y_min_crop) / new_imH
            new_labels.append(
                f"{obj_class} {new_x_center} {new_y_center} {width} {height}"
            )

    # Ghi lại nhãn mới vào file
    with open(label_path, "w") as file:
        file.write("\n".join(new_labels))


def process_directory(root_dir, yolo_str):
    # for subdir, _, files in os.walk(root_dir):
    #     for file in files:
    #         if file.endswith(".jpg"):
    image_path = r"H:\DATA\Cam360SmartGate\Training_data_from_DUY\_Train\11_10\6\6_1\frame000015.jpg"
    # image_path = os.path.join(subdir, file)
    # label_path = os.path.join(subdir, file.replace(".jpg", ".txt"))
    label_path = r"H:\DATA\Cam360SmartGate\Training_data_from_DUY\_Train\11_10\6\6_1\frame000015.txt"
    # Crop ảnh
    cropped_img, old_imW, old_imH = crop_image(image_path, yolo_str)
    new_imW, new_imH=cropped_img.size
    # Lưu ảnh đã crop
    # cropped_img.save(image_path)

    # Cập nhật file nhãn của ảnh vừa crop
    id, x_min_crop, y_min_crop, x2, y2 = yolo_str_to_bbox(yolo_str, old_imH, old_imW)
    print("Crop area:", id, x_min_crop, y_min_crop, x2, y2)
    s=update_labels(
        label_path, x_min_crop, y_min_crop, new_imW, new_imH, old_imW, old_imH                    
                )

    print('s=',s)


if __name__ == "__main__":
    # Ví dụ sử dụng
    root_dir = "H:\DATA\Cam360SmartGate\Training_data_from_DUY\_Train\11_10\6\6_1"
    yolo_str = "0 0.496094 0.772135 0.527344 0.453125"  # Tọa độ YOLO được cung cấp
    process_directory(root_dir, yolo_str)
