
from pyipcore.ui_main import GUI_Main, QApplication, QMessageBox, QMainWindow
from pyipcore.ui_utils import DraggableGraphicsView, QGraphicsScene, QPixmap, QRectF, Qt, QPainter, QFont
from pyipcore.splash import show_first_splash
from pyipcore.utils import create_prepare
import sys


def pyipc():
    """
    Run the GUI application.
    CMD主函数入口
    """
    app = QApplication(sys.argv)
    gui = GUI_Main()

    # create environment
    nfas = create_prepare()
    if nfas:
        splash = show_first_splash(*nfas)
        splash.successFinished.connect(gui.show)
    else:
        gui.show()

    try:
        sys.exit(app.exec_())
    except Exception as err:
        QMessageBox.warning(gui, "Error:", str(err))

if __name__ == '__main__':
    pyipc()
