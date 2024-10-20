import os
import re
import time
import enum
import typing
import threading
from pyipcore.utils import *
from datetime import datetime

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from reft import *
from reft.ft import FTMatched

VERSION = "0.4.34"
GITEE_URL = "https://gitee.com/eagle-s_baby/pyipcore"
APP_NAME = "Py IP-Core Wizard"

IPC_SUFFIX = '.ipc'

V_SUFFIXS = ['.v', '.sv']

OPEN_TYPE = "Verilog (*.v);;SystemVerilog (*.sv);;IP Core (*.ipc)"
SAVE_TYPE = "IP Core (*.ipc);;Verilog (*.v);;SystemVerilog (*.sv)"

VERILOG_TYPE = "Verilog (*.v);;SystemVerilog (*.sv)"

# 读取作者// @AUTHOR:
IPC_AUTHOR_GS = [
    "//+\s*@\s*AUTHOR:\s*",  # 0 "// @AUTHOR: "
    "[^;/\s]+",  # 1 " ... ... "
]
IPC_AUTHOR_VID = 1  # value index in IPC_AUTHOR_GS

# 读取绘制模块时添加间隔 例如: // #a
IPC_VIEW_SEP = [
    "//+\s*\#",  # 0 "// "
    "[^;/\s]+",  # 1 " ... ... "
]
IPC_VIEW_VID = 1  # value index in IPC_VIEW_SEP
IPC_LEFT_GS = [
    "//+\s*<",  # 0 "// <"
    "[^;/\s]+",  # 1 " ... ... "
]
IPC_RIGHT_GS = [
    "//+\s*>",  # 0 "// >"
    "[^;/\s]+",  # 1 " ... ... "
]
IPC_LR_VID = 1  # value index in IPC_LEFT_GS and IPC_RIGHT_GS

FSV = files(type=".sets", sub_type=".svitem")
FSV['sv'] = "Ipcore Setting"

def get_current_username():
    try:
        # Unix and Linux
        return os.getlogin()
    except OSError:
        import getpass
        # Windows
        return getpass.getuser()


def builder_info(author):
    return f"// Created by software {APP_NAME} \n// Software version {VERSION}\n" \
           f"// Author: {author}\n// Creator: {get_current_username()}\n// Created time: {created_time()}\n\n"


def created_time():
    # 获取当前时间
    now = datetime.now()
    # 格式化时间字符串
    created_time = now.strftime("%a %b %d %H:%M:%S %Y")
    return created_time


def get_lib_path():
    """Return the absolute path of the library."""
    # read lib_path from files
    f = files(os.getcwd())
    lib_path = f.get("lib_path")
    if lib_path is F3False:
        return os.getcwd()
    return lib_path


from pyverilog.vparser.parser import parse as verilog_parse
from pyverilog.vparser.ast import ModuleDef, Input, Inout, Output, IntConst, Minus, Plus


def get_str_value(var):
    """
    获取str类型的值
    :param var: IntConst
    :return: str
    """
    if var is None:
        return ""
    elif isinstance(var, IntConst):
        return var.value
    elif isinstance(var, Minus):
        return "-" + get_str_value(var.left)

# 定义超时返回的常量
class TIMEOUT_QRET:
    ...

class IVerilogParseTimeoutError(Exception):
    pass

class IVerilogParseError(Exception):
    pass

class LimitThread(threading.Thread):
    def __init__(self, target, args, kwargs, *, on_error=None):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.on_error = on_error
        self.result = None
        self.error = None
        self._start_time = None
        self._done_flag = False


    def run(self):
        try:
            self.result = self.target(*self.args, **self.kwargs)
        except Exception as e:
            if self.on_error:
                self.on_error(e)
            self.error = e
        self._done_flag = True

    def start(self):
        self._start_time = time.time()
        super().start()

    def wait(self, limit_time:int):
        if self._start_time is None:
            raise Exception("Thread not started.")

        while (time.time() - self._start_time) < limit_time:
            time.sleep(0.25)
            if self._done_flag:
                return self.result
        return TIMEOUT_QRET

def limitStart(target, args, kwargs, limit_time:int, *, on_error=None):
    thread = LimitThread(target, args, kwargs, on_error=on_error)
    thread.start()
    res = thread.wait(limit_time)
    if thread.error:
        raise TIMEOUT_QRET
    return res

