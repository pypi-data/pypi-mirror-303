APP_NAME = "image_dupplicate_remove"
import os, sys
import os.path
from pprint import pprint as pp
from os.path import dirname, basename, join, isfile, isdir,exists
import time
# import imagehash
import numpy as np
from tqdm import tqdm
# print(os.getcwd()) # Thư mục console đang chạy
# print(__file__) # Thư mục file code
codeDir = dirname(os.path.abspath(__file__))
sys.path.append(codeDir)
# pp(sys.path)
# from PIL import Image, ImageChops
from ParamsBase import tactParametters as BasePr
from image_augmentation import taImshow
import shutil


class Parameters1(BasePr):
    def __init__(self, ModuleName="TACT"):
        super().__init__(saveParam_onlyThis_APP_NAME=True)
        # self.onlyThisAPP_NAME=True
        self.Ready_to_run = False
        self.AppName = APP_NAME
        self.Intro = "Chương trình này dành riêng cho việc remove ảnh gần giống nhau, phục vụ cho mục đích training model"
        self.HD_CMD = "ntanh_img_del"
        self.HD_install_this_lib = "pip install ntanh"
        self.HD = {
            "N_first_files_image_to_find_duplicate=x": "x==0: chạy hết tất cả files, x>0: chỉ chạy x file đầu tiên",
            "dupplicate_threshold": "Số thực, cần căn cứ vào số sai khác thực tế theo Diff histogram in cuối mỗi lần chạy",
            "num_diff_average_bins": "Số lượng bị cần chia khi tính histogram, bin càng nhiều thì chia Diff càng nhỏ",
            "Run_actual_move_file": "=True: nó sẽ thực sự chuyển các file vào image_folder_output khi diff<dupplicate_threshold, =false: chỉ tính, không chuyển file, gọi là dry run.",
        }
        self.dupplicate_threshold = 5
        self.image_folder__input = ""
        self.image_folder_output = ""
        self.Loop_Move_image_and_label_until_no_duplicate = False
        self.N_first_files_image_to_find_duplicate = 10
        self.num_diff_average_bins=10
        self.Run_actual_move_file=True
        self.load_then_save_to_yaml(file_path=f"{APP_NAME}.yml", ModuleName=ModuleName)


mParams = Parameters1(APP_NAME)

# class ImageDupplicate_Remover:
#     def __init__(self):
#         self.previous_image=None
#         self.previous_image_H=0
#         self.isDiff=1
#         self.noDiff=0
#         pass

#     def isDiffirent(self, current):
#         H,W = current.shape[:2]
#         if self.previous_image is None:
#             self.previous_image=current
#             self.previous_image_H = H
#             return [0,0,W,H]
#         if self.previous_image_H!=H:
#             self.previous_image = current
#             self.previous_image_H = H
#             return [0, 0, W, H]

#         diff = ImageChops.difference(current, self.previous_image)
#         diff = diff.point(lambda x: 0 if x < mParams.dupplicate_threshold else 255)
#         self.previous_image = current
#         if diff.getbbox():
#             return diff.getbbox()
#         else:
#             return None

#     def fnRemove(self):
#         dupplicate_threshold = mParams.dupplicate_threshold
#         inpPath=mParams.image_folder__input
#         outPath=mParams.image_folder__output
#         fis=mParams.fnFIS(inpPath)
#         ...
#         list_dupplicate_imgs=...
#         for img_path in list_dupplicate_imgs:
#             shutil.move(img_path, outPath)
import os
import shutil
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.io import imread
from skimage.transform import resize


