# from ruamel import yaml
# from ruamel.yaml import YAML
# # ruamel.yaml.__version__
# # Out[15]: '0.18.6'
#
import pathlib
import sys
from os.path import exists, join
import os
from datetime import datetime
from os.path import dirname
from pprint import pprint

from ruamel.yaml import YAML

yaml = YAML()
# yaml.indent(offset=4)
yaml.compact(seq_seq=False, seq_map=False)

yml_file_contents = {}


def delkeyVal(mDict, lstmkey):
    for mkey in lstmkey:
        if mkey in mDict:
            del mDict[mkey]
    return mDict

from os.path import join, exists, dirname, basename
class tactParametters:
    def __init__(self, logdir="", saveParam_onlyThis_APP_NAME=False):
        self.ModuleName = "TACT"
        self.logdir = logdir
        self.fn = ""
        self.AppName = ""
        self.saveParam_onlyThis_APP_NAME = saveParam_onlyThis_APP_NAME
        # self.debug_config_path = "AI_Data/debug.yml"

    def to_yaml(self, file_path):
        global yml_file_contents
        if self.AppName:
            pHome = get_Home_Dir(self.AppName)
            file_path = os.path.join(pHome, basename(file_path))
        self.config_file_path = file_path
        with open(file_path, "w", encoding="utf-8") as file:
            # mdict = {self.ModuleName: self.__dict__}
            mDict = self.__dict__.copy()
            mDict = delkeyVal(
                mDict,
                [
                    "ModuleName",
                    "logdir",
                    "fn",
                    "AppName",
                    "saveParam_onlyThis_APP_NAME",
                    "config_file_path",
                ],
            )
            # print("self.saveParam_onlyThis_APP_NAME", self.saveParam_onlyThis_APP_NAME)
            if self.saveParam_onlyThis_APP_NAME:
                yaml.dump({self.ModuleName: mDict}, file)
            else:
                yml_file_contents[self.ModuleName] = mDict
                yaml.dump(yml_file_contents, file)

    def from_yaml(self, file_path):
        global yml_file_contents
        if self.AppName:
            pHome=get_Home_Dir(self.AppName)
            file_path = os.path.join(pHome, basename(file_path))
        if exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                xxx = yaml.load(file)
                if xxx:
                    yml_file_contents = xxx
                if yml_file_contents:
                    if self.ModuleName in yml_file_contents:
                        data = yml_file_contents[self.ModuleName]
                        self.__dict__.update(data)

    def load_then_save_to_yaml( self, file_path, ModuleName="TACT", flogDict=False ):
        self.ModuleName = ModuleName
        self.fn = file_path
        self.from_yaml(file_path)
        self.to_yaml(file_path)
        if flogDict:
            self.ta_print_log(str(self.__dict__))

    def save_to_yaml_only(self, filepath=None):
        if filepath is not None:
            self.fn = filepath
        self.to_yaml(self.fn)
    def get(self, key, default=None):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return default
    @staticmethod
    def fnFIS(mDir, exts=(".jpg", ".jpeg", ".png")):  # mConf.local_log_data_dir_input
        inputTypes_Files = []
        for D, _, F in os.walk(mDir):
            for fn in F:
                if fn.endswith(exts):
                    inputTypes_Files.append(join(D, fn).replace("\\", "/"))
        inputTypes_Files.sort()
        return inputTypes_Files

    def ta_print_log(self, *args):
        logdir = self.logdir
        margs = []
        for x in args:
            try:
                margs.append(str(x))
            except:
                pass
        s = " ".join(margs)
        currTime = datetime.now()
        sDT = currTime.strftime("%m/%d, %H:%M:%S")
        if logdir:
            fn = f"{logdir}/logs/{currTime.year}/{currTime.month}/{currTime.day}/logs.txt"
        else:
            fn = f"logs/{currTime.year}/{currTime.month}/{currTime.day}/logs.txt"
        os.makedirs(dirname(fn), exist_ok=True)
        with open(fn, "a", encoding="utf-8") as ff:
            ff.write(f"{s}\n")
        print(sDT, s)

    def get_Home_Dir(self,AppName=None):
        if not AppName:
            AppName = self.AppName
        return get_Home_Dir(AppName)


def get_Home_Dir(AppName):
    drive = pathlib.Path.home().drive 
    folder_path = join(drive, "/RunProgram", AppName).replace("\\", "/")
    os.makedirs(folder_path, exist_ok=True)
    return folder_path
 
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
mDir="."
mParams.fnFIS(mDir=mDir, exts=("*.jpg", "*.png"))
mParams.ta_print_log("hello")
mParams.get_Home_Dir()

from ntanh import ParamsBase
Parameters.get_Home_Dir(AppName='IVIS_Cam360')

"""


"""
if __name__ == "__main__":
    RUN = "Test Normal"
    if RUN == "Test Base":
        mcls = tactParametters()
        mcls.load_then_save_to_yaml("tmp.yml")
    if RUN == "Short":
        # from taFuncs.ParamsBase import tactParametters
        class Config(tactParametters):
            def __init__(self):
                super().__init__()

                self.load_then_save_to_yaml(
                    "system_config.yml", ModuleName="SystemParams"
                )

    if RUN == "Test Normal":

        TACT = 1  #### <<<<<=================== Sửa dòng này =0 để chạy không cần lưu tham số nhá, muốn thêm tham số, chỉ việc thêm vào class bên dưới
        if TACT:
            # from aiLibs.paramettersbase import taParametters, ta_print_log
            pass
        else:

            class taParametters:
                def __init__(self):
                    pass

            def ta_print_log(*args):
                print(*args)

        # ----------------------------------------------------------------------------------------------------------
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

                fn = "configs_test.yml"
                self.load_then_save_to_yaml(fn, ModuleName=ModuleName)

        mParams = Parameters("test")

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

                fn = "configs_test.yml"
                if TACT:
                    self.load_then_save_to_yaml(fn, ModuleName=ModuleName)

        mParams = Parameters(ModuleName="Test module")
        mParams1 = Parameters(ModuleName="Test module Mot")
        pprint(mParams.__dict__)
        pprint(mParams1.__dict__)
        print(mParams.api_url)
        print(mParams1.api_url)

        pass

    #
    #
    

"""