def get_module_parameters(param_s) -> dict:
    """
    获取module的参数
    :param param_s: module.paramlist.show() txt
        @example:
        parameter WIDTH = GLOBAL_SET * 1,
        parameter RCO_WIDTH = 4
    :return: dict {name: value}
    """
    rslt = {}

    def _sub_fn(matched):
        # get groups
        name, value = matched.group(1), matched.group(2)
        rslt[name] = value

    # group1: name, group2: value
    pat = re.compile(fr"parameter\s+({FT.VARIABLE})\s*=\s*([^,^\n,^(parameter)]+)")

    re.sub(pat, _sub_fn, param_s)

    return rslt


def get_module_ports(ports_s) -> dict:
    """
    获取module的端口
    :param ports_s: module.portlist.show() txt
        @example:
        input clk,
        input nrst,
        input en,
        input [WIDTH-1:0] i_cmp,
        output reg [WIDTH-1:0] o_cnt,
        output o_rco
    :return: dict {name: (direction:str, prefix:str, width:str)}
    """
    rslt = {}

    def _sub_fn(matched):
        # get groups
        direction, prefix, width, name = matched.group(1), matched.group(2), matched.group(3), matched.group(4)
        # 除了name和direction, 其他都可能为None
        if prefix is None:
            prefix = ""
        if width is None:
            width = ""
        # 移除每个元素末尾的\s*
        prefix = prefix.rstrip()
        width = width.rstrip()

        rslt[name] = (direction, prefix, width)

    # group1: direction, group2: prefix, group3: width, group4: name
    pat = re.compile(fr"(input|output|inout)\s+(reg|wire|logic)?\s*(\[[^\]]+\]\s+)?({FT.VARIABLE})(,\s*)?")

    re.sub(pat, _sub_fn, ports_s)

    return rslt


class StdoutString:
    def __init__(self):
        self.content = ""

    def write(self, txt):
        self.content += txt

    def flush(self):
        pass

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.conten


def show(node) -> StdoutString:
    """
    显示ast的内容
    :param node: ast
    :return: StdoutString
    """
    ss = StdoutString()
    node.show(buf=ss, attrnames=True, showlineno=False)
    return ss


from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

class ThirdToolIVerilogNotFound(Exception):
    pass

def extract_to_module_def_txt(txt: str) -> str:
    """
    从txt中提取module的定义部分
    """

    current_idx = 0
    spec_sv = {}  # 把不属于verilog的部分放到这里，$SPEC_SV_{i}$: sv code
    new_txt = ""
    for line in txt.split("\n"):
        # 1. remove typedef
        if line.find("typedef") != -1:
            key = f"$SPEC_SV_{current_idx}$"
            spec_sv[key] = line
            # new_txt += key + "\n"  # 暂时不添加
            current_idx += 1
            continue
        new_txt += line + "\n\n"
    txt = new_txt

    # remove all between ');' and 'endmodule'
    pat = re.compile("\)\s*;")
    new_txt = ""
    left_txt = txt
    while True:
        matched = pat.search(left_txt)
        if matched is None:
            break
        start, end = matched.span()

        # find the endmodule
        endmodule_idx = left_txt.find("endmodule")
        if endmodule_idx == -1:
            raise ValueError("Can't find 'endmodule' after ');'.")
        new_txt += left_txt[:end] + "\nendmodule\n"
        left_txt = left_txt[endmodule_idx + len("endmodule"):]
    new_txt += left_txt
    txt = new_txt

    # remove more \n
    txt = re.sub(r"\n\n+", "\n", txt)

    # logic -> reg
    txt = re.sub(r"\blogic\b", "reg", txt)

    return txt  # , spec_sv


def parse_to_module_def(module_def_txt: str) -> ModuleDef:
    # def _inner_on_error(e):
    #     with open("parsed~.v", "w", encoding="utf-8") as f:
    #         f.write(module_def_txt)
    #     raise IVerilogParseError(f"Failed to parse the verilog code. Details:\n\t{e}\n\nThe input code has been saved to 'parsed~.v'.")
    try:
    #     res = limitStart(verilog_parse, ([module_def_txt],), {"debug":True}, 8, on_error=_inner_on_error)
    #     if res == TIMEOUT_QRET:
    #         raise IVerilogParseTimeoutError("Timeout to parse the verilog code.")
        ast, _ = verilog_parse([module_def_txt], debug=False)
    except Exception as err:
        if isinstance(err, FileNotFoundError):
            pre_found_error = "[WinError 2]"
            if str(err).find(pre_found_error) != -1:
                raise ThirdToolIVerilogNotFound("Please retry after install 'iverilog' from 'http://bleyer.org/icarus/' and add it to path.")
            raise err
        else:
            with open("parsed~.v", "w", encoding="utf-8") as f:
                f.write(module_def_txt)
            raise IVerilogParseError(f"Failed to parse the verilog code. Details:\n\t{err}\n\nThe input code has been saved to 'parsed~.v'.")

    for description in ast.children():
        if description.definitions:
            for def_code in description.definitions:
                if isinstance(def_code, ModuleDef):
                    return def_code
    return None