class ImageDuplicateRemover:
    def __init__(self):
        pass

    def fnRemove(self):
        # Ngưỡng SSIM để xác định ảnh trùng lặp
        duplicate_threshold = mParams.dupplicate_threshold

        # Đường dẫn đến thư mục input và output
        inpPath = mParams.image_folder__input
        outPath = mParams.image_folder_output

        # Hàm lấy danh sách các file image trong thư mục input
        fis = mParams.fnFIS(inpPath)
        if mParams.N_first_files_image_to_find_duplicate>0:
            fis = fis[: mParams.N_first_files_image_to_find_duplicate]
        # Danh sách các ảnh trùng lặp
        list_duplicate_imgs = []
        checked_imgs = []

        # Hàm kiểm tra kích thước ảnh trước khi so sánh SSIM
        # def preprocess_image(image, min_size=(7, 7)):
        #     # Nếu ảnh quá nhỏ, resize về kích thước tối thiểu
        #     if image.shape[0] < min_size[0] or image.shape[1] < min_size[1]:
        #         image = resize(image, min_size, anti_aliasing=True)
        #     return image

        # Hàm so sánh SSIM giữa hai ảnh
        # def images_are_similar(img1, img2, threshold):
        #     # Resize ảnh cho phù hợp với nhau nếu không có cùng kích thước
        #     # if img1.size != img2.size:
        #     #     img2 = resize(img2, img1.shape, anti_aliasing=True)

        #     # # Tính toán chỉ số SSIM với win_size nhỏ hơn hoặc bằng kích thước ảnh
        #     # win_size = min(
        #     #     img1.shape[0], img1.shape[1], 7
        #     # )  # win_size phải là số lẻ <= kích thước ảnh
        #     # ssim_value = ssim(
        #     #     img1, img2, multichannel=True, win_size=win_size, channel_axis=-1
        #     # )
        #     # print(ssim_value , threshold)
        #     # return ssim_value >= threshold
        #     # sumValue = np.sum(np.array(ImageChops.difference(img1, img2).getdata()))
        #     # return sumValue<threshold
        #     # def images_are_similar(img1, img2, threshold):
        #     diff = ImageChops.difference(img1, img2)
        #     if diff.getbbox() is None:  # Nếu không có sự khác biệt
        #         return True
        #     threshold = 50
        #     diff = diff.point(lambda x: 0 if x < threshold else 255)
        #     print(diff.getbbox())
        #     # Tính toán tổng mức độ khác biệt
        #     sum_diff = np.sum(np.array(diff.getdata()))
        #     # diff_hist = diff.histogram()
        #     # sum_diff = sum(diff_hist)
        #     print(sum_diff , threshold)
        #     diff.show()
        #     return sum_diff < threshold

        def is_Similar__mse(imageA, imageB, threshold, name1='', name2=''):
            # the 'Mean Squared Error' between the two images is the
            # sum of the squared difference between the two images;
            # NOTE: the two images must have the same dimension
            err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
            err /= float(imageA.shape[0] * imageA.shape[1])

            # return the MSE, the lower the error, the more "similar"
            # the two images are
            # print(err,"\t", name1 + "===" + name2)
            return  err < threshold, err
        average = 0
        n = 0
        average_data = []
        # Duyệt qua tất cả các ảnh để so sánh
        with tqdm(total=len(fis)//2) as pbar:
            # for i in tqdm(range(0,len(fis)-1, 2)):
            for i in range(0,len(fis)-1, 2):
                # print()
                img1_path = fis[i]
                # img1 = Image.open(img1_path)
                img1 = imread(img1_path)
                name1=os.path.basename(img1_path)
                # Xử lý ảnh nếu kích thước quá nhỏ
                # img1 = preprocess_image(img1)

                j=i+1
                img2_path = fis[j]
                # img2 = Image.open(img2_path)
                img2 = imread(img2_path)
                name2 = os.path.basename(img2_path)
                # Xử lý ảnh nếu kích thước quá nhỏ
                # img2 = preprocess_image(img2)
                is_Similar, mse= is_Similar__mse(img1, img2, duplicate_threshold, name1, name2)
                average = (n * average + mse) / (n + 1)
                n += 1
                if mse < average:
                    average_data.append(mse)

                if is_Similar:
                    list_duplicate_imgs.append(img2_path)
                # So sánh hai ảnh bằng SSIM
                # if images_are_similar(img1, img2, duplicate_threshold):
                #     list_duplicate_imgs.append(img2_path)
                # print(f"Found duplicate: {img2_path} (similar to {img1_path})")
                pbar.set_postfix(
                    duplicate=f"{len(list_duplicate_imgs)} files, average diff thresh: {average:3.6f}/{duplicate_threshold}"
                )
                # Phần code xử lý
                pbar.update(1)
        NfilesRemove = len(list_duplicate_imgs)

        # Di chuyển các ảnh trùng lặp vào thư mục output
        for k,img_path in enumerate(list_duplicate_imgs):
            dst=img_path.replace(inpPath, outPath)
            if mParams.Run_actual_move_file:
                dst_Dir=dirname(dst)
                os.makedirs(dst_Dir, exist_ok=True)
                shutil.move(img_path, dst_Dir)
                label=img_path.replace(".jpg", ".txt")
                if exists(label):
                    shutil.move(label, dst_Dir)
                print(f"{k:>3}. Moved duplicate image: {img_path} \t ==> \t {outPath}")
            else:
                print(f"{k:>3}. Will move duplicate image: {img_path} \t ==> \t {outPath}")
        min_value = min(average_data)
        max_value = max(average_data)
        bins = np.linspace(min_value, max_value, mParams.num_diff_average_bins + 1)
        # Tính histogram tích lũy
        hist, bin_edges = np.histogram(average_data, bins=bins)
        # Tạo chuỗi kết quả dưới dạng (bin_value: count)
        result_str = ",".join([f"{bin_edges[j]:.2f}-{bin_edges[j+1]:.2f}: {hist[j]}" for j in range(len(hist))])
        # Hiển thị chuỗi kết quả
        result_str = result_str.split(",")
        print()
        print(f"Diff histogram [mse<average], his min-his max: Number of files:")
        pp(result_str)
        print("Căn cứ vào his này, để chọn lại tham số dupplicate_threshold trong file config cho phù hợp.")
        return NfilesRemove

def fnImage_dupplicate_remove():
    if not mParams.Ready_to_run:
        print("Thay đổi tham số config trong file:", mParams.get_Home_Dir())
        return
    start = time.time()
    # Sử dụng lớp ImageDuplicateRemover
    image_remover = ImageDuplicateRemover()
    NfilesRemove=image_remover.fnRemove()
    if mParams.Loop_Move_image_and_label_until_no_duplicate:
        while NfilesRemove>0:
            NfilesRemove = image_remover.fnRemove()
    print("Total running:", time.time() - start, "s")

if __name__ == "__main__":
    fnImage_dupplicate_remove()
