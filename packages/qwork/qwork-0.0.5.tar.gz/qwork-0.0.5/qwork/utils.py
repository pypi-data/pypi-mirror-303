import os
import pickle
import inspect
from files3 import files
from qwork.qtimp import *
from qwork.qtclrs import *
from PyQt5.QtWidgets import QFileDialog

def get_caller_by_offset(last_offset: int = 0) -> str:
    """
    根据偏移量获取调用者的名称。失败返回''。
    :param last_offset: 0, get_caller_by_offset调用者. >0时向前回溯调用栈。
    :return: str, 调用者的名称。
    """
    try:
        # 获取当前的调用栈
        stack = inspect.stack()
        # 计算要获取的帧的索引
        length = len(stack)
        last_offset += 1    # 跳过get_caller_by_offset
        # 检查索引是否有效
        if last_offset >= length:
            return ''
        # 获取指定索引的调用帧
        frame = stack[last_offset]
        # 获取调用者的名称
        caller_name = frame.function

        # 检查module
        if 'module' in caller_name:
            caller_name = f"module_{os.path.basename(frame.filename).split('.')[0]}"

        return caller_name
    except IndexError:
        # 如果索引超出范围，则返回None
        return ''


HASH_BAND = 0X7FFFFFFF

def myhash(input_):
    if not isinstance(input_, bytes):
        input_ = pickle.dumps(str(input_))
    hash_value = 0
    for i, b in enumerate(input_):
        hash_value = ((hash_value << (i & 0x3)) ^ b) & HASH_BAND
    return hash_value

def api_get_key(*names:str, skey:str=None, offset:int=2) -> str:
    if not names:
        raise ValueError("api_get_key: names can not be empty.")
    skey = skey or get_caller_by_offset(offset)
    res = []
    for name in names:
        res.append(str(myhash(f"{name}{skey}".encode())))
    return res if len(res) > 1 else res[0]