@enum.unique
class Direction(enum.StrEnum):
    IN = 'input'
    OUT = 'output'
    INOUT = 'inout'

@enum.unique
class IoType(enum.StrEnum):
    V12 = 'v12'
    V15 = 'v15'
    V18 = 'v18'
    V25 = 'v25'
    V33 = 'v33'

@enum.unique
class Pull(enum.StrEnum):
    FLOAT = 'float'
    UP = 'up'
    DOWN = 'down'



class IoDefRecord:  # just raw record.
    _LOCKED = False
    _CURRENT_INSTANCE = None
    @staticmethod
    def _name_ft_callback(premulti, mainbody, index:FTMatched):
        if not IoDefRecord._CURRENT_INSTANCE:
            raise ValueError("IoDefRecord: _CURRENT_INSTANCE is None")
        if premulti:
            for each in re.split(r'[.:]', str(premulti)):
                if each:
                    IoDefRecord._CURRENT_INSTANCE._name_gs.append(each)
        IoDefRecord._CURRENT_INSTANCE._name_gs.append(str(mainbody))
        if index:
            IoDefRecord._CURRENT_INSTANCE._name_gs.append(int(index[1:]))
        return ''

    NAME_GS = [
        f"({FT.VARIABLE}[.:])*",
        f"{FT.VARIABLE}",
        f"([.:]{FT.INTEGER})?",
    ]

    VIDS = [0, 1, 2]

    _NAME_FT = FT()
    _NAME_FT.login(_name_ft_callback, *NAME_GS, areas=VIDS)

    def __init__(self,
                 pin:str=None, name:str=None,
                 direction:Direction=Direction.IN,
                 iotype:IoType=IoType.V33,
                 pull:Pull=Pull.FLOAT,
                 note:str="", **other_kvs
                 ):

        self.pin = pin
        self.name = name
        # self._name_gs = []
        # self._startwith = ""
        self.direction = direction
        self.iotype = iotype
        self.pull = pull
        self.note = note
        self.others:dict = other_kvs


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value:str):
        while IoDefRecord._LOCKED:
            time.sleep(0.1)
        IoDefRecord._LOCKED = True

        # 第一个字符决定一些特殊属性
        if value and value[0] in ['_', '*']:
            self._startwith = value[0]
            value = value[1:]
        else:
            self._startwith = ''

        # body
        self._name = value
        self._name_gs = []
        IoDefRecord._CURRENT_INSTANCE = self
        self._NAME_FT.handle(value)

        IoDefRecord._LOCKED = False

    @property
    def stared(self):
        return self._startwith == '*'

    @property
    def hiden(self):
        return self._startwith == '_'

    @property
    def startwith(self):
        return self._startwith

    @property
    def namegs(self):
        return self._name_gs

    @namegs.setter
    def namegs(self, value:list[str|int]):
        assert isinstance(value, list), "IoDefRecord:namegs should be a list"
        self._name = '.'.join(value)
        self._name_gs = value

    def __str__(self):
        return f"<'{self.pin}':{self._startwith}'{self.name}' | {self.direction} {self.iotype} {self.pull}>" + (f" # {self.note}" if self.note else "")

    def __repr__(self):
        return f"<'{self.pin}':{self._startwith}'{self.name}'>"

