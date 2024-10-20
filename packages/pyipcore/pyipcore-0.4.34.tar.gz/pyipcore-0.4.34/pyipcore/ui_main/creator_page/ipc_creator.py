from PyQt5.QtWebEngineWidgets import QWebEngineView
from pyipcore.ui_utils import *
from qwork.fileitem import *
import markdown



class QMdView(QWidget):
    def __init__(self, parent=None):
        super(QMdView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 设置布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 创建QWebEngineView对象
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)


    def load_md_file(self, filepath):
        # 将Markdown文件转换为HTML
        markdown_html = self.convert_md_to_html(filepath)

        # 使用QWebEngineView显示HTML内容
        self.web_view.setHtml(markdown_html)

    def setMdText(self, text):
        self.web_view.setHtml(markdown.markdown(text))

    @staticmethod
    def convert_md_to_html(filepath):
        # 读取Markdown文件内容
        with open(filepath, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # 使用markdown库将Markdown转换为HTML
        html_content = markdown.markdown(markdown_content)

        return html_content


class QIpcPreviewExporter(QWidget):
    clearPushed = pyqtSignal()  # 清空内容
    updatePushed = pyqtSignal()  # 更新预览
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(1)

        label = QLabel("概述文件预览:")
        label.setFont(LBL_FONT)
        label.setFixedHeight(QFixWidthLabel.GetHeight(1))
        self.md_view = QMdView()
        self.md_view.setMinimumHeight(300)
        self.md_view.setMinimumWidth(200)
        layout.addWidget(label)
        layout.addWidget(self.md_view)

        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(1, 1, 1, 1)
        bottom_layout.setSpacing(4)
        layout.addLayout(bottom_layout)

        self.clear_btn = QPushButton("清空内容")
        self.clear_btn.setFont(BTN_FONT)
        self.clear_btn.clicked.connect(self.clearPushed)
        bottom_layout.addWidget(self.clear_btn)
        self.update_btn = QPushButton("更新预览")
        self.update_btn.setFont(BTN_FONT)
        self.update_btn.clicked.connect(self.updatePushed)
        bottom_layout.addWidget(self.update_btn)


class QIconLabel(QWidget):
    def __init__(self, icon:QIcon|QPixmap, text:str, direct="left", parent=None):
        super().__init__(parent)
        if isinstance(icon, QPixmap):
            _ = QIcon()
            _.addPixmap(icon, QIcon.Normal, QIcon.Off)
            icon = _
        self.icon = icon
        self.text = text
        assert direct in ["left", "right"], f"direct must be 'left' or 'right', but got {direct}"
        self.direct = direct    # left or right only
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        self.setLayout(layout)
        self.label = QLabel(self.text)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon.pixmap(32, 32))
        if self.direct == "left":
            layout.addWidget(self.icon_label)
            layout.addWidget(self.label)
        else:
            layout.addWidget(self.label)
            layout.addWidget(self.icon_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)



class QIpcInfoCollector(QWidget):
    """
    name: str  # IP核别名
    author: str  # IP核作者
    brand: str  # FPGA芯片品牌
    model: str  # FPGA芯片型号
    board: str  # IP核所适用开发板
    group: str  # IP核所属组别
    都不是必须的，可以为空，默认None
    """

    def __init__(self):
        super().__init__()
        self.initUI()

        # 设置默认值
        username = os.environ.get("USERNAME")
        self.author = username

    def initUI(self):
        layout = QGridLayout(self)
        self.setLayout(layout)
        self.name_edit = QLineEdit()  # border 1px solid LT_RED
        self.name_edit.setFont(LBL_FONT)
        self.name_edit.setStyleSheet(f"border: 2px solid rgba({LT_RED.red()}, {LT_RED.green()}, {LT_RED.blue()}, {LT_RED.alphaF()});")
        self.author_edit = QLineEdit()
        self.brand_edit = QLineEdit()
        self.model_edit = QLineEdit()
        self.board_edit = QLineEdit()
        self.group_edit = QLineEdit()

        # Add icons to each label
        self.name_lbl = QIconLabel(QPixmap(":/icon/rename.png"), " *IP核名称 ", direct="left")
        self.author_lbl = QIconLabel(QPixmap(":/icon/user.png"), "  IP核作者 ", direct="left")
        self.brand_lbl = QIconLabel(QPixmap(":/icon/brand.png"), " FPGA芯片品牌 ", direct="left")
        self.model_lbl = QIconLabel(QPixmap(":/icon/model.png"), " FPGA芯片型号 ", direct="left")
        self.board_lbl = QIconLabel(QPixmap(":/icon/board.png"), " IP核适用开发板 ", direct="left")
        self.group_lbl = QIconLabel(QPixmap(":/icon/group.png"), " IP核所属组别 ", direct="left")
        self.name_lbl.setFont(LBL_FONT)
        self.author_lbl.setFont(LBL_FONT)
        self.brand_lbl.setFont(LBL_FONT)
        self.model_lbl.setFont(LBL_FONT)
        self.board_lbl.setFont(LBL_FONT)
        self.group_lbl.setFont(LBL_FONT)

        layout.addWidget(self.name_lbl, 1, 0)
        layout.addWidget(self.name_edit, 1, 1)
        layout.addWidget(self.author_lbl, 2, 0)
        layout.addWidget(self.author_edit, 2, 1)
        layout.addWidget(self.brand_lbl, 3, 0)
        layout.addWidget(self.brand_edit, 3, 1)
        layout.addWidget(self.model_lbl, 4, 0)
        layout.addWidget(self.model_edit, 4, 1)
        layout.addWidget(self.board_lbl, 5, 0)
        layout.addWidget(self.board_edit, 5, 1)
        layout.addWidget(self.group_lbl, 6, 0)
        layout.addWidget(self.group_edit, 6, 1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)



    @property
    def name(self):
        return self.name_edit.text()

    @name.setter
    def name(self, name):
        self.name_edit.setText(name)

    @property
    def author(self):
        return self.author_edit.text()

    @author.setter
    def author(self, author):
        self.author_edit.setText(author)

    @property
    def brand(self):
        return self.brand_edit.text()

    @brand.setter
    def brand(self, brand):
        self.brand_edit.setText(brand)

    @property
    def model(self):
        return self.model_edit.text()

    @model.setter
    def model(self, model):
        self.model_edit.setText(model)

    @property
    def board(self):
        return self.board_edit.text()

    @board.setter
    def board(self, board):
        self.board_edit.setText(board)

    @property
    def group(self):
        return self.group_edit.text()

    @group.setter
    def group(self, group):
        self.group_edit.setText(group)



