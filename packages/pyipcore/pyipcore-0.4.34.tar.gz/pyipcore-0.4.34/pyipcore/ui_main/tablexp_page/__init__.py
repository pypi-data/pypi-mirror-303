import os.path
from qwork.fileitem import *
from pyipcore.ui_utils import *
from pyipcore.ui_main.tablexp_page._tools import *



class QExcelExampleShower(QWidget):
    def __init__(self, parent=None, width:int=4):
        super(QExcelExampleShower, self).__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setMinimumWidth(250)
        self.setMinimumHeight(300)
        self._font = LBL_FONT_MINI
        self.bias:tuple[int, int] = (0, 0)
        self.target:tuple[int, int] = (1, 1)
        self.delta:tuple[int, int] = (0, 0)

        self._pen_biasx = QPen(DODGERBLUE, width, Qt.SolidLine)
        self._pen_biasy = QPen(OLVORANGE, width, Qt.SolidLine)
        self._pen_targetx = QPen(MEDIUMPURPLE, width, Qt.SolidLine)
        self._pen_targety = QPen(SGGREEN, width, Qt.SolidLine)
        self._pen_deltax = QPen(DARKGOLDENROD, width, Qt.DashDotLine)
        self._pen_deltay = QPen(DARKSLATEGRAY, width, Qt.DashDotLine)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        pen0 = QPen(LT_BLACK, 1, Qt.SolidLine)
        pen1 = QPen(Qt.darkGray, 1, Qt.SolidLine)
        painter.setPen(pen0)
        painter.setBrush(QBrush(LT_YELLOW))

        _width, _height = self.width(), self.height()

        painter.drawRect(0, 0, _width, _height)

        # # top left
        dx = _width // 5
        dy = _height // 6
        painter.setPen(self._pen_biasx)
        painter.drawLine(0, dy, dx, dy)
        painter.setPen(self._pen_biasy)
        painter.drawLine(dx, 0, dx, dy)

        painter.setPen(self._pen_targetx)
        painter.drawLine(dx, dy, dx * 3, dy)
        painter.drawLine(dx * 4, dy, dx * 5 + 5, dy)
        painter.drawLine(dx, dy * 4, dx * 3, dy * 4)
        painter.drawLine(dx, dy * 5, dx * 3, dy * 5)
        painter.drawLine(dx * 4, dy * 4, dx * 5 + 5, dy * 4)
        painter.drawLine(dx * 4, dy * 5, dx * 5 + 5, dy * 5)
        painter.setPen(self._pen_targety)
        painter.drawLine(dx, dy, dx, dy * 4)
        painter.drawLine(dx * 3, dy, dx * 3, dy * 4)
        painter.drawLine(dx * 4, dy * 5, dx * 4, dy * 6 + 6)
        painter.drawLine(dx * 3, dy * 5, dx * 3, dy * 6 + 6)
        painter.drawLine(dx, dy * 5, dx, dy * 6 + 6)
        painter.drawLine(dx * 4, dy, dx * 4, dy * 4)

        painter.setPen(self._pen_deltax)
        painter.drawLine(dx * 3, int(dy * 2.5), dx * 4, int(dy * 2.5))
        painter.setPen(self._pen_deltay)
        painter.drawLine(int(dx * 2), dy * 4, int(dx * 2), dy * 5)
        #
        # # top 'A' left '1'
        painter.setPen(pen1)
        painter.setFont(LBL_FONT_B)
        txt = f'{self.get_excel_alpha(self.bias[0])}{self.bias[1] + 1}'  # 左上角坐标，绘制在dx + 2 dy + 2
        rectf = QRectF(dx + 4, dy + 2, dx - 8, dy - 4)
        painter.drawText(rectf, Qt.AlignLeft | Qt.AlignTop, txt)
        txt = f'{self.get_excel_alpha(self.bias[0] + self.target[0] - 1)}{self.bias[1] + self.target[1]}'  # 右下角坐标，绘制在dx * 3 + 2 dy * 4 + 2
        rectf = QRectF(dx * 2 + 4, dy * 3 + 2, dx - 8, dy - 4)
        painter.drawText(rectf, Qt.AlignRight | Qt.AlignBottom, txt)

    @classmethod
    def get_excel_alpha(cls, offset: int) -> str:
        """
        Convert an integer offset to an Excel column letter.

        0 -> A
        1 -> B
        26 -> AA
        ...

        :param offset: The integer offset to convert.
        :return: The corresponding Excel column letter.
        """
        if offset < 26:
            # If the offset is less than 26, return the corresponding letter.
            return chr(ord('A') + offset)
        else:
            # If the offset is 26 or more, calculate the next letter in the sequence.
            return cls.get_excel_alpha((offset - 1) // 26) + \
                chr(ord('A') + (offset - 1) % 26)


class QCheckedContainer(QWidget):
    def __init__(self, parent=None):
        super(QCheckedContainer, self).__init__(parent)

class QCheckedListWidget(QWidget):
    def __init__(self, parent=None):
        super(QCheckedListWidget, self).__init__(parent)
        self.sheets = []    # 存储名称
        self._checks = []   # 存储复选框
        self._widgets = []
        self.initUI()
        self.setStyleSheet('background-color: white;' f'border: 1px solid rgba({LT_BLACK.red()}, {LT_BLACK.green()}, {LT_BLACK.blue()}, {LT_BLACK.alpha()});')

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.container = QCheckedContainer()
        self.list_layout = QVBoxLayout(self.container)
        self.list_layout.addStretch(1)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(2)
        self._area = QScrollArea()
        self._area.setWidget(self.container)
        self._area.setWidgetResizable(True)
        self._area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.layout.addWidget(self._area)
        # self.layout.addStretch(1)

        self.setMinimumHeight(300)
        self.setMinimumWidth(200)

    def clear(self):
        for widget in self._widgets:
            widget.deleteLater()
        self._area.takeWidget()
        self.container.deleteLater()
        self.container = QCheckedContainer()
        self.list_layout = QVBoxLayout(self.container)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(2)
        self.list_layout.addStretch(1)
        self._area.setWidget(self.container)

        self._widgets.clear()
        self.sheets.clear()
        self._checks.clear()

    def addItem(self, name, checked=False):
        layout = QHBoxLayout()
        lbl = QLabel(name)
        check = QCheckBox()
        check.setChecked(checked)
        layout.addWidget(check)
        layout.addWidget(lbl)
        layout.addStretch(1)
        lbl.setFont(LBL_FONT_MINI)
        lbl.setStyleSheet("border: 0px;")
        check.setStyleSheet("border: 0px;")
        self._checks.append(check)
        self.sheets.append(name)
        self._widgets.append(lbl)
        self._widgets.append(check)
        self.list_layout.insertLayout(len(self._checks) - 1, layout)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.setPen(QPen(LT_BLACK, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))

        painter.drawRect(0, 0, self.width(), self.height())

        super().paintEvent(a0)

    @property
    def selects(self) -> list[bool]:
        return [c.isChecked() for c in self._checks]


class QSheetsListWidget(QCheckedListWidget):
    onCheckedChanged = pyqtSignal(int, int)
    def __init__(self, excel_path=None, parent=None):
        super(QSheetsListWidget, self).__init__(parent)
        self._excel_path = excel_path
        if excel_path: self._load_sheets()

    def _load_sheets(self):
        xls = pd.ExcelFile(self._excel_path)
        for sheet in xls.sheet_names:
            self.addItem(sheet, checked=True)

    @property
    def path(self):
        return self._excel_path

    @path.setter
    def path(self, path):
        self._excel_path = path
        self.clear()
        if os.path.exists(path):
            self._load_sheets()

    def addItem(self, name, checked=False):
        super().addItem(name, checked)
        self._checks[-1].stateChanged.connect(lambda state: self._on_check_changed(len(self._checks) - 1, state))

    def _on_check_changed(self, idx, state):
        self.onCheckedChanged.emit(idx, state)



class QExcelFileHeaderCollector(QWidget):
    onExcelChanged = pyqtSignal(str)
    onCstChanged = pyqtSignal(str)
    onSelectedSheetsChanged = pyqtSignal(list)
    def __init__(self, parent=None):
        super(QExcelFileHeaderCollector, self).__init__(parent)
        self._sv = get_qw_setting()
        if self._sv.has('last_excel_offsets'):
            _bias, _target, _delta = self._sv['last_excel_offsets']
            self.initUI(_bias, _target, _delta)
        else:
            self.initUI()
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))
        self._on_value_changed()

    def initUI(self, bias:tuple[int, int]=(0, 1), target:tuple[int, int]=(6, 30), delta:tuple[int, int]=(0, 2)):
        self.setMinimumHeight(750)
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(1, 1, 1, 1)
        self._layout.setSpacing(8)
        self.setLayout(self._layout)
        h0, h1, h2 = QHBoxLayout(), QHBoxLayout(), QHBoxLayout()
        v0 = QVBoxLayout()
        self.setFont(LBL_FONT_MINI)
        self._excelslot = QFileSlot(formats=['xlsx'], size=100)
        self._excelslot.setBorder(2, LT_RED)
        self._excelslot.fileChanged.connect(self._on_excel_changed)
        self._excelslot.setFont(ARIAL_FONT)
        self._cstslot = QFileSlot(size=100)
        self._cstslot.setBorder(2, LT_RED)
        self._cstslot.fileChanged.connect(self._on_cst_changed)
        self._cstslot.setFont(ARIAL_FONT)
        h0.addStretch(1)
        h0.addWidget(self._excelslot)
        h0.addStretch(1)
        v0.addStretch(1)
        v0.addLayout(h0)
        self._fxlbl = QFixWidthLabel(120)
        self._fxlbl.setText('IO Table\nxlsx')
        self._fxlbl.setAlignment(Qt.AlignCenter)
        v0.addWidget(self._fxlbl)
        h1.addStretch(1)
        h1.addWidget(self._cstslot)
        h1.addStretch(1)
        v0.addLayout(h1)
        self._cslbl = QFixWidthLabel(120)
        self._cslbl.setText('cst fmt\nany')
        self._cslbl.setAlignment(Qt.AlignCenter)
        v0.addWidget(self._cslbl)
        v0.addStretch(1)
        h2.addLayout(v0)
        self._shower = QExcelExampleShower()
        h2.addWidget(self._shower)
        self._layout.addLayout(h2)

        l0, l1, l2 = QHBoxLayout(), QHBoxLayout(), QHBoxLayout()
        lbl = QLabel('Bias   : (')
        lbl.setFixedWidth(90)
        lbl.setFont(LBL_FONT)
        l0.addWidget(lbl)
        self._bias_x = QSpinBox()  # > 0
        self._bias_x.setMinimum(0)
        self._bias_x.setMaximum(100)
        self._bias_x.setValue(bias[0])
        self._bias_x.setFont(LBL_FONT_B)
        self._bias_x.setStyleSheet(f'color: rgba({DODGERBLUE.red()}, {DODGERBLUE.green()}, {DODGERBLUE.blue()}, {DODGERBLUE.alpha()});')
        self._bias_x.valueChanged.connect(self._on_value_changed)
        l0.addWidget(self._bias_x)
        lbl = QLabel(',')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l0.addWidget(lbl)
        self._bias_y = QSpinBox()
        self._bias_y.setMinimum(0)
        self._bias_y.setMaximum(100)
        self._bias_y.setValue(bias[1])
        self._bias_y.setFont(LBL_FONT_B)
        self._bias_y.setStyleSheet(f'color: rgba({OLVORANGE.red()}, {OLVORANGE.green()}, {OLVORANGE.blue()}, {OLVORANGE.alpha()});')
        self._bias_y.valueChanged.connect(self._on_value_changed)
        l0.addWidget(self._bias_y)
        lbl = QLabel(')')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l0.addWidget(lbl)
        self._layout.addLayout(l0)

        lbl = QLabel('Target:(')
        lbl.setFixedWidth(90)
        lbl.setFont(LBL_FONT)
        l1.addWidget(lbl)
        self._target_x = QSpinBox()
        self._target_x.setMinimum(1)
        self._target_x.setMaximum(200)
        self._target_x.setValue(target[0])
        self._target_x.setFont(LBL_FONT_B)
        self._target_x.setStyleSheet(f'color: rgba({MEDIUMPURPLE.red()}, {MEDIUMPURPLE.green()}, {MEDIUMPURPLE.blue()}, {MEDIUMPURPLE.alpha()});')
        self._target_x.valueChanged.connect(self._on_value_changed)
        l1.addWidget(self._target_x)
        lbl = QLabel(',')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l1.addWidget(lbl)
        self._target_y = QSpinBox()
        self._target_y.setMinimum(1)
        self._target_y.setMaximum(200)
        self._target_y.setValue(target[1])
        self._target_y.setFont(LBL_FONT_B)
        self._target_y.setStyleSheet(f'color: rgba({SGGREEN.red()}, {SGGREEN.green()}, {SGGREEN.blue()}, {SGGREEN.alpha()});')
        self._target_y.valueChanged.connect(self._on_value_changed)
        l1.addWidget(self._target_y)
        lbl = QLabel(')')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l1.addWidget(lbl)
        self._layout.addLayout(l1)

        lbl = QLabel('Delta : (')
        lbl.setFixedWidth(90)
        lbl.setFont(LBL_FONT)
        l2.addWidget(lbl)
        self._delta_x = QSpinBox()
        self._delta_x.setMinimum(0)
        self._delta_x.setMaximum(100)
        self._delta_x.setValue(delta[0])
        self._delta_x.setFont(LBL_FONT_B)
        self._delta_x.setStyleSheet(f'color: rgba({DARKGOLDENROD.red()}, {DARKGOLDENROD.green()}, {DARKGOLDENROD.blue()}, {DARKGOLDENROD.alpha()});')
        self._delta_x.valueChanged.connect(self._on_value_changed)
        l2.addWidget(self._delta_x)
        lbl = QLabel(',')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l2.addWidget(lbl)
        self._delta_y = QSpinBox()
        self._delta_y.setMinimum(0)
        self._delta_y.setMaximum(100)
        self._delta_y.setValue(delta[1])
        self._delta_y.setFont(LBL_FONT_B)
        self._delta_y.setStyleSheet(f'color: rgba({DARKSLATEGRAY.red()}, {DARKSLATEGRAY.green()}, {DARKSLATEGRAY.blue()}, {DARKSLATEGRAY.alpha()});')
        self._delta_y.valueChanged.connect(self._on_value_changed)
        l2.addWidget(self._delta_y)
        lbl = QLabel(')')
        lbl.setFixedWidth(12)
        lbl.setFont(LBL_FONT)
        l2.addWidget(lbl)
        self._layout.addLayout(l2)

        self._sheets = QSheetsListWidget()
        self._sheets.onCheckedChanged.connect(self._on_selected_sheets_changed)
        # 设置strengthen
        self._layout.addWidget(self._sheets, 2)


    def _on_selected_sheets_changed(self, idx, state):
        selects = self._sheets.selects
        selects[idx] = True if state == Qt.Checked else False
        sheets = [self._sheets.sheets[i] for i, s in enumerate(selects) if s]
        self.onSelectedSheetsChanged.emit(sheets)

    @property
    def selected_sheets(self) -> list[str]:
        return [self._sheets.sheets[i] for i, s in enumerate(self._sheets.selects) if s]

    @property
    def bias(self) -> tuple[int, int]:
        return self._bias_x.value(), self._bias_y.value()

    @property
    def target(self) -> tuple[int, int]:
        return self._target_x.value(), self._target_y.value()

    @property
    def delta(self) -> tuple[int, int]:
        return self._delta_x.value(), self._delta_y.value()

    def _on_value_changed(self, *args):
        self._shower.bias = self.bias
        self._shower.target = self.target
        self._shower.delta = self.delta
        self._sv['last_excel_offsets'] = self.bias, self.target, self.delta
        self._shower.update()


    def _on_excel_changed(self, path):
        self._sheets.path = path
        self._excelslot.reheight(ARIAL_FONT)
        self.onExcelChanged.emit(path)

    def _on_cst_changed(self, path):
        self._cstslot.reheight(ARIAL_FONT)
        self.onCstChanged.emit(path)

    @property
    def cst_type(self) -> str:  # like 'txt' or 'cst'
        return self._cstslot.filetype

