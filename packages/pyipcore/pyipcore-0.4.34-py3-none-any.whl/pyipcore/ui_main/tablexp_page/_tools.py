from pyipcore.ipc_utils import *
from reft import FT, FTMatched
import pandas as pd


def DFtoDict(df: pd.DataFrame) -> list[dict]:
    """
    将DataFrame转换为字典列表
    """
    res = df.to_dict(orient='records')
    # remove NaN to None
    for i in res:
        for k, v in i.items():
            if pd.isna(v):
                i[k] = None
    return res

def DFLowerHeader(df: pd.DataFrame) -> pd.DataFrame:
    """
    将DataFrame的表头转换为小写
    """
    df.columns = [col.lower() for col in df.columns]
    return df

class MatrixArrayReadError(Exception):
    pass

def MatrixArrayRead(
        tbl: pd.DataFrame,      # 读取的excel时最好忽略header和index
        offset: tuple[int, int],  # 忽略起始的若干列和行，即(offx, offy)
        target: tuple[int, int],  # 目标‘矩阵’的宽和高
        delta: tuple[int, int],  # 矩阵的间隔
        *,
        header: bool = True,  # 描述target的第一行是否是表头  # 如果是表头，要检查每个表头是否一致
        index: bool = True    # 描述target的第一列是否是索引
) -> pd.DataFrame:  # 将所有target纵向拼接.
    # 切换为pd格式
    offset = (offset[1], offset[0])
    target = (target[1], target[0])
    delta = (delta[1], delta[0])

    _shape = tbl.shape
    # 计算shape可以容纳的矩阵数量
    _full_size = (target[0] + delta[0], target[1] + delta[1])

    # 计算可以提取的矩阵数量
    num_matrices_x = (_shape[1] + 1 - offset[1] + delta[1]) // _full_size[1]
    num_matrices_y = (_shape[0] + 1 - offset[0] + delta[0]) // _full_size[0]

    matrices, _m0 = [], None

    for y in range(num_matrices_y):
        for x in range(num_matrices_x):
            start_x = offset[1] + x * _full_size[1]
            start_y = offset[0] + y * _full_size[0]
            end_x = start_x + target[1]
            end_y = start_y + target[0]

            # 提取矩阵
            matrix:pd.DataFrame = tbl.iloc[start_y:end_y, start_x:end_x]
            tmp = str(matrix)

            #header & column
            if header:
                columns = matrix.iloc[0].tolist()
                matrix = matrix.iloc[1:]
                matrix.columns = columns
            if index:
                matrix = matrix.reset_index(drop=True)
            tmp = str(matrix)

            # 记录首个元素
            if not matrices:
                _m0 = set(matrix.columns.tolist())

            # 如果需要检查表头一致性
            if header and matrices:
                _this = set(matrix.columns.tolist())
                if _this != _m0:
                    raise MatrixArrayReadError(f"MatrixArrayRead: 表头不一致: at x={x}, y={y}:\n{_this}\n{_m0}")

            # # 如果需要检查索引列
            # if index and x > 0:
            #     if not pd.Series.equals(matrices[0].iloc[:, 0], matrix.iloc[:, 0]):
            #         raise ValueError("索引列不一致")

            matrices.append(matrix)

    if not matrices:
        raise MatrixArrayReadError("MatrixArrayRead: 未提取到任何矩阵")

    # 将所有矩阵纵向拼接
    result = pd.concat(matrices, axis=0)
    # 移除整行全为NaN的行
    result = result.dropna(how='all')
    return result


def ReadExcelTables(file: str | pd.ExcelFile, sheets:list[str]) -> dict[pd.DataFrame]:
    """
    读取excel文件中的所有表格
    """
    if isinstance(file, str):
        xls = pd.ExcelFile(file)
    else:
        xls = file
    # return {sheet: xls.parse(sheet, header=None, index_col=None) for sheet in xls.sheet_names}
    if sheets is not None:
        return {sheet: xls.parse(sheet, header=None, index_col=None) for sheet in sheets}
    else:
        return {sheet: xls.parse(sheet, header=None, index_col=None) for sheet in xls.sheet_names}

