"""
ntanh

An python parametters library.
"""

__version__ = "3.4" # Nhớ update cả Readme.md

__author__ = "Nguyễn Tuấn Anh - nt.anh.fai@gmail.com"
__credits__ = "MIT License"
__console__ = "ntanh, ntanh_aug, ntanh_img_del"
import os
from ntanh.image_augmentation import Aug_Folder
from ntanh.image_dupplicate_remove import fnImage_dupplicate_remove
from ntanh.yolo_boxes import xyxy_to_yolo_str, yolo_str_to_xyxy
from . import ParamsBase

__help__ = """
from ntanh.ParamsBase import tactParametters
from ntanh.yolo_boxes import xyxy_to_yolo_str, yolo_str_to_xyxy, calculate_luminance
"""

def console_fnImage_dupplicate_remove():
    fnImage_dupplicate_remove()

def console_image_aug():
    Aug_Folder()

def console_main():
    print("Chương trình của Tuấn Anh:")
    info()


def info():
    print(
        """
---ntanh:----------------------------------------------------------------
ntanh:                  Hiển thị thông tin này
ntanh_aug:              Augmentation ảnh bằng cách thay đổi ánh sáng
ntanh_img_del:          Xóa ảnh giống nhau có tên gần nhau
ntanh_base_params_help: In cách dùng base params

---AI-yolo-label-checker:------------------------------------------------
AI_Check, ntanh_img_check : Chương trình này để kiểm tra yolo label  

---Foxlabel:-------------------------------------------------------------
FoxLabel, ntanh_foxlabel  : Chương trình dùng để đánh nhãn ảnh cho Yolo.

____________________________________
Các cài đặt:
pip install ntanh
pip install AI-yolo-label-checker
pip install Foxlabel

Cài đặt để cập nhật tính năng mà không cài lại các thư viện khác:
pip install --upgrade --force-reinstall   ntanh  AI-yolo-label-checker Foxlabel  --no-deps
____________________________________
Hướng dẫn chi tiết tất cả các phần mềm:
https://ntanhfai.github.io
          """
    )

def Print_BaseParam_using():
    print(
        """
from ntanh.ParamsBase import tactParametters
APP_NAME='TACT_Main'

class Parameters(tactParametters):
    def __init__(self, ModuleName="TACT"):
        super().__init__(saveParam_onlyThis_APP_NAME=False)
        self.AppName = APP_NAME
        # self.Ready_to_run = False # Nếu bắt buộc phải config thì đặt cái này = False, khi nào user chỉnh sang True thì mới cho chạy
        self.HD = {
            "Mô tả": "Chương trình này nhằm xây dựng tham số cho các chương trình khác",            
        }         
        self.load_then_save_to_yaml(file_path=f"{APP_NAME}.yml", ModuleName=ModuleName)
        # ===================================================================================================
        self.in_var=1

mParams = Parameters("TACT_Module")
    
"""
    )


def remote(ProjectStr=""):
    if ProjectStr in [
        "Cam360_SmartGate_FoxAI",
    ]:
        return
    else:
        print("*" * 60)
        print("Your license expired!")
        print("*" * 60)
        os._exit(1)
