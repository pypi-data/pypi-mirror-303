import os, sys
import random
# import setuptools
import shutil
import cv2
from os.path import join, exists, dirname
from pprint import pprint as pp
# print(os.getcwd()) # Thư mục console đang chạy
# print(__file__) # Thư mục file code
codeDir=dirname(os.path.abspath(__file__))
sys.path.append(codeDir)

# pp(sys.path)

from ParamsBase import tactParametters
from tqdm import tqdm
from yolo_boxes import yolo_str_to_xyxy

APP_NAME='Image_Augmentation'

class Parameters(tactParametters):
    def __init__(self, ModuleName="TACT"):
        super().__init__(saveParam_onlyThis_APP_NAME=True)
        self.AppName = APP_NAME
        self.Ready_to_run = False # Nếu bắt buộc phải config thì đặt cái này = False, khi nào user chỉnh sang True thì mới cho chạy
        self.HD = {
            "Brightness": "Adjust brightness (value: -255 to 255)",
            "Shadow_Brightness": "Adjust Shadow_Brightness (value: -255 to 255)",
            "Contrast": "Adjust contrast (alpha > 1 increases contrast, 0 < alpha < 1 decreases)",
            "Saturation": "Convert to HSV, adjust saturation, then back to BGR",
            "Hue": "Convert to HSV, adjust hue, then back to BGR",
            "cover_yolo_string": "'0 0.496094 0.772135 0.527344 0.453125' (ví dụ xâu), cái này nếu có giá trị, nó sẽ crop ảnh theo tọa độ trong này, TODO: tính lại tọa độ label theo cái này",
            "cover_yolo_string__resize_after_crop_HW": "Là 1 list, nếu không muốn resize, để thành list rỗng: []",
            "Max_random_image_to_Aug=x": "x==0: Aug tất cả các ảnh, x>0: chỉ Aug random x ảnh thôi, để test trong quá trình dò tim các tham số",
            "Cách dùng 1": "lệnh chạytrong CMD: 'ntanh_aug', khi hiển thị ảnh: bấm SPACE để tạm dừng/chạy tiếp, bấm ESC để thoát",
            "Cách dùng 2": "Muốn đưa tham số nào về mặc định thì xóa nó đi rồi chạy lại",
        }
        self.Intro="Chương trình này dành riêng cho việc augmentation ảnh nhằm tạo ra ảnh có các kiểu khác nhau phục vụ cho mục đích training model"

        self.cover_yolo_string = ""
        self.cover_yolo_string__expand_n_pixel = 20
        self.cover_yolo_string__resize_after_crop_WH=[]
        self.Brightness = 50
        self.Shadow_Brightness=0
        self.Contrast = 1.2
        self.Saturation = 0
        self.Hue = 0
        self.image_folder__input = ""
        self.image_folder_output = ""
        self.Copy_label_when_save_augment_image=True

        self.Display_image=True
        self.Display_image_Stop_to_View_in___cv2_waitkey__ms=1000
        self.Display_image_max_height=800
        self.Max_random_image_to_Aug=10
        self.load_then_save_to_yaml(file_path=f"{APP_NAME}.yml", ModuleName=ModuleName)


mParams = Parameters("Augmentation_images")

def taImshow(title="image",image=None, wait=0):
    H,W=image.shape[:2]
    if H > mParams.Display_image_max_height:
        fxy = mParams.Display_image_max_height / H
        image = cv2.resize(image, None, fx=fxy, fy=fxy)
    cv2.imshow(title, image)
    cv2.waitKey(wait)

from PIL import Image


