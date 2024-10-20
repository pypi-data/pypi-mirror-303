from PyQt5.QtCore import Qt, QUrl, QPoint, QRectF, QLineF, QPointF, QObject, QPropertyAnimation, QSizeF, QMimeData, pyqtSignal
from PyQt5.QtCore import QThread, QTimer, QSettings
from PyQt5.QtPrintSupport import QPrinter, QPrintEngine
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel, QGridLayout, QPushButton, QSpacerItem, QSizePolicy, QApplication, QMessageBox
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsPathItem, QGraphicsDropShadowEffect, QGraphicsPixmapItem
from PyQt5.QtWidgets import QScrollArea, QGridLayout, QHBoxLayout, QFormLayout, QLineEdit, QFileDialog, QSpinBox, QCheckBox
from PyQt5.QtWidgets import QAction, QMainWindow
from PyQt5.Qsci import QsciScintilla, QsciLexerVerilog, QsciAPIs
from PyQt5.QtGui import QIcon, QPixmap, QImage, QDesktopServices, QFont, QColor, QPainter, QPen, QBrush, QPainterPath, QPolygonF, QFontMetrics, QDrag, QDragEnterEvent, QDragMoveEvent, QDragLeaveEvent, QDropEvent
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from pyipcore.ipc_utils import VERSION, GITEE_URL, APP_NAME
from rbpop import WinManager, RbpopInfo, RbpopWarn, RbpopError
from qwork.utils import QSetting
from threading import Thread
from pyipcore.utils import *
from qwork.qtclrs import *
import pyipcore.icon_rc
import subprocess
import winsound
import time
import math
import sys
import re
import os


ARIAL_FONT = QFont("Arial", 10, QFont.Normal)
LBL_FONT_MINI = QFont("Microsoft YaHei UI", 10, QFont.Normal)
LBL_FONT = QFont("Microsoft YaHei UI", 12, QFont.Normal)
LBL_FONT_B = QFont("Microsoft YaHei UI", 12, QFont.Bold)
BTN_FONT = QFont("Microsoft YaHei UI", 14, QFont.Normal)
BTN_FONT_B = QFont("Microsoft YaHei UI", 14, QFont.Bold)


SGGREEN = QColor(30, 124, 90, 175)
OLVORANGE = QColor(238, 121, 66, 175)

# raise ThirdToolFolderIcoNotFound("Please retry after install 'Teorex FolderIco' (url refer:https://www.folderico.com/download.html) and add it to path.")


def is_executable_in_path(executable_name):
    # 根据操作系统选择正确的命令
    if os.name == 'nt':  # Windows系统
        command = ['where', executable_name]
    else:  # Unix或类Unix系统
        command = ['which', executable_name]

    try:
        # 执行命令
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # 获取命令的输出
        output = result.stdout.strip()
        return bool(output)
    except subprocess.CalledProcessError:
    #     # 如果命令执行失败（例如，找不到文件），返回False
        return False

def export_icon_as_ico(rcpath:str, filename):
    pixmap = QPixmap(rcpath)
    # 保存为.ico文件
    pixmap.save(filename, 'ICO')


def get_qw_setting():
    return QSetting()

class ThirdToolFolderIcoNotFound(Exception): ...
class FolderIcoExecuteError(Exception): ...

class FolderIcoPathContainSpace(Exception): ...


def set_ipcdir_icon(fdir_path):
    if not os.path.exists(FP_ICON_IPCDIR):
        raise FileNotFoundError(f"Icon File not found: {FP_ICON_IPCDIR}")
    if not os.path.isdir(fdir_path):
        raise FileNotFoundError(f"Directory not found: {fdir_path}")

    # ['FolderIco', f'--folder {fdir_path}', f'--icon {FP_ICON_IPCDIR}']
    result = os.system(f'{TFI_PATH} --folder "{fdir_path}" --icon "{FP_ICON_IPCDIR}"')
    if result != 0:
        raise FolderIcoExecuteError("FolderIco execute error")

