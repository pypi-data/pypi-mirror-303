import re
import io
import os
import zipfile
import chardet
from files3 import files, F3False

__dir__ = os.path.dirname(__file__)
TFI_PATH = os.path.join(__dir__, 'tfi.exe')
FP_ICON_IPCDIR = os.path.join(__dir__, 'ipcdir.ico')
def parse_group_path(group_path:str) -> list[str]:
    """
    Parse the group path string to a list of group names.
    解析组路径字符串为组名列表
    :param group_path: str, the group path string, e.g. "group1/group2/group3"
    :return: list[str], the list of group names, e.g. ["group1", "group2", "group3"]
    """
    return [it.strip() for it in re.split(r'[\\/]', group_path) if it.strip()]


def auto_encoding(data: bytes|str, threshold: float = 0.9) -> str|None:
    """
    Automatic encoding transformation
    :param data: bytes|str. If str, mean a file path
    :param threshold: float, the confidence threshold. If the confidence is less than this value, return None.
    :return: str
    """

    if isinstance(data, str):
        with open(data, 'rb') as f:
            data = f.read()

    result = chardet.detect(data)
    encoding = result['encoding']
    confidence = result['confidence']
    if confidence < threshold:
        return None
    return encoding


def auto_decode(data: bytes) -> str|None:
    """
    Automatic encoding transformation
    :param data: bytes
    :param error: bool, whether to raise an error when an exception occurs
    :return: str
    """
    entype = auto_encoding(data)
    if entype is None:
        return None
    try:
        return data.decode(entype)
    except UnicodeDecodeError:
        return None

def auto_open(file:str) -> str:  # auto select encoding
    """
    Open a file and return the content
    :param file: str, the file path
    :return: str, the content
    """
    with open(file, 'rb') as f:
        data = f.read()
    return auto_decode(data)

def unziptarget(input:bytes|str, target:str=None) -> bytes:
    """
    Unzip the input data to bytes
    :param input: bytes|str, the input data or the input file path.
        * bytes: zip file bytes(read by rb)
        * str: zip file path
    :param target: str, the target archive name. If None, return the first file in the zip file.
    :return: target file bytes
    """
    if isinstance(input, str):
        with open(input, 'rb') as f:
            data = f.read()
    else:
        data = input

    with zipfile.ZipFile(io.BytesIO(data)) as z:
        # empty check
        if len(z.namelist()) == 0:
            return b''

        # sel target
        if target is None:
            target = z.namelist()[0]

        return z.read(target)


def create_prepare():
    name_func_args = []
    if not os.path.exists(TFI_PATH):
        name_func_args.append(
            ("tool: tfi.exe", files.prefab.astarget, (TFI_PATH, ))
        )
    if not os.path.exists(FP_ICON_IPCDIR):
        name_func_args.append(
            ("icon: ipcdir.ico", files.prefab.astarget, (FP_ICON_IPCDIR, ))
        )
    return name_func_args


