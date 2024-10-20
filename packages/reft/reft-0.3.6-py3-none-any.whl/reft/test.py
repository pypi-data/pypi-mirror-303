import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QColor, QPixmap
# Qpoint
from PyQt5.QtCore import QPoint

def create_triangle_pixel(size: int, color: QColor = QColor("black"), direct="down"):
    assert direct in ["down", "right"], "direct must be 'down' or 'right'"
    # 创建一个 QPixmap 对象，参数为图标大小和是否透明
    pm = QPixmap(size, size)
    pm.fill(Qt.transparent)  # 设置背景透明

    # 创建 QPainter 对象用于绘制
    painter = QPainter(pm)
    painter.setRenderHint(QPainter.Antialiasing)  # 设置反锯齿
    painter.setPen(Qt.NoPen)  # 不绘制边框
    painter.setBrush(color)  # 设置填充颜色

    # 绘制三角形
    if direct == "down":
        points = [QPoint(0, 0), QPoint(size, 0), QPoint(size // 2, size)]  # 三角形的三个顶点
    else:
        points = [QPoint(0, 0), QPoint(0, size), QPoint(size, size // 2)]  # 三角形的三个顶点
    painter.drawPolygon(*points)  # 绘制三角形

    painter.end()  # 完成绘制
    # save it
    pm.save("triangle.png")
    return pm

# 使用图标
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
app = QApplication([])

# 使用函数创建图标
triangle_down_pixel = create_triangle_pixel(16)  # 创建一个大小为 16x16 的向下三角形图标
triangle_right_pixel = create_triangle_pixel(16, direct="right")  # 创建一个大小为 16x16 的向右三角形图标

w = QWidget()
w.setLayout(QVBoxLayout())
w.setWindowTitle("Triangle Icon")
lbl0 = QLabel()
lbl0.setFixedSize(16, 16)
lbl0.setPixmap(triangle_down_pixel)  # 设置图标
w.layout().addWidget(lbl0)
lbl1 = QLabel()
lbl1.setFixedSize(16, 16)
lbl1.setPixmap(triangle_right_pixel)  # 设置图标
w.layout().addWidget(lbl1)
w.setFixedSize(20, 20)
w.show()
sys.exit(app.exec_())