class QVerilogEdit(QsciScintilla):
    def __init__(self, parent=None, default_text=""):
        super().__init__(parent)

        # 创建 QScintilla 编辑器组件
        self.lexer = QsciLexerVerilog(parent)

        # 设置字体
        self.editor_font = QFont("Consolas", 14, QFont.Bold)
        self.editor_font.setFixedPitch(True)
        self.lexer.setFont(self.editor_font)
        self.setFont(self.editor_font)

        # 设置 lexer 为 Verilog
        self.setLexer(self.lexer)

        # 设置编辑器的大小和位置
        self.setGeometry(100, 100, 1400, 800)

        # 设置文本
        self.setText(default_text)

        # Set editor edit attributes
        self.set_editor_attributes()

        self._user_text_changed = None

    def set_editor_attributes(self):
        self.setUtf8(True)
        self.setMarginsFont(self.editor_font)
        self.setMarginWidth(0, len(str(len(self.text().split('\n')))) * 20)
        self.setMarginLineNumbers(0, True)

        self.setEdgeMode(QsciScintilla.EdgeLine)
        self.setEdgeColumn(100)
        self.setEdgeColor(QColor(0, 0, 0))

        self.setBraceMatching(QsciScintilla.StrictBraceMatch)

        self.setIndentationsUseTabs(True)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)

        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor('#FFFFCD'))

        self.setIndentationGuides(True)

        self.setFolding(QsciScintilla.PlainFoldStyle)
        self.setMarginWidth(2, 12)

        self.setMarkerForegroundColor(QColor("#272727"), QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionCaseSensitivity(True)
        self.setAutoCompletionReplaceWord(False)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)

        self.__api = QsciAPIs(self.lexer)
        auto_completions = ['module', 'endmodule', 'input', 'output', 'inout', 'wire', 'reg', 'assign',
                            'always', 'posedge', 'negedge', 'if', 'else', 'begin', 'end',
                            'case', 'endcase', 'default', 'for', 'while', 'repeat', 'forever',
                            'initial', 'function', 'endfunction', 'task', 'endtask', 'logic', 'integer',
                            'parameter', 'localparam', 'generate', 'endgenerate']
        for word in auto_completions:
            self.__api.add(word)
        self.__api.prepare()
        self.autoCompleteFromAll()

        self.textChanged.connect(self.changed)

    def changed(self):
        self.setMarginWidth(0, len(str(len(self.text().split('\n')))) * 20)
        if self._user_text_changed:
            self._user_text_changed()

    def setUserTextChanged(self, func):
        self._user_text_changed = func


class DraggableGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(DraggableGraphicsView, self).__init__(parent)
        self._raw_scene = QGraphicsScene()
        self.setScene(self._raw_scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.lastPos = QPoint()
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

    def wheelEvent(self, event):
        factor = 1.2
        if event.angleDelta().y() > 0:
            self.scale(factor, factor)
        else:
            self.scale(1 / factor, 1 / factor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = event.pos() - self.lastPos
            self.lastPos = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())

    def line(self, p0x, p0y, p1x, p1y, pcolor=Qt.black, width=1, *, dash=False):
        pen = QPen(QColor(pcolor), width)
        if dash:
            pen.setStyle(Qt.DashLine)
        line = QLineF(QPointF(p0x, p0y), QPointF(p1x, p1y))
        path = QPainterPath()
        path.moveTo(line.p1())
        path.lineTo(line.p2())
        item = QGraphicsPathItem(path)
        item.setPen(pen)
        self._raw_scene.addItem(item)
        return item

    def rectangle(self, p0x, p0y, w, h, bcolor=Qt.black, width=1, fcolor=None, *, dash=False):
        pen = QPen(QColor(bcolor), width)
        if dash:
            pen.setStyle(Qt.DashLine)
        brush = QBrush(QColor(fcolor)) if fcolor else QBrush()
        rect = QRectF(p0x, p0y, w, h)
        # self.scene().addRect(rect, pen, brush)
        # return rect
        path = QPainterPath()
        path.addRect(rect)
        item = QGraphicsPathItem(path)
        item.setPen(pen)
        item.setBrush(brush)
        self._raw_scene.addItem(item)
        return item

    def cycle(self, center_x, center_y, radius, pcolor=Qt.black, width=1, fcolor=None, *, dash=False):
        pen = QPen(QColor(pcolor), width)
        if dash:
            pen.setStyle(Qt.DashLine)
            pen.setDashPattern([5, 5])  # 设置虚线的样式，5个单位的线段后跟5个单位的空白
        brush = QBrush(QColor(fcolor)) if fcolor else QBrush()
        path = QPainterPath()
        path.addEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)
        item = QGraphicsPathItem(path)
        item.setPen(pen)
        item.setBrush(brush)
        self._raw_scene.addItem(item)
        return item

    def text(self, text, x, y, font=None, font_color=Qt.black, *, dash=False, rotate=0, use_r=False, use_b=False):
        text_item = QGraphicsTextItem(text)
        if font:
            text_item.setFont(font)
        else:
            # 如果没有提供字体，可以设置默认字体属性
            default_font = QFont()
            default_font.setPointSize(12)  # 默认字体大小
            text_item.setFont(default_font)
        text_item.setDefaultTextColor(QColor(font_color))

        # 计算文本的宽度和高度
        text_width = text_item.boundingRect().width()
        text_height = text_item.boundingRect().height()

        # 计算旋转角度（弧度）
        rotate = rotate % 360
        theta = math.radians(rotate)

        if rotate == 0 or rotate == 180:
            new_width = text_width
            new_height = text_height
        elif rotate == 90 or rotate == 270:
            new_width = text_height
            new_height = text_width
        else:
            new_width = text_width * math.cos(theta) + text_height * math.sin(theta)
            new_height = text_width * math.sin(theta) + text_height * math.cos(theta)

        # 如果 use_rp 为 True，则将坐标调整为右上角
        if use_r:
            x -= new_width
        if use_b:
            y -= new_height

        text_item.setPos(x, y)
        text_item.setRotation(rotate)
        self._raw_scene.addItem(text_item)
        return text_item

    @staticmethod
    def _find_points_on_line(k, b, x0, y0, length) -> tuple[QPointF, QPointF]:
        if k == float('inf'):
            return QPointF(x0, y0 - length), QPointF(x0, y0 + length)
        if k == 0:
            return QPointF(x0 - length, y0), QPointF(x0 + length, y0)
        y0 = k * x0 + b
        # 计算判别式
        discriminant = (length * length - (y0 - b) ** 2) / (1 + k ** 2)

        # 计算两个解
        x1 = (x0 + length * k - (y0 - b) * k) / (1 + k ** 2)
        x2 = (x0 - length * k - (y0 - b) * k) / (1 + k ** 2)

        # 计算对应的y值
        y1 = k * x1 + b
        y2 = k * x2 + b

        return QPointF(x1, y1), QPointF(x2, y2)

    @staticmethod
    def _calc_k_vertical(x0, y0, x1, y1) -> tuple[float, float]:
        if x1 - x0 == 0:
            return float('inf'), 0
        if y1 - y0 == 0:
            return 0, float('inf')
        k = (y1 - y0) / (x1 - x0)
        k_vertical = -1 / k
        return k, k_vertical

    def arrow(self, start_x, start_y, end_x, end_y, pen_color=Qt.black, pen_width=1, arrow_size=10, *, dash=False):
        # 创建线条的笔
        pen_line = QPen(QColor(pen_color), pen_width)
        if dash:
            pen_line.setStyle(Qt.DashLine)
            pen_line.setDashPattern([5, 5])  # 设置虚线的样式，5个单位的线段后跟5个单位的空白
        else:
            pen_line.setStyle(Qt.SolidLine)

        # ref
        length = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)
        line_length = length - arrow_size
        line_length = max(0, line_length)
        _ratio = line_length / length
        _ratio_1 = 1 / length
        line_end_x = start_x + (_ratio - _ratio_1) * (end_x - start_x)
        line_end_y = start_y + (_ratio - _ratio_1) * (end_y - start_y)
        tri_start_x = start_x + _ratio * (end_x - start_x)
        tri_start_y = start_y + _ratio * (end_y - start_y)
        k, k_vertical = self._calc_k_vertical(start_x, start_y, end_x, end_y)
        # 计算经过line_end的垂线的方程的b
        b = line_end_y - k_vertical * line_end_x

        # 创建路径
        path_line = QPainterPath()
        path_arrow = QPainterPath()
        path_line.moveTo(start_x, start_y)
        if line_length:
            path_line.lineTo(line_end_x, line_end_y)

        # 创建箭头的笔
        pen_arrow = QPen(QColor(pen_color), 1)
        pen_arrow.setStyle(Qt.SolidLine)  # 箭头通常为实线

        # 计算三角形箭头的三个点
        p0 = QPointF(end_x, end_y)
        p1, p2 = self._find_points_on_line(k_vertical, b, tri_start_x, tri_start_y, arrow_size / 2 + pen_width//8)

        # 添加箭头
        path_arrow.addPolygon(QPolygonF([p0, p1, p2, p0]))

        # 创建图形项目
        item = QGraphicsPathItem(path_line)
        item.setPen(pen_line)  # 使用线条的笔
        item.setBrush(QBrush(QColor(pen_color)))

        # 绘制箭头部分
        item_arrow = QGraphicsPathItem(path_arrow)
        item_arrow.setPen(pen_arrow)  # 使用箭头的笔
        item_arrow.setBrush(QBrush(QColor(pen_color)))

        # 合并箭头和线条
        self._raw_scene.addItem(item)
        self._raw_scene.addItem(item_arrow)

        return item, item_arrow



    def fill(self, rect, color=Qt.white):
        pen = QPen(Qt.NoPen)
        brush = QBrush(QColor(color))
        self._raw_scene.addRect(rect, brush=brush, pen=pen)


    def move_item_center(self, item, x, y):
        rect = item.boundingRect()
        item.setPos(x - rect.width() / 2, y - rect.height() / 2)

    def clear(self):
        self._raw_scene.deleteLater()  # TODO: QKill Timer 错误貌似是这句话导致的，不过不影响使用
        self._raw_scene = QGraphicsScene()
        self.setScene(self._raw_scene)

    def remove(self, item):
        self._raw_scene.removeItem(item)

    def effect_shallow(self, radius=25, offset_x=5, offset_y=5, color=Qt.darkGray):
        # 创建阴影效果对象
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(radius)  # 设置模糊半径
        shadow_effect.setOffset(offset_x, offset_y)
        shadow_effect.setColor(color)

        # 获取场景中的所有图形项
        items = self._raw_scene.items()

        # 为每个图形项应用阴影效果
        for item in items:
            item.setGraphicsEffect(shadow_effect)

    def pixelize(self):
        """
        将图像像素化
        先render，清空场景，再添加像素化图像

        """
        # 渲染场景
        pixmap = QPixmap(self.scene().sceneRect().size().toSize())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self._raw_scene.render(painter)
        painter.end()

        # 清空场景
        self.clear()

        # 添加像素化图像
        pixel_item = QGraphicsPixmapItem(pixmap)
        self._raw_scene.addItem(pixel_item)

        return pixel_item

    def image(self, filename, x, y, width, height):
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(width, height)
        item = QGraphicsPixmapItem(pixmap)
        item.setPos(x, y)
        self._raw_scene.addItem(item)
        return item

    def save(self, filename):
        """
        保存场景为图片
        :param filename: 保存的文件名
        """
        pixmap = QPixmap(self.scene().sceneRect().size().toSize())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self._raw_scene.render(painter)
        painter.end()
        pixmap.save(filename)

# class VerilogModuleView(QWidget):
#     ...


class BeepThread(Thread):
    def __init__(self):
        # 主程序退出后，子线程也退出
        super().__init__(daemon=True)
        self.tasks = []
        self.flag = True

    def Beep(self, freq, duration):
        self.tasks.append((freq, duration))

    def run(self):
        while self.flag:
            if not self.tasks:
                time.sleep(0.5)
                continue
            freq, duration = self.tasks.pop(0)
            winsound.Beep(freq, duration)

    def stop(self):
        self.flag = False


class BeepWinManager(WinManager):
    def __init__(self):
        super().__init__()
        self.beep = BeepThread()
        self.beep.start()

    def add(self, win, freq, duration):
        super().add(win)
        self.beep.Beep(freq, duration)


_GLOBAL_WM = [None]

QPOP_DEFAULT_SIZE = (360, 120)
def QPop(pop_win_inst, freq=400, duration=100):
    if _GLOBAL_WM[0] is None:
        _GLOBAL_WM[0] = BeepWinManager()

    _GLOBAL_WM[0].add(pop_win_inst, freq, duration)


def _pop_pre(title, msg, size=None):
    if size is None:
        size = QPOP_DEFAULT_SIZE
    cnt = int(30 * size[0] / QPOP_DEFAULT_SIZE[0])
    msg = re.sub(r'(.{' + str(cnt) + '})', r'\1\n', ' ' + msg)
    _len = len(msg)
    ct = 4000 + _len * 50
    return title, msg, ct


def PopInfo(title, msg, win_size:tuple|float|int=None):
    if isinstance(win_size, (float, int)):
        assert win_size > 0, "win_size must be a positive number"
        old_size = QPOP_DEFAULT_SIZE
        win_size = int(old_size[0] * win_size), int(old_size[1] * win_size)
    title, msg, ct = _pop_pre(title, msg, win_size)
    win = RbpopInfo(msg, title, ct=ct, title_style='color:rgb(105,109,105);font-size:20px;', msg_style='color:rgb(65,98,65);font-size:20px;', close=True, size=win_size)
    QPop(win, 400, 300)

def PopWarn(title, msg, win_size:tuple|float|int=None):
    if isinstance(win_size, (float, int)):
        assert win_size > 0, "win_size must be a positive number"
        old_size = QPOP_DEFAULT_SIZE
        win_size = int(old_size[0] * win_size), int(old_size[1] * win_size)
    title, msg, ct = _pop_pre(title, msg, win_size)
    win = RbpopWarn(msg, title, ct=ct, title_style='color:rgb(105,125,85);font-size:20px;', msg_style='color:rgb(85,105,75);font-size:20px;', close=True, size=win_size)
    QPop(win, 600, 300)

def PopError(title, msg, win_size:tuple|float|int=None):
    if isinstance(win_size, (float, int)):
        assert win_size > 0, "win_size must be a positive number"
        old_size = QPOP_DEFAULT_SIZE
        win_size = int(old_size[0] * win_size), int(old_size[1] * win_size)
    title, msg, ct = _pop_pre(title, msg, win_size)
    win = RbpopError(msg, title, ct=ct, title_style='color:rgb(225,50,50);font-size:20px;', msg_style='color:rgb(185,50,50);font-size:20px;', close=True, size=win_size)
    QPop(win, 800, 300)


class QAboutDialog(QDialog):
    def __init__(self, parent=None):
        super(QAboutDialog, self).__init__(parent)
        self.setWindowTitle(f"关于 {APP_NAME}")

        # 创建布局
        layout = QVBoxLayout()

        # 创建图标标签
        icon_label = QLabel(self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/verilog.png"), QIcon.Normal, QIcon.Off)
        icon_label.setPixmap(icon.pixmap(128, 128))  # 设置图标大小

        # 创建文本标签
        self.text_label = QLabel(self)
        self.url_label = QLabel(self)
        self.set_text()  # 设置文本内容和链接
        self.text_label.setWordWrap(True)  # 开启文本换行
        self.url_label.setTextInteractionFlags(Qt.TextBrowserInteraction)  # 允许文本交互
        font = QApplication.font("SIMHEI")
        font.setPointSize(11)  # 例如，设置字号为12，您可以根据需要调整这个值
        self.text_label.setFont(font)
        self.url_label.setFont(font)

        # 创建按钮
        button = QPushButton("确定", self)
        button.setDefault(True)  # 设置为默认按钮

        # 创建网格布局并添加组件
        grid_layout = QGridLayout()
        grid_layout.addWidget(icon_label, 0, 0, 3, 1)  # 图标跨越3行
        grid_layout.addWidget(self.text_label, 0, 1, 1, 1)  # 文本标签在第一行，第二列
        grid_layout.addWidget(self.url_label, 1, 1, 1, 1)  # URL标签在第二行，第二列
        grid_layout.addWidget(button, 2, 1, 1, 1)  # 按钮在第三行，第二列

        # 添加水平间隔
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        grid_layout.addItem(spacer_item, 1, 0)

        # 将网格布局添加到垂直布局
        layout.addLayout(grid_layout)

        # 设置对话框的布局
        self.setLayout(layout)

        # 连接按钮的点击事件
        button.clicked.connect(self.close)

        # 连接文本标签的链接激活事件
        self.url_label.linkActivated.connect(self.open_url)

    def set_text(self):
        self.text_label.setText(f"Version: {VERSION}\n"
                                "Author: Eagle'sBaby，EAShine\n"
                                "Bilibili: 我阅读理解一直可以的\n"
                                "Bilibili UID: 129249826")
        # f"Gitee URL: <a href='{GITEE_URL}'>{GITEE_URL}</a>")
        self.url_label.setText(f"Gitee URL: <a href='{GITEE_URL}'>{GITEE_URL}</a>")
        self.url_label.setOpenExternalLinks(True)  # 允许打开外部链接

    def open_url(self, url):
        print(url)
        QDesktopServices.openUrl(QUrl(url))
