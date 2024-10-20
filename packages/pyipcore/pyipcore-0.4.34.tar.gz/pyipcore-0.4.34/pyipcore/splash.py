import sys
import time

from PyQt5.QtWidgets import QSplashScreen, QProgressBar
import pyipcore.icon_rc
from pyipcore.ui_utils import *

class QTask(QThread):
    progressChanged = pyqtSignal(int)
    currentChanged = pyqtSignal(str)
    errorOccurred = pyqtSignal(str)
    successFinished = pyqtSignal()
    def __init__(self, parent=None, *, perdelay:int=1):
        super(QTask, self).__init__(parent)
        self._current_value = 0
        self._current_task = ""
        self._perdelay = perdelay
        self._tasks:list[tuple[str, callable, tuple]] = []

    def add(self, task_name:str, task:callable, args:tuple=()):
        self._tasks.append((task_name, task, args))

    def run(self):
        # 这里模拟一个任务
        for i in range(self.total):
            self._current_value = i
            self._current_task = self._tasks[i][0]
            self.progressChanged.emit(self._current_value)
            self.currentChanged.emit(self._current_task)
            # self.sleep(1)  # 模拟耗时操作
            task, args = self._tasks[i][1:]
            try:
                task(*args)
                time.sleep(self._perdelay)
            except Exception as e:
                self.errorOccurred.emit(str(e))
                return
        self.successFinished.emit()

    @property
    def current(self) -> tuple[int, str]:
        return self._current_value, self._current_task

    @property
    def total(self):
        return len(self._tasks)


# 你的SplashTask类
class SplashTask(QWidget):
    successFinished = pyqtSignal()
    def __init__(self, task, logo, parent=None):
        super(SplashTask, self).__init__(parent)
        self.task:QTask = task
        self.logo:QIcon = logo
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Splash Screen")
        self.setWindowFlag(Qt.FramelessWindowHint)  # hide the header
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # always on top
        self.setAttribute(Qt.WA_TranslucentBackground)  # transparent background
        self.setWindowOpacity(0.9)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setPixmap(self.toTransparentPixmap(self.logo.pixmap(256, 256), 0.9))
        # self.logo_label.setPixmap(self.logo.pixmap(256, 256))
        layout.addWidget(self.logo_label)

        h0 = QHBoxLayout()
        h0.setContentsMargins(0, 0, 0, 0)
        h0.setSpacing(0)
        h0.addStretch(1)
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setFormat("")
        self.progress_bar.setMaximum(0)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedWidth(240)
        h0.addWidget(self.progress_bar)
        h0.addStretch(1)
        layout.addLayout(h0)

        self.task_label = QLabel("Initializing...")
        self.task_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.task_label.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.task_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.task_label)

        self.setLayout(layout)

        self.show()
        self.move_to_screen_center()
        self.task.start()

        # self.task.progressChanged.connect(self.update_progress)
        self.task.currentChanged.connect(self.update_task)
        self.task.errorOccurred.connect(self.on_task_error)
        self.task.successFinished.connect(self.on_task_finished)

    @staticmethod
    def toTransparentPixmap(raw: QPixmap, percent:float) -> QPixmap:
        # 创建一个新的QPixmap对象，具有与原始相同的尺寸
        transparent_pixmap = QPixmap(raw.size())
        transparent_pixmap.fill(QColor(0, 0, 0, 0))  # 填充透明背景

        # 创建QPainter对象
        painter = QPainter(transparent_pixmap)
        painter.setOpacity(percent)  # 设置透明度为percent
        painter.drawPixmap(0, 0, raw)  # 绘制原始图标
        painter.end()  # 结束绘制

        return transparent_pixmap

    def move_to_screen_center(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        self.move((screen_rect.width() - self.width()) // 2, (screen_rect.height() - self.height()) // 2)

    def update_task(self, task_name):
        self.task_label.setText(task_name)

    def on_task_finished(self):
        self.successFinished.emit()
        self.close()

    def on_task_error(self, error):
        self.task_label.setText(f"Error Occurred!")
        self.task_label.setStyleSheet("color: rgba(255, 0, 0, 180); font-weight: bold;")
        self.progress_bar.setMaximum(1)
        # winpos = self.pos()
        # self.move(winpos.x(), winpos.y() - 200)

        # 显示错误消息框()
        QMessageBox.critical(self, "Error", error)

        self.close()

    def paintEvent(self, a0):
        # 绘制圆角矩形
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(LT_DODGERBLUE.darker(), 5, Qt.SolidLine))
        painter.setBrush(LT_YELLOW.lighter().lighter())

        rect = QRectF(0, 0, self.width(), self.height())
        painter.drawRoundedRect(rect, 10, 10)

        super(SplashTask, self).paintEvent(a0)




def show_first_splash(*name_func_args:tuple[str, callable, tuple], wait:int=4) -> QWidget:
    length = len(name_func_args)
    piece = min(wait / length, 1)
    def _inner():
        time.sleep(1 + piece)
    assert isinstance(name_func_args, tuple), "name_func_args must be a tuple."
    task = QTask(perdelay=piece)
    task.add("First Loading...", _inner)
    for name, func, args in name_func_args:
        task.add(name, func, args)
    task.add("Success Done.", _inner)

    logo = QIcon()  # 替换为你的图标路径
    logo.addPixmap(QPixmap(":/icon/verilog.png"), QIcon.Normal, QIcon.Off)
    splash = SplashTask(task, logo)
    return splash
