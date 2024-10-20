import numpy as np
from rbpop.win_manager import WinManager
from rbpop.win_pop import PopWin
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPolygon, QColor, QBrush, QPen
from PyQt5.Qt import Qt, QPoint, QLine

X_MARGIN, Y_MARGIN = 5, 3
BTNX_MARGIN, BTNY_MARGIN = 2, 1
TITLE_STYLE = {"font-family": "Consolas", "font-size": "16px", "font-weight": "bold"}
MESSAGE_STYLE = {"font-family": "Consolas", "font-size": "14px"}
COLOR_INFO = "rgb(140, 190, 122)"
COLOR_WARN = "rgb(195, 185, 72)"
COLOR_ERROR = "rgb(190, 140, 122)"


class CloseButton(QPushButton):
    def __init__(self, parent=None, back_color:str=None, color:str=None, border_color:str=None, *, border=0):
        super().__init__(parent)
        if back_color is None:
            back_color = 'red'
        self.back_color = back_color
        if color is None:
            color = 'black'
        self.font_color = color
        if border_color is None:
            border_color = 'black'
        self.border_color = border_color
        self.border_width = border
        self.initUI()

    def initUI(self):
        self.setFixedSize(16, 16)
        self.setText('X')
        style = ""
        style += f"background-color:{self.back_color};"
        style += f'font-family: "Consolas";'
        style += f'font-size: 12px;'
        style += f"font-weight:bold;"
        style += f"color:{self.font_color};"
        style += f"padding-left:0px;"
        style += f"padding-top:0px;"
        style += f"border-radius:8px;"
        style += f"border: {self.border_width}px solid {self.border_color};"


        self.setStyleSheet(style)

    def moveToCornor(self):
        parent = self.parent()
        if not parent:
            return

        size = parent.size()
        size.setWidth(size.width() - 2 * BTNX_MARGIN)
        size.setHeight(size.height() - 2 * BTNY_MARGIN)
        self.move(BTNX_MARGIN + size.width() - self.width(), BTNY_MARGIN)




def QSS_Str2Dict(qss_txt:str):
    _column_splits = qss_txt.split(';')
    qss_dict = {}
    for item in _column_splits:
        if not item:
            continue
        # find :
        _index = item.find(':')
        if _index == -1:
            raise ValueError(f"Unexpected qss: '{item}' in '{qss_txt}'")
        # split key and value
        key, value = item[:_index], item[_index + 1:]
        # remove blank start | end
        while key[0] in [' ', '\t']:
            key = key[1:]
        while key[-1] in [' ', '\t']:
            key = key[:-1]
        key = key.lower()

        qss_dict[key] = value
    return qss_dict

def QSS_Dict2Str(qss_dict:dict):
    txt = ""
    for k, v in qss_dict.items():
        txt += f"{k}:{v};"

    return txt


class _RbpopMessage(PopWin):
    def __init__(self, msg:str, title=None, ct:int=4000, *, msg_style=None, title_style=None, close=False, **kwargs):
        self.msg = msg
        self.msg_style = msg_style
        self.title = title
        self.title_style = title_style
        self.close_btn = close
        super(_RbpopMessage, self).__init__(ct, **kwargs)

    def initUI(self):
        self.resize(360, 120)
        # self.setStyleSheet(f"background-color: {COLOR_INFO};")
        self.setWindowOpacity(0.8)

        # Add a msg label
        self.lbl_msg = QLabel(self)
        self.lbl_msg.setText(self.msg)
        # Consolas 12, Center
        self.lbl_msg.setAlignment(Qt.AlignCenter)
        # fit widget
        self.lbl_msg.move(X_MARGIN, Y_MARGIN)
        _size = self.size()
        _size.setWidth(_size.width() - 2 * X_MARGIN)
        _size.setHeight(_size.height() - 2 * Y_MARGIN)
        self.lbl_msg.resize(_size)
        msg_qss = MESSAGE_STYLE.copy()
        if self.msg_style is not None:
            msg_qss.update(QSS_Str2Dict(str(self.msg_style)))
        self.lbl_msg.setStyleSheet(QSS_Dict2Str(msg_qss))

        # Add a title label
        if self.title is not None:
            self.lbl_title = QLabel(self)
            self.lbl_title.move(X_MARGIN, Y_MARGIN)
            self.lbl_title.setText(str(self.title))
            self.lbl_title.setAlignment(Qt.AlignLeft)
            title_qss = TITLE_STYLE.copy()
            if self.title_style is not None:
                title_qss.update(QSS_Str2Dict(str(self.title_style)))
            self.lbl_title.setStyleSheet(QSS_Dict2Str(title_qss))


        # closebutton
        if self.close_btn:
            # self.btn_close = CloseButton(self, "rgb(195, 125, 105)", "rgb(50, 50, 50)")
            self.btn_close = CloseButton(self, "rgb(195, 195, 195)", "rgb(50, 50, 50)")
            self.btn_close.moveToCornor()
            self.btn_close.clicked.connect(self.close)



class RbpopInfo(_RbpopMessage):
    def initUI(self):
        super(RbpopInfo, self).initUI()
        self.setStyleSheet(f"background-color: {COLOR_INFO};")

class RbpopWarn(_RbpopMessage):
    def initUI(self):
        super(RbpopWarn, self).initUI()
        self.setStyleSheet(f"background-color: {COLOR_WARN};")

class RbpopError(_RbpopMessage):
    def initUI(self):
        super(RbpopError, self).initUI()
        self.setStyleSheet(f"background-color: {COLOR_ERROR};")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wm = WinManager()
    wm.add(RbpopInfo("This is a message. | 带有关闭按钮.", 'Information:', 5000, close=True))
    wm.add(RbpopWarn("This is a message. | 没有标题.", ct=6500))
    wm.add(RbpopError("This is a message. | 红色的标题.", 'Error:', 8000, title_style="color:red"))

    sys.exit(app.exec_())

