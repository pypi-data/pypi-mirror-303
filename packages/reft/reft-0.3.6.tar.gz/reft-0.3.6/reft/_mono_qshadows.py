from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPainter, QImage, QColor, QPixmap, QPen, QBrush, QFont
from PyQt5.QtCore import Qt, QRect

class QShadowLabel(QLabel):
    def __init__(self, text, text_color:QColor, shadow_color:QColor=None, shadow_radius:int=3, reversed:bool=False, parent=None):
        super(QShadowLabel, self).__init__(parent)
        self._txt_color = text_color
        self._shd_color = shadow_color or QColor(text_color.red() // 4, text_color.green() // 4, text_color.blue() // 4, text_color.alpha())
        self._radius = shadow_radius
        self._reversed = reversed
        self.setText(text)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))

        # 绘制阴影
        _init_alpha = self._shd_color.alpha()
        color = QColor(self._shd_color.red(), self._shd_color.green(), self._shd_color.blue())
        for i in range(self._radius, -1, -1):
            painter.translate(i, i)
            _coef = (i / self._radius) if not self._reversed else (1 - i / self._radius)
            color.setAlpha(int(_init_alpha * _coef + .5))
            painter.setPen(color)
            painter.setFont(self.font())
            painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, self.text())
            painter.translate(-i, -i)

        painter.setPen(QPen(self._txt_color))
        painter.setFont(self.font())
        painter.drawText(0, 0, self.width(), self.height(), Qt.AlignCenter, self.text())