class PhysicsIoDef: ...
class PhysicsIoDef(PhysicsIoDef):
    @staticmethod
    def _combine_single(one_single_rec:list[IoDefRecord]) -> PhysicsIoDef:
        length = len(one_single_rec)
        if length == 0:
            raise ValueError("PhysicsIoDef:pio group is empty")

        d0, iot0, p0, s0 = one_single_rec[0].direction, one_single_rec[0].iotype, one_single_rec[0].pull, one_single_rec[0].startwith

        one_single_rec.sort(key=lambda x: x.namegs[-1])
        sorted = one_single_rec
        for i, rec in enumerate(sorted):
            if i != rec.namegs[-1]:
                raise ValueError("PhysicsIoDef:pio group contains non-continuous index\n\npios:{}".format(sorted))
            if rec.direction != d0 or rec.iotype != iot0 or rec.pull != p0 or rec.startwith != s0:
                raise ValueError("PhysicsIoDef:pio group contains pio with different properties\n\npios:{}".format(sorted))

        pins = [rec.pin for rec in sorted]
        name = '.'.join(rec.namegs[:-1])
        note = '|'.join(rec.note for rec in sorted)

        return PhysicsIoDef(
            pins, name=name,
            direction=d0, width=length,
            iotype=iot0, pull=p0,
            namegs=rec.namegs[:-1], note=note,
            startwith=s0
        )


    @staticmethod
    def _bundle_singles(singles:list[IoDefRecord])-> list[PhysicsIoDef]:
        """
        归并所有多位宽的pio，返回一个新的pio列表
        内部第一个列表是孤立的单个pio，此时将其namegs[-2]+str(namegs[-1])作为namegs[-2]，namegs[-1]被移除
        内部第二个列表是多位宽的pio组。
        """
        module_path_dict = {}  # key:module_path_tuple #(namegs[:-1]), value:pio list
        iso_recs, iso_pios, combines = [], [], []


        for pio in singles:
            if not isinstance(pio.namegs[-1], int):
                iso_recs.append(pio)
                continue
            module_path = tuple(pio.namegs[:-1])
            if module_path in module_path_dict:
                module_path_dict[module_path].append(pio)
            else:
                module_path_dict[module_path] = [pio]

        # combine
        for module_path, recs in module_path_dict.items():
            if len(recs) == 1:
                rec = recs[0]
                rec.name = '.'.join(rec.namegs[:-2]) + str(rec.namegs[-1])
                iso_recs.append(rec)
            else:
                combines.append(PhysicsIoDef._combine_single(recs))

        for rec in iso_recs:
            iso_pios.append(PhysicsIoDef(
                rec.pin, name=rec.name,
                direction=rec.direction,
                iotype=rec.iotype, pull=rec.pull,
                namegs=rec.namegs, note=rec.note,
                startwith=rec.startwith
            ))

        return iso_pios + combines

    @staticmethod
    def FromTableDict(dlst:list[dict]) -> list[PhysicsIoDef]:
        """
        你需要构造N个字典，包含以下字段：
        *'pin':str,  # 只包含一个引脚
        *'name':str,
        *'direction':Direction,
        *'iotype':IoType,
        *'pull':PullMode,
        'note':str,
        """
        iodrs = []
        for d in dlst:
            assert 'pin' in d, "PhysicsIoDef:missing 'pin' in dict:{}".format(d)
            assert 'name' in d, "PhysicsIoDef:missing 'name' in dict:{}".format(d)
            assert 'direction' in d, "PhysicsIoDef:missing 'direction' in dict:{}".format(d)
            assert 'iotype' in d, "PhysicsIoDef:missing 'iotype' in dict:{}".format(d)
            assert 'pull' in d, "PhysicsIoDef:missing 'pull' in dict:{}".format(d)
            note = d.get('note', "") or ""
            iodrs.append(IoDefRecord(d['pin'], d['name'], d['direction'], d['iotype'], d['pull'], note))

        return PhysicsIoDef._bundle_singles(iodrs)


    def __init__(self,
                 pins:str|list[str], name:str,  # pins的顺序按照从低位到高位
                 direction=Direction.IN,
                 width=1,  # None|0|1 mean 1
                 iotype=IoType.V33,
                 pull=Pull.FLOAT,* ,namegs=None, note:str="", startwith:str=""):
        self._pins = pins if isinstance(pins, list) else [pins]
        self._name = name
        self._width = None
        self._startwith = startwith
        self.width = width
        self.direction = direction
        self.iotype = iotype
        self.pull = pull
        self.note = note

        if not namegs:
            _name_ft = FT()
            _name_ft.login(self._name_ft_callback, *NAME_GS, areas=VIDS)
            self._name_gs = []
            _name_ft.handle(name)
        else:
            self._name_gs = namegs


    def _name_ft_callback(self, premulti, mainbody, index:FTMatched):
        if premulti:
            for each in re.split(r'[.:]', str(premulti)):
                if each:
                    self._name_gs.append(each)
        self._name_gs.append(str(mainbody))
        if index:
            self._name_gs.append(int(index[1:]))
        return ''

    @property
    def name(self) -> str:
        return self._name

    @property
    def plain_name(self) -> str:
        return '_'.join(self._name_gs)

    @property
    def stared(self) -> bool:
        return self._startwith == '*'

    @property
    def hiden(self) -> bool:
        return self._startwith == '_'

    @property
    def namegs(self) -> list[str|int]:
        return self._name_gs

    @property
    def width(self) -> int:
        return self._width

    @property
    def widthdef(self) -> str:
        if self._width and self._width > 1:
            return f"[{self._width - 1}:0]"
        return ""

    @property
    def voltage(self) -> str:
        return f"{self.iotype[1]}.{self.iotype[2]}"

    @width.setter
    def width(self, value):
        if value is None:
            self._width = 1
        elif value == 0:
            self._width = 1
        else:
            self._width = value

    @property
    def pins(self):
        return tuple(self._pins)

    @property
    def rpins(self):
        return tuple(reversed(self._pins))

    def todict(self, *, list=False) -> dict|list[dict]:
        res = []
        for i, pin in enumerate(self.pins):
            _ = {}
            _['pin'] = pin      # 例如 'A1'  '17'  # 具体要看是什么芯片
            _['name'] = self.plain_name   # 例如 'clk'  'DDR_BA0'
            if self._width and self._width > 1:
                _['idxname'] = f"{self.plain_name}[{i}]"  # 例如 'clk'(没有width)    'DDR_D[1]'(有width)
            else:
                _['idxname'] = self.plain_name
            _['index'] = str(i)
            _['iotype'] = self.iotype.lower()       # 例如 'v33'  'v18' 'v12' ...
            _['direct'] = self.direction.lower()        # 例如 'input' 'output' 'inout'
            _['pull'] = self.pull.lower()       # 例如 'float'  'up' 'down'
            _['note'] = self.note       # str
            _['width'] = str(self.width)     #
            _['startwith'] = self._startwith  # 例如 '*'  '_'  '^'  # 用于标记特殊的信号
            _['voltage'] = self.voltage     # 例如 '3.3'  '1.8' '1.2' ...
            res.append(_)

        if len(res) == 1 and not list:
            return res[0]
        return res

    @classmethod
    def todoc(cls) -> str:
        doc_lines = [
            "// pin: str - Pin identifier, e.g., 'A1', '17'",
            "// name: str - Human-readable name, e.g., 'clk', 'DDR_D'",
            "// idxname: str - Indexed name if width > 1, e.g., 'clk', 'DDR_D[1]'",
            "// index: str - Index of the pin, e.g., '0', '1'",
            "// iotype: str - I/O type, e.g., 'v33', 'v18', 'v12'",
            "// direct: str - Direction of the pin, e.g., 'input', 'output', 'inout'",
            "// pull: str - Pull type, e.g., 'float', 'up', 'down'",
            "// note: str - Additional note about the pin",
            "// width: str - Width of the pin, e.g., '1', '32'",
            "// startwith: str - Character that the name starts with, e.g., '*', '_', '^'",
            "// voltage: str - Voltage level, e.g., '3.3', '1.8', '1.2'"
        ]
        return "\n".join(doc_lines)

    def __str__(self):
        return (f"<'{self.rpins}':{self._startwith}'{self.name}"
                f"{('[' + str(self._width - 1) + ':0]') if self._width and self._width > 1 else ''}'"
                f" | {self.direction} {self.iotype} {self.pull}>")

    def __repr__(self):
        return f"<'{self.rpins}':{self._startwith}'{self.name}'>"


