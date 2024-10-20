import re
import time
import math as pymodule_math
from pyipcore.ipc_utils import *
from pyipcore.ui_utils import QPixmap, QIcon, QImage, QApplication
from pyipcore.ipcore_support_functions import SP_ENV_S as ENV_SUPPORT
from files3 import files


class IpCoreBuiltError(Exception):
    pass


class IpCoreModuleDefParseError(Exception):
    pass


class IpCoreCompileError(Exception):
    def __init__(self, rec: dict):
        txt = "[Compile Error] Details:\n"
        for v in rec['main']:
            txt += "\t{}\n".format(v)
        super().__init__(txt)


SINGLE_FILE_MAX_SIZE = 64  # MB
TOTAL_FILE_MAX_SIZE = 1024  # MB

class IpCore:
    """
    维护IP核文本
    """
    @staticmethod
    def _check_ipc(f:files, ipckey:str):
        if not f.has(ipckey):
            raise Exception(f"IpCore:IP core <{ipckey}> not found at {f.path}")
        _checks = ["header", "fmain", "ficon", "freadme", "fmanual", "fsubs", "fothers", "fpmain", "fpicon", "fpreadme", "fpmanual", "fpsubs", "fpothers"]
        for chk in _checks:
            if not f.has(ipckey, chk):
                raise Exception(f"IpCore:IP core <{ipckey}> at {f.path}:\n\t can not find '{chk}'")

    @staticmethod
    def _build_mono():
        return Mono(
            "//\s*>", "[;#\n]",
            r"\$", r"\$",
            r"/\*\s*>", r"\*/",
            "//\s*\[", "\]",
            COMMENT=r";#", CSO=r"^XXYYZZ", CEO=r"XXYYZZ$",
            ENV=ENV_SUPPORT
        )

    def __init__(self, dir=None, name=None):
        self.fdir = os.path.abspath(dir) if dir is not None else None
        self.key = name if name else None
        self.f = files(self.fdir, IPC_SUFFIX) if self.fdir is not None else None
        if self.f: self._check_ipc(self.f, self.key)

        self._mono = self._build_mono()

        """
        ipc:{
            "header": header,
            "files": {
                "main": bsmain,
                "icon": bsicon,
                "readme": bsreadme,
                "manual": bsmanual,
                # list:
                "subs": bssubfiles,
                "others": bsotherpaths
            }
        }
        """
        self._header:dict = self.f[self.key, "header"]
        self._content = None
        self._built = None
        self._fmd: FirstModuleDef = None
        self._last_icode = None
        self._lefts = None
        self._rights = None
        self._separators = None
        self._temp_dir = None  # TODO: 临时文件夹，用于解压缩文件，记得在析构函数中删除

    def GetICode(self):
        """Get the instance code of the IP core."""
        return self.icode

    @classmethod
    def _get_file_size(cls, path) -> float:  # 单位:MB
        return os.path.getsize(path) / 1024 / 1024

    @classmethod
    def Compile(cls,
                name: str, author: str, brand: str, model: str, board: str, group: str,
                fmain: str, ficon: str, freadme: str, fmanual: str,
                subpaths: list, otherpaths: list
                ) -> dict:
        """
        编译IP核, 返回header, files_paths, files_bytes
        """
        rec = {"main": ["Compile Start At: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))]}

        header = {
            "name": name,
            "author": author,
            "brand": brand,
            "model": model,
            "board": board,
            "group": group
        }
        rec['main'].append("Header: {}".format(header))

        # 将所有文件path转为绝对路径
        fmain = os.path.abspath(fmain)
        ficon = os.path.abspath(ficon) if ficon else None
        freadme = os.path.abspath(freadme) if freadme else None
        fmanual = os.path.abspath(fmanual) if fmanual else None
        subpaths = [os.path.abspath(f) for f in subpaths]
        otherpaths = [os.path.abspath(f) for f in otherpaths]

        # 获取所有文件的"名称.类型"
        fname_main = os.path.basename(fmain)
        fname_icon = os.path.basename(ficon) if ficon else None
        fname_readme = os.path.basename(freadme) if freadme else None
        fname_manual = os.path.basename(fmanual) if fmanual else None
        fnames_subfiles = [os.path.basename(f) for f in subpaths]
        fnames_otherpaths = [os.path.basename(f) for f in otherpaths]

        # 检查所有文件的大小
        rec['FileSizes'] = {}
        total_size = 0  # MB
        for f in subpaths:
            if not os.path.exists(f):
                rec['main'].append("File not found: {}".format(f))
                raise IpCoreCompileError(rec)
            _this_size = cls._get_file_size(f)
            if _this_size > SINGLE_FILE_MAX_SIZE:
                rec['main'].append("File too large: {}".format(f))
                raise IpCoreCompileError(rec)
            total_size += _this_size
            rec['FileSizes'][f] = _this_size
        rec['main'].append("Total size used: {:.2f}/{:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
        if total_size > TOTAL_FILE_MAX_SIZE:
            rec['main'].append("Total size used exceeds the limit: {:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
            raise IpCoreCompileError(rec)
        for f in otherpaths:
            if not os.path.exists(f):
                rec['main'].append("File not found: {}".format(f))
                raise IpCoreCompileError(rec)
            _this_size = cls._get_file_size(f)
            if _this_size > SINGLE_FILE_MAX_SIZE:
                rec['main'].append("File too large: {}".format(f))
                raise IpCoreCompileError(rec)
            total_size += _this_size
            rec['FileSizes'][f] = _this_size
        rec['main'].append("Total size used: {:.2f}/{:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
        if total_size > TOTAL_FILE_MAX_SIZE:
            rec['main'].append("Total size used exceeds the limit: {:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
            raise IpCoreCompileError(rec)
        for f in [fmain, ficon, freadme, fmanual]:
            if f is None or f == "":
                continue
            if not os.path.exists(f):
                rec['main'].append("File not found: {}".format(f))
                raise IpCoreCompileError(rec)
            _this_size = cls._get_file_size(f)
            if _this_size > SINGLE_FILE_MAX_SIZE:
                rec['main'].append("File too large: {}".format(f))
                raise IpCoreCompileError(rec)
            total_size += _this_size
            rec['FileSizes'][f] = _this_size
        rec['main'].append("Total size used: {:.2f}/{:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
        if total_size > TOTAL_FILE_MAX_SIZE:
            rec['main'].append("Total size used exceeds the limit: {:.2f} MB".format(total_size, TOTAL_FILE_MAX_SIZE))
            raise IpCoreCompileError(rec)
        rec['main'].append("All files are checked.")

        # create files_bytes
        _total_length = 0
        bsmain = files.pack(fmain)  # 考虑到subs和others的文件可能很多，所以这里统一用pack打包一下
        _length = len(bsmain)
        _total_length += _length
        rec['main'].append(f"pack target: {fmain} -> bytes<len={_length}>")
        bsicon = files.pack(ficon) if ficon else None
        if ficon:
            _length = len(bsicon)
            _total_length += _length
            rec['main'].append(f"pack target: {ficon} -> bytes<len={_length}>")
        else:
            rec['main'].append("No icon file. Skip.")
        bsreadme = files.pack(freadme) if freadme else None
        if freadme:
            _length = len(bsreadme)
            _total_length += _length
            rec['main'].append(f"pack target: {freadme} -> bytes<len={_length}>")
        else:
            rec['main'].append("No readme file. Skip.")
        bsmanual = files.pack(fmanual) if fmanual else None
        if fmanual:
            _length = len(bsmanual)
            _total_length += _length
            rec['main'].append(f"pack target: {fmanual} -> bytes<len={_length}>")
        else:
            rec['main'].append("No manual file. Skip.")
        bssubfiles = [files.pack(f) for f in subpaths]
        _length = sum([len(b) for b in bssubfiles])
        _total_length += _length
        rec['main'].append(f"pack subfiles: {len(bssubfiles)} files. Total bytes: {_length} bytes")
        bsotherpaths = [files.pack(f) for f in otherpaths]
        _length = sum([len(b) for b in bsotherpaths])
        _total_length += _length
        rec['main'].append(f"pack otherpaths: {len(bsotherpaths)} files. Total bytes: {_length} bytes")
        rec['main'].append("All files are packed. Total bytes: {}".format(_total_length))

        # 生成编译结果
        return {
            'header': header,
            "fpmain": fmain,
            "fpicon": ficon if ficon else None,
            "fpreadme": freadme if freadme else None,
            "fpmanual": fmanual if fmanual else None,
            # list:
            "fpsubs": subpaths,
            "fpothers": otherpaths,
            "fmain": bsmain,     # bytes
            "ficon": bsicon,     # bytes or None
            "freadme": bsreadme, # bytes or None
            "fmanual": bsmanual, # bytes or None
            # list:
            "fsubs": bssubfiles,
            "fothers": bsotherpaths
        }

    VERILOG_NUMBER = f"({FT.DIGIT_CHAR}+'{FT.ALPHA})?[0-9_]+"

    def build(self, **params) -> str:
        """Build the IP core with the given parameters."""
        # print("Building...")
        content = self.content
        try:
            self._built = self._mono.handle(content, **params)
        except Exception as e:
            raise IpCoreBuiltError("Failed to build the IP core. Details:\n\t{}".format(e))
        # with open('test~.v', 'w', encoding='utf-8') as f:
        #     f.write(self._built)
        # print("Parsing...")
        try:
            self._fmd = FirstModuleDef(self._built)
        except Exception as e:
            # with open('built~.v', 'w', encoding='utf-8') as f:
            #     f.write(self._built)
            raise IpCoreModuleDefParseError("Failed to parse the module definition. Details:\n\t{}".format(e))
        return self._built

    @classmethod
    def Build(cls, content:str, **params) -> str:
        """Build the IP core with the given parameters."""
        try:
            _built = cls._build_mono().handle(content, **params)
        except Exception as e:
            raise IpCoreBuiltError("Failed to build the IP core. Details:\n\t{}".format(e))
        return _built

    def decode_file(self, ipc_fname: str, *, to_str=False) -> str | bytes:
        if ipc_fname not in self._ipc['files']:
            raise Exception("File not found: {} in ipc.files:{}".format(ipc_fname, self._ipc['files'].keys()))
        _target = self._ipc['files'][ipc_fname]
        if _target is None:
            return "" if to_str else b""
        bs: bytes = files.loads(self._ipc['files'][ipc_fname])
        if to_str:
            return bs.decode('utf-8')
        return bs

    def __get_f(self, skey, *, unzip=True, to_str=False):
        """
        Get the content of the file.
        :param skey: str, the key of the file.
        :param unzip: bool, whether to unzip the file.
            * If True, only the first file in the zip file is returned.
            * If False, the zip file bytes is returned.
        :param to_str: bool, whether to decode the bytes to str. only works when unzip is True.
        """
        _zip_bs = files.loads(self.f[self.key, skey])

        if not unzip:
            return _zip_bs

        _bs = unziptarget(_zip_bs)
        if to_str:
            return auto_decode(_bs)
        return _bs

    # ----------------------------------------- Following are properties -----------------------------------------

    @property
    def name(self):
        return self.fmd.name

    @property
    def author(self):
        if self._header.get('author'):
            return self._header['author']
        flst = FList()
        flst.login(IPC_AUTHOR_VID, *IPC_AUTHOR_GS)
        flst.handle(self.built)
        return flst[0] if len(flst) else "Unknown"

    @property
    def content(self):
        """Return the content of the IP core."""
        if self._content is None:
            self._content = self.__get_f('fmain', to_str=True)
        return self._content

    @property
    def pixmap(self) -> QPixmap:
        if self.f[self.key, 'ficon'] is None:
            return QPixmap()
        return QPixmap.fromImage(QImage.fromData(self.__get_f('ficon')))

    @property
    def icon(self) -> QIcon:
        return QIcon(self.pixmap)

    @property
    def readme(self) -> str:
        return self.__get_f('freadme', to_str=True)

    @property
    def manual(self) -> bytes:  # 获取pdf的bytes内容
        return self.__get_f('fmanual')

    @property
    def ipcname(self):
        return self._header['name']

    @property
    def brand(self):
        return self._header['brand']

    @property
    def model(self):
        return self._header['model']

    @property
    def board(self):
        return self._header['board']

    @property
    def group(self):
        return self._header['group']

    @property
    def readonlys(self) -> list[str]:  # 识别被readonly修饰的参数
        return self._mono.readonlys

    def __inner_build_subs_handler(self, unziped_fpath:str):
        """
        Build the sub files.
        :param unziped_fpath: str, the path of the unzipped file.
        """
        # check type
        if os.path.isdir(unziped_fpath):
            for root, dirs, files in os.walk(unziped_fpath):
                for file in files:
                    # 创建文件的完整路径
                    file_path = os.path.join(root, file)
                    # 递归处理
                    self.__inner_build_subs_handler(file_path)
        else:
            # 试图以文本方式打开文件
            entype = auto_encoding(unziped_fpath, 0.9)
            if entype is None:
                return  # 无法识别编码，不处理
            s = auto_open(unziped_fpath)
            if s is None:
                return  # 无法以文本方式打开，不处理
            # 处理文本
            s = self._mono.slaveHandle(s)
            # 保存
            with open(unziped_fpath, 'w', encoding=entype) as f:
                f.write(s)


    def buildsubs(self, target_dir, overwrite=False):
        # read & check
        _f3bs_subs = self.f[self.key, 'fsubs']
        if _f3bs_subs is F3False:
            raise Exception(f"ipcore.buildsubs: Failed to load the file: {self.key}.fsubs")

        # unzip
        for i, _f3bs in enumerate(_f3bs_subs):
            zipf = files.unpack(_f3bs)  # zipfile
            _paths = []  # 解压后的文件路径

            # 解压文件并获得文件路径
            for _name in zipf.namelist():
                _path = os.path.join(target_dir, _name)
                if not overwrite and os.path.exists(_path):
                    raise FileExistsError("ipcore.buildsubs: File already exists: {}".format(_path))
                with open(_path, 'wb') as f:
                    f.write(zipf.read(_name))
                _paths.append(_path)

            # 遍历这些路径及其文件
            for _path in _paths:
                self.__inner_build_subs_handler(_path)

    def buildothers(self, target_dir, overwrite=False):
        # read & check
        _f3bs_others = self.f[self.key, 'fothers']
        if _f3bs_others is F3False:
            raise Exception(f"ipcore.buildothers: Failed to load the file: {self.key}.fothers")

        # unzip
        for i, _f3bs in enumerate(_f3bs_others):
            try:
                files.unpack(_f3bs, target_dir, overwrite=overwrite, error=True)
            except FileExistsError as e:
                raise FileExistsError("ipcore.buildothers: File already exists: {}".format(e))

    def export(self, target_dir, *, spec_name:str=None, overwrite=False):
        """
        Export the IP core to the target directory.
        :param target_dir: str, the target directory.
        :param overwrite: bool, whether to overwrite the existing files.
        """
        # check
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        if not os.path.isdir(target_dir):
            raise Exception("Target directory is not a directory: {}".format(target_dir))

        # export main
        spec_name = spec_name if spec_name else (self.name + ".v")
        spec_name = spec_name if spec_name.endswith('.v') else (spec_name + ".v")
        _target = os.path.join(target_dir, spec_name)
        with open(_target, 'w', encoding='utf-8') as f:  # main内容必然可以覆盖
            f.write(self.built)

        # export subs
        try:
            self.buildsubs(target_dir, overwrite=overwrite)
        except FileExistsError as e:
            raise FileExistsError("ipcore.export: File already exists: {}".format(e))

        # export others
        try:
            self.buildothers(target_dir, overwrite=overwrite)
        except FileExistsError as e:
            raise FileExistsError("ipcore.export: File already exists: {}".format(e))

    # 获取参数名称
    @property
    def keys(self):
        """Return the parameters of the IP core."""
        return self._mono.keys

    @property
    def dict(self):
        """Return the parameters of the IP core."""
        return self._mono.dict

    def get_inspector(self, skip_update=False, **params):
        if not skip_update:
            self._mono.handle(self.content, **params)
        w = QMonoInspector(self._mono)
        return w

    @classmethod
    def GetInspector(cls, content:str, **params):
        mono = cls._build_mono()
        mono.handle(content, **params)
        w = QMonoInspector(mono)
        return w

    @property
    def monos(self):
        return self._mono.monos

    @property
    def types(self) -> dict:
        return self._mono.types

    @property
    def separators(self):
        # if self._separators is None:
        flst = FList()
        flst.login(IPC_VIEW_VID, *IPC_VIEW_SEP)
        flst.handle(self.built)
        # self._separators = flst
        return flst
        # return self._separators

    @property
    def lefts(self):
        # if self._lefts is None:
        flst = FList()
        flst.login(IPC_LR_VID, *IPC_LEFT_GS)
        flst.handle(self.built)
        # self._lefts = flst
        return flst
        # return self._lefts

    @property
    def rights(self):
        # if self._rights is None:
        flst = FList()
        flst.login(IPC_LR_VID, *IPC_RIGHT_GS)
        flst.handle(self.built)
        # self._rights = flst
        return flst
        # return self._rights

    @property
    def icode(self):
        """
        Get the instance code of the IP core.
        * Cost lots of time.
        :return:
        """
        header = builder_info(self.author)
        try:
            pure_inst_code = self.fmd.create_module_inst_code()
        except Exception as e:
            pure_inst_code = f"// Failed to create instance code. Details:\n// {e}\n"
        self._last_icode = header + pure_inst_code
        return self._last_icode

    @property
    def last_icode(self):
        return self._last_icode

    @property
    def raw_ports(self) -> list[Input, Output]:
        return self.fmd.ports

    @property
    def ports(self) -> list[dict]:
        return [self.fmd.ioport_to_dict(i) for i in self.fmd.ports]

    @property
    def raw_inputs(self) -> list[Input]:
        return self.fmd.inputs

    @property
    def inputs(self) -> list[dict]:
        return [self.fmd.ioport_to_dict(i) for i in self.fmd.inputs]

    @property
    def raw_outputs(self) -> list[Output]:
        return self.fmd.outputs

    @property
    def outputs(self) -> list[dict]:
        return [self.fmd.ioport_to_dict(i) for i in self.fmd.outputs]

    @property  # TODO: 解决Icode不根据param改变而更新的问题
    def built(self):
        if self._built is None:
            self.build()
        return self._built

    @property
    def fmd(self):
        if self._fmd is None:
            self.build(**self.dict)
        return self._fmd


if __name__ == '__main__':
    # # raise
    app = QApplication([])
    vfile = r"H:\FPGA_Learns\04 ClockDiv\src\clockdiv-n.v"
    content = auto_open(vfile)
    result = IpCore.Build(content)
    print(result)
    w = IpCore.GetInspector(content)
    w.show()
    app.exec_()
