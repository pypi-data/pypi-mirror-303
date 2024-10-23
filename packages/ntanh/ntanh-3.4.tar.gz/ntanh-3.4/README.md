# Giới thiệu

ntanh là một thư viện các nhiệm vụ hàng ngày sử dụng, hay dùng nhưng không khó, mất thời gian code cho các dự án lẻ tẻ.

# Cài đặt bằng các cách sau:

```bash
pip install ntanh
pip install --upgrade --force-reinstall ntanh
pip install --upgrade ntanh --no-deps

```

Cài trực tiếp trong code:

```python

try:
    os.system("python -m pip install --upgrade --force-reinstall ntanh --no-deps")
except Exception as e:
    print('ntanh:', e)
import ntanh
```

# Cách dùng:

```python
from pprint import pprint
from ntanh.ParamsBase import tactParametters
import ntanh

print(ntanh.__version__)
mParams = tactParametters()

fns = mParams.fnFIS(r"../", exts=(".py"))
pprint(fns)
```

Kết quả:

```
'0.1.4'
['../tact/setup.py',
 '../tact/__init__.py',
 '../tact/build/lib/ntanh/ParamsBase.py',
 '../tact/build/lib/ntanh/__init__.py',
 '../tact/build/lib/tact/ParamsBase.py',
 '../tact/build/lib/tact/__init__.py',
 '../tact/dev/test_tact.py',
 '../tact/ntanh/ParamsBase.py',
 '../tact/ntanh/__init__.py']
```

Ví dụ 2: tạo file tham số:

```python

from pprint import pprint
from ntanh.ParamsBase import tactParametters

class Parameters(tactParametters):
    def __init__(self, ModuleName="TACT"):
        super().__init__()
        self.thamso1 = "thamso1"
        self.thamso2 = " xâu tiếng việt"
        self.api_url = "https://200.168.90.38:6699/avi/collect_data"
        self.testpath = "D:/test_debug_fii"
        self.test_real = 0.8
        self.test_int = 12
        self.test_dict = {
            1: 2,
            3: 4.5,
            "6": "bảy nhá",
            -1: "Tám",
            9: [10, 11.2, "22", (33, 44, "55")],
            10: {101: 12, 102: "mười ba"},
        }
        self.test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.load_then_save_to_yaml(file_path="configs_test.yml", ModuleName=ModuleName)
        self.privateVar1 = 2
        self.privateVar2 = "Not in param file"


mParams = Parameters(ModuleName="test")

pprint(mParams.__dict__)
```

Kết quả:

```
{'ModuleName': 'test',
 'api_url': 'https://200.168.90.38:6699/avi/collect_data',
 'fn': 'configs_test.yml',
 'logdir': '',
 'privateVar1': 2,
 'privateVar2': 'Not in param file',
 'test_dict': {-1: 'Tám',
               1: 2,
               3: 4.5,
               9: [10, 11.2, '22', (33, 44, '55')],
               10: {101: 12, 102: 'mười ba'},
               '6': 'bảy nhá'},
 'test_int': 12,
 'test_list': [1, 2, 3, 4, 5, 6, 7, 8, 9],
 'test_real': 0.8,
 'testpath': 'D:/test_debug_fii',
 'thamso1': 'thamso1',
 'thamso2': ' xâu tiếng việt'}
```

## Console Running

### 3. Image dupplicate remover
Lệnh này sẽ di chuyển ảnh bị trùng lặp ra 1 folder khác (cấu hình trong file config), nhằm loại bỏ các ảnh quá giống nhau theo nội dung, nhưng so sánh theo tên liên tiếp (ảnh do video tách ra), training cho nhanh.

Command: `ntanh_img_del`

Lệnh này sẽ tạo 1 file config, đường dẫn sẽ hiển thị trên CMD, chúng ta vào đó cấu hình lại, rồi chạy

### 2. Image Augmentation
Intro: Lệnh này nhằm tăng cường ảnh, từ 1 thư mục ảnh gốc, nó sẽ tăng cường ảnh ra thành ảnh mới, có độ sáng, độ nét,... thay đổi theo cấu hình.