class QIpcMainFilesCollector(QWidget):
    """
    2x4网格布局。内部为4个(QFileSlot上 + QLabel下)组合，用于收集IP核的主要文件。
        QFileSlot(self, parent=None, *, size=64, dragcut=True, formats:list=None)对象
        @property path r|w
        @property formats r|w

    *"主代码文件.v": 只支持.v文件  # ['v']
    "图标文件":  支持多种格式  # ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'svg']
    "自述文件.md": 只支持.md文件  # ['md']
    "使用手册.pdf": 只支持.pdf文件  # ['pdf']

    *使用红色边框修饰必要文件
    """
    vfileChanged = pyqtSignal(str)
    iconChanged = pyqtSignal(str)
    readmeChanged = pyqtSignal(str)
    def __init__(self, parent=None, *, size=64):
        super().__init__(parent)

        # 创建网格布局
        self.grid_layout = QGridLayout(self)

        # 文件槽和标签的列表
        self.file_slots = []
        self.labels = []
        self._size = size
        self._id = 0

        self.initUI()

    @property
    def fmain(self) -> str:
        return self.file_slots[0].path

    @fmain.setter
    def fmain(self, path):
        self.file_slots[0].path = path

    @property
    def ficon(self) -> str:
        return self.file_slots[1].path

    @ficon.setter
    def ficon(self, path):
        self.file_slots[1].path = path

    @property
    def freadme(self) -> str:
        return self.file_slots[2].path

    @freadme.setter
    def freadme(self, path):
        self.file_slots[2].path = path

    @property
    def fmanual(self) -> str:
        return self.file_slots[3].path

    @fmanual.setter
    def fmanual(self, path):
        self.file_slots[3].path = path

    def initUI(self):
        # 主代码文件.v
        self.add_file_slot("代码文件\n*.v", ['v'], required=True)
        self.file_slots[0].fileChanged.connect(self.vfileChanged)

        # 图标文件
        self.add_file_slot("图标文件\n ", ['png', 'jpg', 'jpeg', 'bmp', 'svg'])
        self.file_slots[1].fileChanged.connect(self.iconChanged)

        # 自述文件.md
        self.add_file_slot("自述文件\n*.md|txt", ['md', 'txt'])
        self.file_slots[2].fileChanged.connect(self.readmeChanged)

        # 使用手册.pdf
        self.add_file_slot("使用手册\n*.pdf", ['pdf'])

        # 设置布局
        self.setLayout(self.grid_layout)

    def add_file_slot(self, label_text, formats, required=False):
        """
        添加文件槽和标签到布局
        """
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(QFixWidthLabel.GetHeight(2) + 2)
        label.setFont(LBL_FONT_MINI)
        file_slot = QFileSlot(self, formats=formats, size=self._size)

        if required:
            file_slot.setBorder(2, LT_RED)
        else:
            file_slot.setBorder(2, LT_GREY)

        base_row, base_col = self._get_next_valid()
        self.grid_layout.addWidget(file_slot, base_row, base_col)
        self.grid_layout.addWidget(label, base_row + 1, base_col)

        self.file_slots.append(file_slot)
        self.labels.append(label)

    def _get_next_valid(self):
        """
        获取下一个可用的起始位置
        """
        idx = self._id
        self._id += 1

        # 计算行列
        row = idx // 2
        col = idx % 2

        return row * 2, col