class LogicIoDef(PhysicsIoDef): ...
class LogicIoDef(LogicIoDef):
    @staticmethod
    def FromTableDict(dlst:list[dict]) -> list[LogicIoDef]:
        """
        你需要构造N个字典，包含以下字段：
        *'name':str,
        *'direction':Direction,
        *'iotype':IoType,
        *'pull':PullMode,
        'note':str,
        """
        iodrs = []
        for d in dlst:
            assert 'name' in d, "LogicIoDef:missing 'name' in dict:{}".format(d)
            assert 'direction' in d, "LogicIoDef:missing 'direction' in dict:{}".format(d)
            assert 'iotype' in d, "LogicIoDef:missing 'iotype' in dict:{}".format(d)
            assert 'pull' in d, "LogicIoDef:missing 'pull' in dict:{}".format(d)
            note = d.get('note', "")
            iodrs.append(IoDefRecord(None, d['name'], d['direction'], d['iotype'], d['pull'], note))

        ios = LogicIoDef._bundle_singles(iodrs)
        return [LogicIoDef(pio.name, pio.direction, pio.width, pio.iotype, pio.pull, namegs=pio.namegs, note=pio.note) for pio in ios]

    # not pins
    def __init__(self, name:str, direction=Direction.IN, width=1, iotype=IoType.V33, pull=Pull.FLOAT, *, namegs=None, note:str=""):
        super().__init__(None, name, direction, width, iotype, pull, namegs=namegs, note=note)

    def __str__(self):
        return f"<logic '{self.name}{('[' + str(self._width - 1) + ':0]') if self._width else ''}' | {self.direction} {self.iotype} {self.pull}>"

    def __repr__(self):
        return f"<logic '{self.name}'>"