class QPiosTableSelectors(QWidget):
    def __init__(self, parent=None):
        super(QPiosTableSelectors, self).__init__(parent)
        self.initUI()
        self._pios:list[PhysicsIoDef] = []

    def initUI(self):
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(1, 1, 1, 1)
        self._layout.setSpacing(1)
        self.setLayout(self._layout)
        self._checklst = QCheckedListWidget()
        self._layout.addWidget(self._checklst)

    @property
    def pios(self):
        return self._pios

    @pios.setter
    def pios(self, pios):
        self._pios = pios
        self._update_checks()

    @property
    def selects(self):
        return self._checklst.selects

    @property
    def seleted_pios(self):
        return [pio for pio, s in zip(self._pios, self.selects) if s]

    def _update_checks(self):
        self._checklst.clear()
        for pio in self._pios:
            if pio.hiden: continue
            self._checklst.addItem(f"{pio.name}{pio.widthdef}", checked=True if pio.stared else False)

class QExcelTableExportor(QWidget):
    def __init__(self, parent=None):
        super(QExcelTableExportor, self).__init__(parent)
        self.initUI()
        self._excel = None
        self._sv = get_qw_setting()
        if self._sv.has('last_excel') and os.path.exists(self._sv['last_excel']):
            self._left._excelslot.setPath(self._sv['last_excel'])
        if self._sv.has('last_cstfmt') and os.path.exists(self._sv['last_cstfmt']):
            self._left._cstslot.setPath(self._sv['last_cstfmt'])



    def initUI(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(2)
        self.setLayout(self.layout)
        self._left = QExcelFileHeaderCollector()
        self.layout.addWidget(self._left)
        self._right = QPiosTableSelectors()
        self.layout.addWidget(self._right)

        self._left.onExcelChanged.connect(self._on_excel_changed)
        self._left.onSelectedSheetsChanged.connect(self._update_pios)
        self._left.onCstChanged.connect(self._on_cst_changed)

    @property
    def excel(self):
        return self._excel

    def _on_excel_changed(self, path):
        self._sv['last_excel'] = path
        if not path:
            self._excel = None
        else:
            self._excel = pd.ExcelFile(path)
        self._update_pios(self._left.selected_sheets)

    def _on_cst_changed(self, path):
        self._sv['last_cstfmt'] = path

    def _update_pios(self, selected_sheets):
        if self._excel is None:
            self._right.pios = []
            return
        try:
            pios = tbl_export_read(self._excel, self._left.bias, self._left.target, self._left.delta, sheets=selected_sheets)
        except Exception as e:
            PopError("读取失败", f"读取excel文件失败, 请检查bias target delta: {e}")
            return
        self._right.pios = pios


    def export(self, path, overwrite=False):
        if not self._left.cst_type:
            raise ValueError("请指定cst文件")
        txt_tpl = auto_open(self._left._cstslot.path)
        dirname, basename = os.path.split(path)
        fname, ftype = os.path.splitext(basename)
        vfpath = os.path.join(dirname, fname + '.v')
        cstpath = os.path.join(dirname, fname + f'{self._left.cst_type}')

        if not overwrite:
            if os.path.exists(vfpath) or os.path.exists(cstpath):
                raise FileExistsError(f"文件已存在: \n\t'{vfpath}' \nor \n\t'{cstpath}'")

        # 如果vfpath存在, 那么提取目标的用户代码
        old_code = None
        if os.path.exists(vfpath):
            with open(vfpath, 'r') as f:
                old_code = f.read()

        # 生成新的代码
        top_str = GenerateVerilogTopModule(self._right.seleted_pios, old_code)
        cst_str = EvalCst(txt_tpl, self._right.seleted_pios)


        with open(vfpath, 'w') as f:
            f.write(top_str)
        with open(cstpath, 'w') as f:
            f.write(cst_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QExcelTableExportor()
    w.show()
    sys.exit(app.exec_())


