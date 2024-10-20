from pyipcore.ui_utils import *
from PyQt5.QtGui import QIcon, QPixmap, QTransform
import time
def rotate_icon(icon, size, clockwise=True):
    if icon.isNull():
        return QIcon()
    # 获取图标的原始像素图
    original_pixmap = icon.pixmap(size, size)  # 使用图标的原始尺寸
    # 创建一个变换对象
    transform = QTransform()
    if clockwise:
        transform.rotate(90)  # 顺时针旋转
    else:
        transform.rotate(-90)  # 逆时针旋转
    # 应用变换到图标
    rotated_pixmap = original_pixmap.transformed(transform)
    # save
    # rotated_pixmap.save(f"rotated_pixmap_{int(time.time()*10000000)}.png")
    # 创建一个新的图标对象
    return QIcon(rotated_pixmap)

def rotate_tab_icons(tab_widget, size, clockwise=True):
    for i in range(tab_widget.count()):
        icon = tab_widget.tabIcon(i)
        if not icon.isNull():
            # 旋转图标
            new_icon = rotate_icon(icon, size, clockwise)
            # 设置新的图标到标签页
            tab_widget.setTabIcon(i, new_icon)
class UiTool_StyleAdjust:
    # Static class
    @classmethod
    def effect(cls, ui):
        """
        Adjust the style of the UI.
        """
        # 设置样式表
        ui.tab_main.setStyleSheet("""
            QTabBar::tab:selected {
                background-color: %s;
            }
        """ % LT_YELLOW.lighter(150).name(QColor.HexArgb))

        ui.tab_sc.setStyleSheet("""
            QTabBar::tab {
                color: %s;
                text-decoration: none;
            }
            QTabBar::tab:selected {
                color: %s;
                background-color: %s;
                text-decoration: none;
            }
        """ % (DODGERBLUE.darker(150).name(QColor.HexArgb),
               DODGERBLUE.darker(120).name(QColor.HexArgb),
               LT_YELLOW.name(QColor.HexArgb)
               ))

        rotate_tab_icons(ui.tab_main, 32, True)