class QSetting:  # Settings
    def __init__(self, setting_path:str="", setting_filename:str="settings", type_suffix:str=".qst", stype_suffix:str=".ist"):
        setting_path = os.path.abspath(setting_path)
        if not os.path.isdir(setting_path):
            raise NotADirectoryError(f"QSetting:{setting_path} is not a directory.")
        self._f = files(setting_path, type_suffix, stype_suffix)
        self._filename = setting_filename

        # is first runtime check
        self.runtimes = {}

    def __getitem__(self, stkey:str):
        return self._f[self._filename, stkey]

    def __setitem__(self, stkey:str, value):
        self._f[self._filename, stkey] = value

    def __contains__(self, item):
        return self._f.has(self._filename, item)

    def set(self, name:str, value):
        self._f[self._filename, name] = value

    def get(self, name:str):
        return self._f[self._filename, name]

    def hset(self, name:str, value):
        name = api_get_key(name)
        self[name] = value

    def hget(self, name:str):
        name = api_get_key(name)
        return self[name]

    def has(self, name:str):
        return self._f.has(self._filename, name)

    def getOpenFileName(self, title: str = "Open File", dirpath: str = "", filter_string: str = "All Files (*)", skey:str='', auto:bool=False) -> str:
        """
        Qt.FileDialog.getOpenFileName.
        在Qt中打开文件对话框，获取文件名和文件类型。
        * 自动保存最后打开的文件夹路径。
        :param title:
        :param dirpath:
        :param filter_string:
        :param skey: str, 保存的键名。如果为空，则使用上一帧的函数名作为辅助键名。
        :param auto: bool, 自动返回最后打开的结果(如果有记录且存在)。
            * 注意，无论如何，某个caller首次运行此函数时auto不生效
        :return: str
        """
        key = api_get_key("getOpenFileName", skey=skey)

        # check auto return
        _last_res:str = self[key]
        if key not in self.runtimes:    # 避免首次运行时auto生效
            self.runtimes[key] = True
        elif auto and _last_res and os.path.exists(_last_res):
            return _last_res

        # body
        _last_dir = os.path.dirname(_last_res) if _last_res else dirpath
        _0, _1 = QFileDialog.getOpenFileName(None, title, _last_dir, filter_string)

        if _0 and os.path.exists(_0):
            self[key] = _0

        return _0

    def getSaveFileName(self, title: str = "Save File", dirpath: str = "", filter_string: str = "All Files (*)", *, filename:str='', skey:str=None, auto:bool=False) -> str:
        """
        Qt.FileDialog.getSaveFileName.
        在Qt中打开保存文件对话框，获取文件名和文件类型。
        * 自动保存最后打开的文件夹路径。
        :param title:
        :param dirpath:
        :param filter_string:
        :param filename:
        :param skey: str, 保存的键名。如果为空，则使用上一帧的函数名作为辅助键名。
        :param auto: bool, 自动返回最后打开的结果(如果有记录)。
            * 注意，无论如何，某个caller首次运行此函数时auto不生效
        :return:
        """
        key = api_get_key("getSaveFileName", skey=skey)

        # check auto return
        _last_res:str = self[key]
        if key not in self.runtimes:
            self.runtimes[key] = True
        elif auto and _last_res:    # save not check exists
            return _last_res

        # body
        _last_dir = os.path.dirname(_last_res) if _last_res else dirpath
        _0, _1 = QFileDialog.getSaveFileName(None, title, _last_dir, filter_string, filename)

        if _0:  # save not check exists
            self[key] = _0

        return _0




    def getOpenFileNames(self, title: str = "Open Files", dirpath: str = "", filter_string: str = "All Files (*)", skey:str=None, auto:bool=False) -> list[str]:
        """
        Qt.FileDialog.getOpenFileNames.
        在Qt中打开文件对话框，获取文件名列表和文件类型。
        * 自动保存最后打开的文件夹路径。
        :param title:
        :param dirpath:
        :param filter_string:
        :param skey: str, 保存的键名。如果为空，则使用上一帧的函数名作为辅助键名。
        :param auto: bool, 自动返回最后打开的结果(如果有记录且存在)。
            * 注意，无论如何，某个caller首次运行此函数时auto不生效
        :return:
        """
        key = api_get_key("getOpenFileNames", skey=skey)

        # check auto return
        _last_res:str = self[key]
        if key not in self.runtimes:
            self.runtimes[key] = True
        elif auto and _last_res and os.path.exists(_last_res):
            return _last_res

        # body
        _last_dir = os.path.dirname(_last_res[0]) if _last_res else dirpath
        _0, _1 = QFileDialog.getOpenFileNames(None, title, _last_dir, filter_string)

        if _0:
            self[key] = _0

        return _0


    def getExistingDirectory(self, title: str = "Open Directory", dirpath: str = "", *, stlast:bool=False, skey:str=None, auto:bool=False) -> str:
        """
        Qt.FileDialog.getExistingDirectory.
        在Qt中打开文件夹对话框，获取文件夹路径。
        * 自动保存最后打开的文件夹路径。
        :param title:
        :param dirpath:
        :param stlast: bool, 使用选中目标文件夹的上一级目录作为结果，而不是选中的目标文件夹。
        :param skey: str, 保存的键名。如果为空，则使用上一帧的函数名作为辅助键名。
        :param auto: bool, 自动返回最后打开的结果(如果有记录且存在)。
            * 注意，无论如何，某个caller首次运行此函数时auto不生效
        :return:
        """
        _caller = get_caller_by_offset(1)
        key = api_get_key("getExistingDirectory", skey=skey)

        # check auto return
        _last_res:str = self[key]
        if key not in self.runtimes:
            self.runtimes[key] = True
        elif auto and _last_res and os.path.exists(_last_res):
            return _last_res if not stlast else os.path.dirname(_last_res)

        # body
        _last_dir = os.path.dirname(_last_res) if _last_res else dirpath
        _0 = QFileDialog.getExistingDirectory(None, title, _last_dir)

        if _0:
            self[key] = _0

        if stlast:
            _0 = os.path.dirname(_0)

        return _0