def update_labels(
    label_path, x_min_crop, y_min_crop, new_imW, new_imH, old_imW, old_imH
):
    # Cập nhật file nhãn dựa trên ảnh đã crop
    new_labels = []
    with open(label_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
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


class ImageAugmentation:
    def __init__(self):
        pass

    def Change_Brightness(self, image, value):
        # Adjust brightness
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        # Ensure brightness value is in the range of [-255, 255]
        if value > 0:
            lim = 255 - value
            v[v > lim] = 255
            v[v <= lim] += value
        else:
            lim = -value
            v[v < lim] = 0
            v[v >= lim] += value

        final_hsv = cv2.merge((h, s, v))
        result = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR) 
        return result

    def Change_Shadow_Brightness(self, image, value):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        # Create a mask for shadows (dark areas)
        shadow_mask = v < 128

        # Adjust brightness in shadow areas
        if value > 0:
            lim = 255 - value
            v[shadow_mask & (v > lim)] = 255
            v[shadow_mask & (v <= lim)] += value
        else:
            lim = -value
            v[shadow_mask & (v < lim)] = 0
            v[shadow_mask & (v >= lim)] += value

        final_hsv = cv2.merge((h, s, v))
        result = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

        return result

    def Change_Contrast(self, image, value):
        # Adjust contrast (alpha > 1 increases contrast, 0 < alpha < 1 decreases)
        return cv2.convertScaleAbs(image, alpha=value, beta=0)

    def Change_Saturation(self, image, value):
        # Convert to HSV, adjust saturation, then back to BGR
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[:, :, 1] = cv2.add(hsv[:, :, 1], value)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def Change_Hue(self, image, value):
        # Convert to HSV, adjust hue, then back to BGR
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[:, :, 0] = cv2.add(hsv[:, :, 0], value)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def Change_Vibrance(self, image, value):
        # Custom vibrance logic, placeholder here
        return image  # Vibrance adjustment not implemented for simplicity

    def Change_image_multiple_ways(self, image,image_path, options):
        newLabel=''
        if options.get("cover_yolo_string", False):            
            imH, imW = image.shape[:2]
            id, x1, y1, x2, y2 = yolo_str_to_xyxy(
                yolo_str=mParams.cover_yolo_string, imH=imH, imW=imW
            )

            d = mParams.cover_yolo_string__expand_n_pixel
            y1, y2,  x1, x2= y1-d,y2+d, x1-d,x2+d

            image = image[y1:y2, x1:x2]

            # TODO: tính lại tọa độ theo cái này:
            label_path = image_path.replace(".jpg", ".txt")
            if exists(label_path): 
                x_min_crop, y_min_crop= x1, y1 
                new_imH, new_imW = image.shape[:2]
                newLabel = update_labels(
                    label_path,
                    x_min_crop,
                    y_min_crop,
                    new_imW,
                    new_imH,
                    imW,
                    imH,
                )
            if mParams.cover_yolo_string__resize_after_crop_WH:
                image = cv2.resize(
                    image, mParams.cover_yolo_string__resize_after_crop_WH
                )

        if mParams.Display_image: taImshow(title="Org image", image=image, wait=1)
        if options.get("Brightness", False):            
            image = self.Change_Brightness(image, mParams.Brightness)
            if mParams.Display_image: taImshow(title="Brightness", image=image, wait=1)
        if options.get("Shadow_Brightness", False):   
            image = self.Change_Shadow_Brightness(image, mParams.Shadow_Brightness)
            if mParams.Display_image: taImshow(title="image3", image=image, wait=0)
        if options.get("Contrast", False):
            image = self.Change_Contrast(image, mParams.Contrast)
            if mParams.Display_image: taImshow(title="Contrast", image=image, wait=1)
        if options.get("Saturation", False):            
            image = self.Change_Saturation(image, mParams.Saturation)
            if mParams.Display_image: taImshow(title="Saturation", image=image, wait=1)
        if options.get("Hue", False):            
            image = self.Change_Hue(image, mParams.Hue)
            if mParams.Display_image: taImshow(title="Hue", image=image, wait=1)

        if mParams.Display_image:
            keyPressed=cv2.waitKey(mParams.Display_image_Stop_to_View_in___cv2_waitkey__ms)
            if keyPressed==32:
                while True:
                    keyPressed = cv2.waitKey(
                        mParams.Display_image_Stop_to_View_in___cv2_waitkey__ms
                    )
                    if keyPressed==32:
                        break
                    if keyPressed==27:
                        os._exit(1)

        return image, newLabel

    def Augment_folder(self, **options):
        if mParams.image_folder__input == "":
            print("Hãy cấu hình giá trị cho file tham số trước, rồi chạy lại.")
            os.startfile("configs_ntanh_libs.yml")
            return
        image_folder_input = mParams.image_folder__input
        image_folder_output = mParams.image_folder_output

        FIS = mParams.fnFIS(image_folder_input, exts=(".jpg",))
        if mParams.Max_random_image_to_Aug > 0:
            FIS = [random.choice(FIS) for _ in range(mParams.Max_random_image_to_Aug)]
        nImg = len(FIS)

        if not exists(image_folder_output):
            os.makedirs(image_folder_output, exist_ok=True)

        for image_path in tqdm(FIS):
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to read image: {image_path}")
                continue

            image_out, newLabel = self.Change_image_multiple_ways( image, image_path, options )
            fnOut = image_path.replace(image_folder_input, image_folder_output)
            label_inp = image_path.replace(".jpg", ".txt")
            label_out = fnOut.replace('.jpg', '.txt')

            os.makedirs(dirname(fnOut), exist_ok=True) 
            cv2.imwrite(fnOut, image_out)
            if mParams.Copy_label_when_save_augment_image:
                if newLabel:
                    with open(label_out, "w") as file:
                        file.write(newLabel)
                elif exists(label_inp):
                    shutil.copy(label_inp, label_out) 
            # print(".", end="", flush=True)

        print()
        print(f"Done augmenting {nImg} images to {image_folder_output}")

def Aug_Folder():
    if not mParams.Ready_to_run:
        print('Thay đổi tham số config trong file:', mParams.get_Home_Dir())
        return
    
    aug = ImageAugmentation()
    print("cover_yolo_string:", mParams.get("cover_yolo_string", False))
    print("Brightness:", mParams.get("Brightness", False))
    print("Contrast:", mParams.get("Contrast", False))
    print("Saturation:", mParams.get("Saturation", False))
    print("Hue:", mParams.get("Hue", False))
    aug.Augment_folder(
        cover_yolo_string=mParams.get("cover_yolo_string", False),
        Brightness=mParams.get("Brightness", False),
        Contrast=mParams.get("Contrast", False),
        Saturation=mParams.get("Saturation", False),
        Hue=mParams.get("Hue", False),
        Vibrance=mParams.get("Vibrance", False),
    )
if __name__ == "__main__":
    Aug_Folder()
