import math
import time
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor
from pyipcore.ipcore import IpCore
from pyipcore.ui_utils import *


MODULE_COLOR = DODGERBLUE
BORDER_COLOR = QColor(0, 0, 0, 25)
FILL_BACKGROUND = LT_YELLOW
INPUT_LINE_COLOR = SGGREEN.lighter(120)
OUTPUT_LINE_COLOR = OLVORANGE
class IpCoreView(DraggableGraphicsView):
    def __init__(self, parent=None):
        super(IpCoreView, self).__init__(parent)
        self._font = QFont("Microsoft YaHei UI", 16)
        self._font_width = 12
        self._font_height = 32
        self._font_margin = 8
        self._line_width = 2
        self._font_margin_per_width = 0
        self._line_width_per_width = 0.1
        self._current_width = 1
        self._body_margin = 20
        self._arrow_size = 80
        self._arrow_margin = 5

    @property
    def cw(self):
        return self._current_width

    @cw.setter
    def cw(self, value):
        self._current_width = value

    @property
    def font_height(self):
        return self._font_height
    @property
    def font_width(self):
        return self._font_width

    @property
    def item_size(self):
        return self.font_height + self._font_margin + self._font_margin_per_width * self.cw

    @property
    def line_width(self):
        _cw = self.cw
        if _cw > 32:
            _ln4 = math.floor(math.log2(_cw)) - 4
            _cw = 16 + 16 * _ln4 + (_cw - 2 ** (_ln4 + 4)) / 2 ** _ln4
        return self._line_width + (max(self._line_width_per_width * _cw, 1) if _cw > 1 else 0)

    @property
    def margin(self):
        return self._body_margin

    def _get_item_size_lst(self, lps, rps, bps) -> tuple:
        ls, rs, bs = [], [], []
        for lp in lps:
            self.cw = lp['w'] if lp else 1
            ls += [self.item_size]
        for rp in rps:
            self.cw = rp['w'] if rp else 1
            rs += [self.item_size]
        for bp in bps:
            self.cw = bp['w'] if bp else 1
            bs += [self.item_size]
        return ls, rs, bs


    def render_ipcore(self, ipcore: IpCore):
        """
        Render the IP core.
        :param ipcore: IP core
        """

        # print("enter draw")
        ports = ipcore.ports            # list of ports:dict
        lefts = ipcore.lefts            # list of port_name:str  意味着该端口强制放在左边
        rights = ipcore.rights          # list of port_name:str  意味着该端口强制放在右边
        separators = ipcore.separators  # list of port_name:str  意味着该端口后面需要插入分割线

        # 1. generate left_ports & right_ports & bottom_ports. 特殊占位符: None
        # print("1.generate")
        left_ports, right_ports, bottom_ports = [], [], []
        # 插入sep
        for sep in separators:
            # find sep in ports
            index = 0
            for port in ports:
                if port['name'] == sep:
                    break
                index += 1
            # insert sep
            if index >= len(ports):
                continue
            _copy = ports[index].copy()
            _copy['width'] = _copy['w'] = None
            if (index + 1) >= len(ports):
                ports.append(_copy)
            else:
                ports.insert(index + 1, _copy)

        for port in ports:
            if port['name'] in lefts:
                left_ports.append(port if port['w'] is not None else None)
            elif port['name'] in rights:
                right_ports.append(port if port['w'] is not None else None)
            elif port['direction'] == 'input':
                left_ports.append(port if port['w'] is not None else None)
            elif port['direction'] == 'output':
                right_ports.append(port if port['w'] is not None else None)
            else:
                bottom_ports.append(port if port['w'] is not None else None)

        # remove None at the end
        if left_ports and left_ports[-1] is None:
            left_ports.pop(-1)
        if right_ports and right_ports[-1] is None:
            right_ports.pop(-1)
        if bottom_ports and bottom_ports[-1] is None:
            bottom_ports.pop(-1)

        # 2. calculate the width & height of the view
        # print("2.calculate")
        has_bottom = len(bottom_ports) > 0
        name_width = self.font_height * len(ipcore.name)
        lslst, rslst, bslst = self._get_item_size_lst(left_ports, right_ports, bottom_ports)
        left_ports_height,right_ports_height, bottom_ports_width = sum(lslst), sum(rslst), sum(bslst)
        max_left_length = max([len(port['name'] + port['width']) for port in left_ports if port] + [0]) * self.font_width
        max_right_length = max([len(port['name'] + port['width']) for port in right_ports if port] + [0]) * self.font_width
        max_bottom_length = max([len(port['name'] + port['width']) for port in bottom_ports if port] + [0]) * self.font_width
        body_width = 4 * self.margin + max(max_left_length + max_right_length, bottom_ports_width, name_width) + 2 * self._line_width + 2 * self._arrow_margin + 2 * self._arrow_size
        body_height = 3 * self.margin + max(left_ports_height, right_ports_height) + max_bottom_length + 2 * self._line_width + (self._arrow_size + self._arrow_margin) * has_bottom

        # 3. draw the view
        # print("Start Draw.")
        self.clear()
        br_width = body_width - 2 * self._arrow_size - 2 * self._arrow_margin - 2 * self.margin
        br_height = body_height - (self._arrow_margin + self._arrow_size) * has_bottom - self.margin
        # draw header name
        header_item = self.text(ipcore.name, 0,  - self.font_height, self._font, MODULE_COLOR)  # adjust later
        # draw body rect
        self.rectangle(self._arrow_size + self._arrow_margin + self.margin, 0, br_width, br_height, BORDER_COLOR, self.line_width, FILL_BACKGROUND)
        # draw left arrows and text
        _y_bias = 0
        for i in range(len(left_ports)):
            if left_ports[i] is not None:
                self.cw = left_ports[i]['w']
                if left_ports[i]['direction'] in ['input', 'inout']:
                    self.arrow(self.margin, self.margin + _y_bias + lslst[i] / 2, self._arrow_size + self.margin, self.margin + _y_bias + lslst[i] / 2, INPUT_LINE_COLOR, self.line_width, self.line_width + 10)
                if left_ports[i]['direction'] in ['output', 'inout']:
                    self.arrow(self._arrow_size + self.margin, self.margin + _y_bias + lslst[i] / 2, self.margin, self.margin + _y_bias + lslst[i] / 2, OUTPUT_LINE_COLOR, self.line_width, self.line_width + 10)
                self.text(left_ports[i]['name'] + left_ports[i]['width'], self._arrow_size + self.margin + self._arrow_margin + self._line_width + 2, self.margin + _y_bias, self._font, Qt.black)
            _y_bias += lslst[i]
        # draw right arrows
        _y_bias = 0
        for i in range(len(right_ports)):
            if right_ports[i] is not None:
                self.cw = right_ports[i]['w']
                if right_ports[i]['direction'] in ['output', 'inout']:
                    self.arrow(body_width - self._arrow_size - self.margin, self.margin + _y_bias + rslst[i] / 2, body_width - self.margin, self.margin + _y_bias + rslst[i] / 2, OUTPUT_LINE_COLOR, self.line_width, self.line_width + 10)
                if right_ports[i]['direction'] in ['input', 'inout']:
                    self.arrow(body_width - self.margin, self.margin + _y_bias + rslst[i] / 2, body_width - self._arrow_size - self.margin, self.margin + _y_bias + rslst[i] / 2, INPUT_LINE_COLOR, self.line_width, self.line_width + 10)
                self.text(right_ports[i]['name'] + right_ports[i]['width'], body_width - self._arrow_size - self.margin - self._arrow_margin - self._line_width - 2, self.margin + _y_bias, self._font, Qt.black, use_r=True)

            _y_bias += rslst[i]
        # draw bottom arrows
        _x_bias = br_width / (len(bottom_ports) + 1) + self._arrow_size + self._arrow_margin + self._line_width + 2
        for i in range(len(bottom_ports)):
            if bottom_ports[i] is not None:
                self.cw = bottom_ports[i]['w']
                if bottom_ports[i]['direction'] in ['input', 'inout']:
                    self.arrow(_x_bias + bslst[i] / 2, body_height, _x_bias + bslst[i] / 2, body_height - self._arrow_size - self._arrow_margin - self._line_width - 2, Qt.black, self.line_width, self.line_width + 10)
                if bottom_ports[i]['direction'] in ['output', 'inout']:
                    self.arrow(_x_bias + bslst[i] / 2, body_height - self._arrow_size - self._arrow_margin - self._line_width - 2, _x_bias + bslst[i] / 2, body_height, Qt.black, self.line_width, self.line_width + 10)
                self.text(bottom_ports[i]['name'] + bottom_ports[i]['width'], _x_bias + bslst[i] / 2 + self.font_height / 2 + self._line_width + 2, br_height - self.margin, self._font, Qt.black, rotate=90, use_b=True)
            _x_bias += bslst[i]


        # adjust
        total_rect = self.scene().itemsBoundingRect()
        self.move_item_center(header_item, total_rect.center().x(), total_rect.top())

        # Effect
        self.effect_shallow()
        self.scale_tofit()


    def scale_tofit(self):
        """
        Scale the view to fit the window.
        """
        rf = self.scene().itemsBoundingRect()
        rf.adjust(-self.margin, -self.margin, self.margin, self.margin)
        if rf.width() > self.width():
            whratio = self.width() / self.height()
            rfratio = rf.width() / rf.height()
            if rfratio > whratio:
                rf.adjust(0, 0, rf.height() / whratio - rf.width(), 0)

        self.fitInView(rf, Qt.KeepAspectRatio)
        self.scene().update()

    def render_error(self, error: str):
        """
        Render the error message.
        :param error: error message
        """
        self.clear()
        self.text(error, 0, 0, self._font, Qt.red)
        self.effect_shallow()
        self.pixelize()
        self.scale_tofit()


if __name__ == '__main__':
    ip = IpCore("", 'test')
    d = ip.dict
    # d['WIDTH'] = 32
    # d['add_clr'] = False
    # save to a counter~.v file
    # with open('counter~.v', 'w', encoding='utf-8') as f:
    #     f.write(t)
    # test = "module Counter #(parameter WIDTH=16,parameter RCO_WIDTH=4"
    # txt = ip.decorate_paragraph(test, 30, 35, "WIDTH", 0)
    # print(txt)
    # txt = ip.decorate_paragraph(txt, 33, 35, "WIDTH", 0)
    print(ip.name)
    print(ip.author)
    print(ip.dict)
    print(ip.types)
    print(ip.ports)
    print(ip.lefts)
    print(ip.rights)
    print(ip.separators)
    # print(ip.icode)
    # print(ip.built)