class FirstModuleDef:
    def __init__(self, verilog_code: str):
        self.verilog_code = verilog_code
        self.module_def_code = extract_to_module_def_txt(verilog_code)
        # print("finish extract_to_module_def_txt")
        self.module_def = parse_to_module_def(self.module_def_code)
        # print("finish parse_to_module_def")

        if self.module_def is None:
            raise ModuleNotFoundError("Can't find module definition in the verilog code: \n\n" + verilog_code[:100] + "\n...")

    @property
    def paramlist(self):
        return self.module_def.paramlist

    @property
    def portlist(self):
        return self.module_def.portlist

    @property
    def ports(self):
        return list(self.module_def.portlist.ports)

    @property
    def inputs(self):
        return [item for item in self.module_def.portlist.ports if isinstance(item.first, Input)]

    @property
    def outputs(self):
        return [item for item in self.module_def.portlist.ports if isinstance(item.first, Output)]

    @property
    def name(self):
        return self.module_def.name

    @staticmethod
    def ioport_to_dict(ioport) -> dict:
        """
        将ioport转换为dict, 包含:
        - name: str
        - direction: str
        - prefix: str
        - width: str
        :param ioport: ioport
        :return: dict
        """
        name = ioport.first.name
        direction = ioport.first.__class__.__name__.lower()
        if ioport.first.width:
            _msb, _lsb = get_str_value(ioport.first.width.msb), get_str_value(ioport.first.width.lsb)
            if _msb is None or _lsb is None:
                raise ValueError(f"Can't get correct msb or lsb from {ioport.first.width}. Got msb={_msb}, lsb={_lsb}")
            width = f"[{_msb}:{_lsb}]"
            w = 1 + int(_msb) - int(_lsb)
        else:
            width = ""
            w = 1
        if ioport.second:
            prefix = ioport.second.__class__.__name__.lower()

        else:
            prefix = "wire"
            # width = ""
            # w = 1

        return {
            "name": name,
            "direction": direction,
            "prefix": prefix,
            "width": width,
            "w": w
        }

    def create_module_inst_code(self) -> str:
        """
        生成verilog module模块的实例代码
        """
        codegen = ASTCodeGenerator()
        rslt = codegen.visit(self.paramlist)
        params = get_module_parameters(rslt)

        ports = [self.ioport_to_dict(port) for port in self.ports]

        # build wire declarations
        wire_decls = ""
        for port in ports:
            if port['w'] > 1:
                wire_decls += f"\twire {port['width']} {port['name']};\n"
            else:
                wire_decls += f"\twire {port['name']};\n"

        # build inst code
        ic = f"\t{self.name} " + ("#(\n" if params else "")  # module name
        # add parameters
        for k, v in params.items():
            ic += f"\t\t.{k}({v}),\n"
        if params:
            ic = ic[:-2] + "\n"
        ic += ("\t) " if params else "") + f"{self.name.lower()}_inst (\n"
        # add ports
        for port in ports:
            if port['w'] > 1:
                ic += f"\t\t.{port['name']}({port['name']}),  // {port['width']} \n"
            else:
                ic += f"\t\t.{port['name']}({port['name']}),\n"

        ic = ic[:-2] + "\n"
        ic += "\t);"

        # combine wire declarations and inst code
        return f"//--------Copy here to design-------- \n{wire_decls}\n{ic}\n//--------Copy end-------------------\n"
