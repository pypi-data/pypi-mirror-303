from pyipcore.ui_main.ui_main import Ui_MainForm
from pyipcore.ui_main.ui_style import UiTool_StyleAdjust
from pyipcore.ipcore import IpCore, IpCoreCompileError
from pyipcore.ui_main.creator_page.ipc_creator import QIpCoreCreator
from pyipcore.ui_main.tablexp_page import QExcelTableExportor
from pyverilog.vparser.parser import ParseError
from pyipcore.ip_module_view import IpCoreView
from pyipcore.ipc_utils import *
from pyipcore.ui_utils import *
from files3 import files
import os.path
import time

class TaskWorker(QThread):
    """
    一个Worker线程，用于处理InstCode的生成。
    具体来说，它会在一个循环中，每隔dt时间，从任务队列中取出一个任务并执行。
    而任务队列中的任务目前可以理解为一个InstCode生成函数。
    """

    def __init__(self, dt=0.2):
        super().__init__()
        self._tasks = []
        self._args = []
        self._flag = True
        self._dt = dt


    def run(self):
        while self._flag:
            if len(self._tasks) > 0:
                task = self._tasks.pop(0)
                args = self._args.pop(0)
                try:
                    _ = task(*args)
                except Exception as e:
                    raise Exception(f"Error: {e.__class__.__name__}: {str(e)}")



            time.sleep(self._dt)

    def add(self, task, *args):
        self._tasks.append(task)
        self._args.append(args)

    def stop(self):
        self._flag = False

    def __bool__(self):
        return self._flag

    def __len__(self):
        return len(self._tasks)


class QInspectorContainer(QWidget):
    def __init__(self, callback, parent=None):
        super(QInspectorContainer, self).__init__(parent)
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self.setLayout(self._layout)
        self._callback = callback
        self._current:QMonoInspector = None
        self._logo = QMonoLogo()
        self._layout.addWidget(self._logo)

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        # 移除先前组件
        if self._current is not None:
            self._layout.removeWidget(self._current)
            del self._current
        else:
            self._layout.removeWidget(self._logo)

        # 赋值为新组件
        self._current = value
        if self._current is not None:
            self._current.paramChanged.connect(self._callback)
            self._layout.addWidget(self._current)
        else:
            self._layout.addWidget(self._logo)