def tbl_export_read(file: str | pd.ExcelFile,
                    offset: tuple[int, int],  # 忽略起始的若干列和行，即(offx, offy)
                    target: tuple[int, int],  # 目标‘矩阵’的宽和高
                    delta: tuple[int, int],  # 矩阵的间隔
                    *,
                    header: bool = True,  # 描述target的第一行是否是表头  # 如果是表头，要检查每个表头是否一致
                    index: bool = True,  # 描述target的第一列是否是索引
                    sheets: list[str] = None
                    ) -> list[PhysicsIoDef]:
    """
    读取一个excel文件中的表格，并转换为PhysicsIoDef列表

    """
    dfs = ReadExcelTables(file, sheets=sheets)
    result = []
    for tbl in dfs.values():
        _ = MatrixArrayRead(tbl, offset, target, delta, header=header, index=index)
        _ = DFLowerHeader(_)
        _ = DFtoDict(_)
        _ = PhysicsIoDef.FromTableDict(_)
        result.extend(_)

    return result


def EvalCst(txt_tpl:str, piodefs:list[PhysicsIoDef]) -> str:
    def _inner(s, env:dict):
        try:
            _ = eval(str(s), env)
        except Exception as e:
            _env = {k: v for k, v in env.items() if not k.startswith("__")}
            raise ValueError(f"EvalCst: Failed to evaluate '{s}' \n\t:with env: {_env}. \n\t:Details: {e}")
        return str(_)

    txt = PhysicsIoDef.todoc()
    ft = FT()
    ft.login(lambda s: _inner(s, ft.env), "\$", "[^$]+", "\$", areas=[1])
    for pio in piodefs:
        envs = pio.todict(list=True)
        for env in envs:
            ft.env = env
            _ = ft.handle(txt_tpl)
            txt += _
    return txt

def GenerateVerilogTopModule(pins_list:list[PhysicsIoDef], old_code:str=None) -> str:
    module_name = "Top"
    header = f"module {module_name}(\n"
    ports = []

    # 检查旧代码
    usr_code = ''
    if old_code:
        _ = FT.Extract(old_code, f"//\s*UsrCodeHere\s*:{FT.BNN}*\n", f"({FT.ANY_CHAR})+?", "\s*endmodule", areas=[1])
        if _:
            usr_code = str(_[0][0])

    for pio in pins_list:
        dct = pio.todict()
        if isinstance(dct, list):
            dct = dct[0]

        direction = dct.get('direct', 'input')  # 默认为输入
        if direction == 'output':
            a= 0
        name = dct['name']
        if pio.width and pio.width > 1:
            port = f"    {direction} wire [{pio.width - 1}:0] {name},\n"
        else:
            port = f"    {direction} wire {name},\n"
        ports.append(port)

    # 移除最后一个逗号
    ports = ''.join(ports).rstrip(',\n')
    footer = f"\n);\n\n// UsrCodeHere:\n{usr_code}\n\nendmodule\n"

    verilog_code = header + ports + footer
    return verilog_code






if __name__ == '__main__':
    # 调用函数
    result = tbl_export_read("../../IO分配表.xlsx",
                             (0, 1), (6, 30), (0, 2),
                             header=True, index=False,
                             sheets=['CORE'])

    tpl_txt = open(r"H:\FPGA_Learns\00 IPC\_ip_wizard\pyipcore gowin_cst.txt", 'r').read()
    # print(*result, sep='\n')
    # result = EvalCst(tpl_txt, result)
    # print(result)
    cst = EvalCst(tpl_txt, result)
    print(cst)
    result = GenerateVerilogTopModule(result)
    print(result)