Command:`ntanh_aug`

Lệnh này sẽ tạo 1 file config, đường dẫn sẽ hiển thị trên CMD, chúng ta vào đó cấu hình lại, rồi chạy

### 1. Help
Command: `ntanh`

Lệnh này sẽ hiển thị help có các trường hợp sử dụng cơ bản


# Version changed

- V3.4 (2024-10-23): 
    - Thêm hàm `YoloCrop`: `image = YoloCrop(image_cv2, coverYolo_str, Delta_Expand=0)`, hàm này sẽ cắt ảnh trực tiếp từ xây yolo.
- V3.3 (2024-10-17):        
    - V3.3.7-8 (2024-10-19): Thêm console `ntanh_base_params_help`, in ra cách dùng của `BaseParams`, fixbug
    - V3.3.6 (2024-10-18): thêm chức năng resize ảnh sau crop theo list `cover_yolo_string__resize_after_crop_HW`, nếu không muốn resize, đặt thành `[]`
    - V3.3.4 (2024-10-18): fix lỗi lệch tọa độ các object bên trong ảnh, khi crop ảnh bằng `cover_yolo_string`
    - V3.3.3 (2024-10-18): Update chỉ dẫn trong help `ntanh` để cập nhật thêm các tên của các thư viện khác.
    - V3.3.2 (2024-10-18): Update this document.
    - V3.3.1 (2024-10-18): Bổ sung hướng dẫn trong lệnh `anhnt`, thêm hướng dẫn link ra `https://ntanhfai.github.io`

    - Thêm chức năng crop + tính toán lại tọa độ yolo label theo ảnh mới mà vẫn đúng object theo ảnh cũ.
-   V3.2 (2024-10-17):
    - Thay đổi cách `ParamsBase` lưu cấu hình, không để nó chồng chéo các project khác nhau trong cùng 1 project này nữa.
-   V3.1 (2024-10-17):
    - Thêm chức năng Xóa ảnh trùng lặp trong thư mục yolo training data. Chạy lệnh  `ntanh_img_del`, sửa config, chạy lại, nó sẽ move ảnh+label trùng lặp ra thư mục output.
    - Nó tính toán xong hết rồi mới move, nên nếu thấy lâu quá thì kệ nó chạy, hoặc là chạy cho các thư mục nhỏ nhỏ thôi. 
    - Từ nay sẽ đổi cách tính version: mỗi lần có thêm 1 chức năng mới, sẽ lên 1 version chính, số phụ đằng sau sẽ là số lần update chức năng nào đó.

-   V0.1.7 (2024-10-16):
    - Thêm chức năng Augment ảnh theo folder
        - Có thể chạy augment image trực tiếp trong console, thay đổi cấu hình trong file config, đường dẫn file config sẽ được hiển thị trong console khi chạy.
    - Thêm hàm `ntanh.ParamsBase.get_Home_Dir(AppName)`, Hàm này sẽ tạo folder `C:\RunProgram\AppName` và trả về đường dẫn. Mặc định cho tất cả các ứng dụng, dễ dùng và tập trung, không bị nhầm lẫn.

-   V0.1.6 (2024-10-14):

    -   Thêm thư viện convert yolo-bbox: `from ntanh.yolo_boxes import xyxy_to_yolo_str, yolo_str_to_xyxy`
    -   print: `ntanh.__help__` sẽ ra hướng dẫn.
    -   V 0.1.6.1:
        -   Thay đổi thứ tự tham số trong hàm Yolo convert, trả kết quả dạng int thay vì float khi convert yolo2bbox

-   V0.1.5 (2024-10-14):
    -   Hoàn thiện chức năng tạo file config cho mỗi class: `from ntanh.ParamsBase import tactParametters`
    -   Cập nhật readme, diễn giải nội dung.
    -   Chạy `ntanh.info()` sẽ in ra code mẫu.
-   V0-V0.1.4:
    -   Test upload.