class QIpcSubFilesCollector(QWidget):
    """
    用于收集'从属文件'和'其他文件'的文件槽
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建垂直布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(1)


        # 创建从属文件槽
        self.lbl0 = QLabel("从属文件:")
        self.lbl0.setToolTip("使用主文件处理得到的环境处理这些文件。可以使用EVAL替换语法和分支控制语法。")
        self.lbl0.setFixedHeight(QFixWidthLabel.GetHeight(1))
        self.lbl0.setFont(LBL_FONT)
        self.sub_files = QFilesView()
        self.sub_files.setFixedHeight(120)
        self.layout.addWidget(self.lbl0)
        self.layout.addWidget(self.sub_files)

        # 创建其他文件槽
        self.lbl1 = QLabel("其他文件:")
        self.lbl1.setToolTip("其他文件不会被处理，但会被打包到IP核中。")
        self.lbl1.setFixedHeight(QFixWidthLabel.GetHeight(1))
        self.lbl1.setFont(LBL_FONT)
        self.other_files = QFilesView()
        self.other_files.setMinimumHeight(256)
        self.layout.addWidget(self.lbl1)
        self.layout.addWidget(self.other_files)

    @property
    def subpaths(self):
        return self.sub_files.paths

    @property
    def otherpaths(self):
        return self.other_files.paths


class QIpCoreCreator(QWidget):
    """
    组合QIpcInfoCollector, QIpcMainFilesCollector, QIpcSubFilesCollector(占据1x2大小), QIpcPreviewExport(占据右侧2x1大小)
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QGridLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(1)
        self.setLayout(layout)

        # 创建QIpcInfoCollector对象
        self.info_collector = QIpcInfoCollector()
        self.info_collector.setFixedWidth(400)
        layout.addWidget(self.info_collector, 0, 0)

        # 创建QIpcMainFilesCollector对象
        self.main_files_collector = QIpcMainFilesCollector(size=80)
        self.main_files_collector.setFixedWidth(180)
        self.main_files_collector.vfileChanged.connect(self.auto_fill_name)
        layout.addWidget(self.main_files_collector, 0, 1)

        # 创建QIpcSubFilesCollector对象
        self.sub_files_collector = QIpcSubFilesCollector()
        layout.addWidget(self.sub_files_collector, 1, 0, 1, 2)

        # 创建QIpcPreviewExporter对象
        self.preview_exporter = QIpcPreviewExporter()
        layout.addWidget(self.preview_exporter, 0, 2, 2, 1)
        self.preview_exporter.clearPushed.connect(self.clear)
        self.preview_exporter.updatePushed.connect(self.update)

    def auto_fill_name(self, v_path):
        """
        从.v文件路径自动填充IP核名称
        """
        if not v_path:
            return
        name = os.path.basename(v_path)
        name = name.split('.')[0]
        self.info_collector.name = name

    def clear(self):
        self.info_collector.name = ""
        self.info_collector.author = ""
        self.info_collector.brand = ""
        self.info_collector.model = ""
        self.info_collector.board = ""
        self.info_collector.group = ""

        self.main_files_collector.fmain = ""
        self.main_files_collector.ficon = ""
        self.main_files_collector.freadme = ""
        self.main_files_collector.fmanual = ""

        self.sub_files_collector.sub_files.clear()
        self.sub_files_collector.other_files.clear()

    def update(self):
        if self.main_files_collector.freadme:
            self.preview_exporter.md_view.load_md_file(self.main_files_collector.freadme)
        else:
            self.preview_exporter.md_view.setMdText("")

    @property
    def name(self):
        return self.info_collector.name

    @name.setter
    def name(self, name):
        self.info_collector.name = name

    @property
    def author(self):
        return self.info_collector.author

    @author.setter
    def author(self, author):
        self.info_collector.author = author

    @property
    def brand(self):
        return self.info_collector.brand

    @brand.setter
    def brand(self, brand):
        self.info_collector.brand = brand

    @property
    def model(self):
        return self.info_collector.model

    @model.setter
    def model(self, model):
        self.info_collector.model = model

    @property
    def board(self):
        return self.info_collector.board

    @board.setter
    def board(self, board):
        self.info_collector.board = board

    @property
    def group(self):
        return self.info_collector.group

    @group.setter
    def group(self, group):
        self.info_collector.group = group

    @property
    def fmain(self):
        return self.main_files_collector.fmain

    @fmain.setter
    def fmain(self, path):
        self.main_files_collector.fmain = path

    @property
    def ficon(self):
        return self.main_files_collector.ficon

    @ficon.setter
    def ficon(self, path):
        self.main_files_collector.ficon = path

    @property
    def freadme(self):
        return self.main_files_collector.freadme

    @freadme.setter
    def freadme(self, path):
        self.main_files_collector.freadme = path

    @property
    def fmanual(self):
        return self.main_files_collector.fmanual

    @fmanual.setter
    def fmanual(self, path):
        self.main_files_collector.fmanual = path

    @property
    def subpaths(self):
        return self.sub_files_collector.subpaths

    @property
    def otherpaths(self):
        return self.sub_files_collector.otherpaths

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QIpCoreCreator()

    w.show()
    sys.exit(app.exec_())