WORKER_ACTIVE_DELTA = 1.0
WORKER_DEACTIVE_DELTA = 3.0
class GUI_Main(QMainWindow):
    onOpen = pyqtSignal(str)  # dir_path.   xxx.ipc  # is a dir
    onClose = pyqtSignal()      # close file, no args
    onIpExport = pyqtSignal(str)  # dir_path  # export to this target
    OnTblExport = pyqtSignal(str)  # dir_path  # export to this target
    def __init__(self):
        super(GUI_Main, self).__init__()
        self.qst = get_qw_setting()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self._render_lock = False
        self.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.load_current_size()
        self.ui.tab_sc.setCurrentIndex(0)

        # 自身的独立UI
        self.initUI()

        # add VarItemWidget into var_layout
        self.var_widget = QInspectorContainer(self._enable_ipcore_generate_update)
        self._need_update_flag = False

        self.ui.gbox_var.layout().addWidget(self.var_widget)

        # close即退出
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)

        # worker
        self.worker = TaskWorker()
        self.worker.start()
        self.worker.dt = WORKER_DEACTIVE_DELTA

        # vars
        self.ipcore:IpCore = None
        self.ip_creator = None
        self.var_dict = {}

        # /// customs
        # \t = 4 spaces
        self.ui.ptxt_rc.setTabStopWidth(4 * 4)
        self.ui.ptxt_cc.setTabStopWidth(4 * 4)
        self.ui.ptxt_ic.setTabStopWidth(4 * 4)
        self.reset_signals()

        # reset ptxt to QVerilogEdit
        self.reset_ptxt_xcs()

        # style change
        UiTool_StyleAdjust.effect(self.ui)

        self._update_lock = False


    @property
    def debug(self):
        return self.ui.action_debug.isChecked()

    @property
    def params(self):
        return self.var_widget.current.params

    def reset_signals(self):
        """
        重新绑定信号槽
        :return:
        """
        self.ui.action_file_open.triggered.connect(self._action_open_file)
        self.ui.action_file_close.triggered.connect(self._action_close_file)
        self.ui.action_file_reload.triggered.connect(self._action_reload_file)
        self.ui.action_file_scs.triggered.connect(self._action_save_current_size)
        self.ui.action_file_quit.triggered.connect(self.close)
        self.ui.action_proj_export.triggered.connect(self._action_export_proj)
        self.ui.action_proj_export_at.triggered.connect(self._action_export_proj_at)
        self.ui.action_help_readme.triggered.connect(lambda: PopInfo("Readme", "请参考README.md"))
        self.ui.action_help_about.triggered.connect(self._action_show_about)
        self.ui.tab_main.currentChanged.connect(self._fit_module_view)


    def _fit_module_view(self, index):
        tab = self.ui.tab_main.widget(index)
        if tab is self.ui.tab_main_body:
            self.ui.ptxt_mv.scale_tofit()

    def reset_ptxt_xcs(self):
        """
        重置代码显示区域为VerilogEditor
        """
        self.ui.horizontalLayout_3.removeWidget(self.ui.ptxt_rc)
        self.ui.ptxt_rc = QVerilogEdit(self.ui.tab_rc)
        self.ui.ptxt_rc.setReadOnly(True)
        self.ui.ptxt_rc.setObjectName("ptxt_rc")
        self.ui.horizontalLayout_3.addWidget(self.ui.ptxt_rc)
        self.ui.horizontalLayout_4.removeWidget(self.ui.ptxt_cc)
        self.ui.ptxt_cc = QVerilogEdit(self.ui.tab_cc)
        self.ui.ptxt_cc.setReadOnly(True)
        self.ui.ptxt_cc.setObjectName("ptxt_cc")
        self.ui.horizontalLayout_4.addWidget(self.ui.ptxt_cc)
        self.ui.horizontalLayout_5.removeWidget(self.ui.ptxt_ic)
        self.ui.ptxt_ic = QVerilogEdit(self.ui.tab_ic)
        self.ui.ptxt_ic.setReadOnly(True)
        self.ui.ptxt_ic.setObjectName("ptxt_ic")
        self.ui.horizontalLayout_5.addWidget(self.ui.ptxt_ic)
        self.ui.horizontalLayout_2.removeWidget(self.ui.ptxt_mv)
        self.ui.ptxt_mv = IpCoreView(self.ui.tab_mv)
        self.ui.horizontalLayout_2.addWidget(self.ui.ptxt_mv)


    def initUI(self):
        # menu
        # self.ui._action_proj_export = QAction()
        # icon12 = QIcon()
        # icon12.addPixmap(QPixmap(":/icon/export.png"), QIcon.Normal, QIcon.Off)
        # self.ui._action_proj_export.setIcon(icon12)
        # self.ui._action_proj_export.setObjectName("_action_proj_export")
        # self.ui.menu_proj.insertAction(self.ui.action_proj_export, self.ui._action_proj_export)
        # self.ui._action_proj_export.setText("导出")

        # tab main
        self.ui.tab_main.removeTab(0)

        # creator
        _has = self.ui.tab_main_creator.layout() is not None
        if not _has:
            layout = QHBoxLayout()
            self.ui.tab_main_creator.setLayout(layout)
        else:
            layout = self.ui.tab_main_creator.layout()
        layout.setContentsMargins(4, 0, 0, 0)
        layout.setSpacing(0)
        self.core_widget__ipc_creator = QIpCoreCreator()
        layout.addWidget(self.core_widget__ipc_creator)

        # tables
        _has = self.ui.tab_main_tables.layout() is not None
        if not _has:
            layout = QHBoxLayout()
            self.ui.tab_main_tables.setLayout(layout)
        else:
            layout = self.ui.tab_main_tables.layout()
        layout.setContentsMargins(4, 0, 0, 0)
        layout.setSpacing(0)
        self.core_widget__tables = QExcelTableExportor()
        layout.addWidget(self.core_widget__tables)


    def _enable_ipcore_generate_update(self, *args):
        if not len(self.worker):
            self.worker.add(self._enter_update_vars)

    def _enter_update_vars(self, *args, default=False):
        while self._update_lock:
            time.sleep(0.1)
        self._update_lock = True

        # update cc ic
        try:
            if default:
                self.ipcore.build()
            else:
                self.ipcore.build(**self.params)
        except Exception as e:
            error = f"{e.__class__.__name__}:\n{str(e)}"
            self.ui.ptxt_cc.setText(error)
            self.ui.ptxt_ic.setText(error)
            self.ui.ptxt_mv.render_error(error)
            self._update_lock = False
            return
        # print("finish build")
        self.ui.ptxt_cc.setText(self.ipcore.built)
        self.ui.ptxt_ic.setText(self.ipcore.icode)
        try:
            self.ui.ptxt_mv.render_ipcore(self.ipcore)
        except Exception as e:
            self.ui.ptxt_mv.render_error(f"Render failed. Details:\n{e.__class__.__name__}:\n{str(e)}")
        # update inspector
        if self.var_widget.current is not None:
            try:
                self.var_widget.current.rebuildTrigger.emit(self.ipcore._mono)
            except Exception as e:
                self.ui.ptxt_mv.render_error(f"Rebuild failed. Details:\n{e.__class__.__name__}:\n{str(e)}")

            # self.var_widget.current.examine_rebuild(self.ipcore._mono)

        self._update_lock = False

    def load_current_size(self):
        f = files(os.getcwd(), '.prefer')
        size = f["window_size"]
        if size:
            self.resize(size)


    def _action_open_file(self):
        self._fn_open()

    def _action_reload_file(self):
        self._fn_open(auto=True)

    def _action_close_file(self):
        self._fn_close()

    def _action_save_current_size(self):
        f = files(os.getcwd(), '.prefer')
        f["window_size"] = self.size()

    def _action_export_proj(self, *, auto:bool=True):
        tab_main = self.ui.tab_main

        # index == 1:
        if tab_main.currentIndex() == 0:  # Ip Wizard
            self._fn_ip_export(auto=auto)
        elif tab_main.currentIndex() == 1:  # Ip Creator
            self._fn_compile_handler(auto=auto)
        elif tab_main.currentIndex() == 2:  # Table Export
            self._fn_tbl_export(auto=auto)

    def _action_export_proj_at(self):
        self._action_export_proj(auto=False)

    def _action_show_about(self):
        about_dialog = QAboutDialog(self)
        about_dialog.exec_()

    def _fn_open(self, path:str=None, auto:bool=False):
        # open a directory
        path = path or self.qst.getExistingDirectory(f"选择IP核:({IPC_SUFFIX})", auto=auto)
        if not path: return
        if not os.path.isdir(path):
            PopError("错误", "路径无效")
            return
        fdir, fnametype = os.path.split(path)
        fname = fnametype[:-len(IPC_SUFFIX)]
        f = files(fdir, IPC_SUFFIX)
        if not f.has(fname):
            PopError("错误", "IPC文件不存在或无法读取")
            return

        self.ipcore = IpCore(fdir, fname)
        self.ui.ptxt_rc.setText(self.ipcore.content)
        self.ui.ptxt_cc.setText("")
        self.ui.ptxt_ic.setText("")
        self.ui.tab_sc.setCurrentIndex(0)
        self._enter_update_vars(default=True)

        # model
        try:
            self.var_widget.current = self.ipcore.get_inspector(skip_update=True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e.__class__.__name__}:\n{str(e)}")
            return

        # active worker
        self.worker.dt = WORKER_ACTIVE_DELTA

        PopInfo("Info", "打开成功.")

    def _fn_close(self):
        self.ipcore = None
        self.ui.ptxt_rc.setText("")
        self.ui.ptxt_cc.setText("")
        self.ui.ptxt_ic.setText("")
        self.ui.ptxt_mv.clear()
        self.var_widget.current = None
        self.ui.tab_sc.setCurrentIndex(0)

        # deactive worker
        self.worker.dt = WORKER_DEACTIVE_DELTA


    def _fn_compile_handler(self,auto:bool=False):

        crt = self.core_widget__ipc_creator

        # 检查必填项name和fmain
        if not crt.info_collector.name:
            PopError("缺失:", "IP核名称不能为空")
            return
        if not crt.main_files_collector.fmain:
            PopError("缺失:", "主代码文件不能为空")
            return

        # 假设name不为空
        try:
            res = IpCore.Compile(
                crt.name, crt.author, crt.brand, crt.model, crt.board, crt.group,
                crt.fmain, crt.ficon, crt.freadme, crt.fmanual,
                crt.subpaths, crt.otherpaths
            )
        except IpCoreCompileError as e:
            QMessageBox.critical(self, "Error", str(e))
            return
        # 询问save路径
        f = files(type='.perfer')
        fdir = f['last_export_dir']
        fdir = os.path.abspath(fdir) if fdir and os.path.isdir(fdir) else os.getcwd()
        fdir = self.qst.getExistingDirectory("选择导出路径", fdir, auto=auto)
        if not fdir:
            return
        if not os.path.isdir(fdir):
            PopError("错误", f"路径无效: {fdir}")
            return
        if fdir.endswith(IPC_SUFFIX):
            fdir = os.path.dirname(fdir)

        # 保存
        f.last_export_dir = fdir
        groups = parse_group_path(crt.group)
        if groups:
            fdir = os.path.join(fdir, *groups)
            if not os.path.exists(fdir):
                os.makedirs(fdir)
        fipc = files(fdir, IPC_SUFFIX)
        for k, v in res.items():
            fipc[crt.name, k] = v
        PopInfo("Info", "编译导出成功.")
        try:
            set_ipcdir_icon(os.path.join(fdir, crt.name + IPC_SUFFIX))
        # except ThirdToolFolderIcoNotFound as e:
        #     PopWarn("工具未下载", str(e), 1.5)
        #     return
        # except FolderIcoPathContainSpace as e:
        #     PopWarn("路径包含空格", str(e))
        #     return
        except Exception as e:
            PopWarn("警告", f"设置图标失败: {e}\n*该功能不影响使用，但可能导致图标显示不正常.")
            return


    def _fn_ip_export(self, path:str=None, auto:bool=False):
        if self.ipcore is None:
            PopWarn("警告", "请先打开一个IP核文件.")
            return
        path = path or self.qst.getSaveFileName("选择导出的verilog文件", "", VERILOG_TYPE, filename=self.ipcore.name, auto=auto)
        if not path: return
        fname = os.path.basename(path)
        dirname = os.path.dirname(path)
        try:
            try:
                self.ipcore.export(dirname, spec_name=fname)
            except FileExistsError as e:
                if QMessageBox.question(self, "Warning", f"Do you want to overwrite it?\n\nexists: {e}",
                                        QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    self.ipcore.export(dirname, spec_name=fname, overwrite=True)
                else:
                    return
        except Exception as e:
            PopError(f"{e.__class__.__name__}:", str(e), 1.5)
            return
        PopInfo("Info", "导出成功.")

    def _fn_tbl_export(self, path:str=None, auto:bool=False):
        if self.core_widget__tables.excel is None:
            PopWarn("警告", "请先打开一个Excel文件.")
            return
        path = path or self.qst.getSaveFileName("选择导出的Top文件的位置(一并导出约束文件)", "", VERILOG_TYPE, filename="top")
        if not path: return
        try:
            try:
                self.core_widget__tables.export(path)
            except FileExistsError as e:
                if QMessageBox.question(self, "Warning", f"Do you want to overwrite it?\n\nexists: {e}",
                                        QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    self.core_widget__tables.export(path, overwrite=True)
                else:
                    return
        except Exception as e:
            PopError(f"{e.__class__.__name__}:", str(e), 1.5)
            return
        PopInfo("Info", "导出成功.")



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gui = GUI_Main()
    gui.show()
    sys.exit(app.exec_())
