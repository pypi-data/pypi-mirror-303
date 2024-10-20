from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QColor
from rbpop.utils import *

import random

class PopWin(QWidget):
    RESET_PATIENCE = 100
    MINIUM_DELTA = 1

    def __init__(self, ct: int, *, anim_ratio: float = 0.3, split_num: int = 8, up_ratio: int = 2, min_opacity=0.1, offset=0, all=None, on_death=None):
        """

        :param ct: 显示时间，单位毫秒
        """
        super().__init__(None)
        self.initUI()
        # 置顶|无边框

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.SplashScreen)

        # ct
        self.pause = 0
        self.ct = int(ct * (1 - anim_ratio))
        self.up_ratio = up_ratio
        self.step = int(ct * anim_ratio) // 100
        self.anim_total = int(ct * anim_ratio) // self.step
        self.up_max = self.up_left = self.anim_total // split_num  # 这里是透明度增加的剩余次数
        self.keep_max = self.keep_left = self.ct // self.step
        self.down_max = self.down_left = ((split_num - 1) * self.anim_total) // split_num  # 这里是透明度减少的剩余次数

        # fit to screen
        self.offset = offset
        self.start_top = 0

        # record start opacity
        self.start_opacity = self.windowOpacity()
        # 7/8 * o_step: 100% * start
        # o_step: 100% * start / (7/8)
        self.opacity_step = ((self.start_opacity - min_opacity) * split_num / (split_num - 1)) / self.anim_total  # 总的透明度/总的步数
        self.setWindowOpacity(self.start_opacity - self.opacity_step * self.up_left * self.up_ratio)  # 0.5 -> 1.0 --------> 0.0 -> destroy

        # new opacity timer
        self._oflag = False
        self.opacity_timer = QTimer(self)
        self.opacity_timer.setInterval(self.step)
        self.opacity_timer.timeout.connect(self.opacity_timeout)

        # capacitor
        self.all = all
        self.on_death = on_death
        self.patience = self.RESET_PATIENCE

    def Start(self):
        if self._oflag:
            return
        self._oflag = True
        self.fit_rb()
        self.start_top = self.geometry().top()
        # start timer
        self.opacity_timer.start()

    def initUI(self):
        raise NotImplementedError

    def fit_rb(self, ratio=1.0):
        # 贴合到屏幕右下角，但是要在任务栏上面
        screen = QApplication.primaryScreen()
        available_geometry = screen.availableGeometry()
        screen_geometry = screen.geometry()

        # 获取任务栏的高度
        taskbar_height = screen_geometry.height() - available_geometry.height()

        # left(x) top(y)
        self_x, self_y = self.geometry().left(), self.geometry().top()

        # target pos
        target_x = screen_geometry.width() - self.width()
        target_y = screen_geometry.height() - self.height() - taskbar_height - self.offset

        # delta
        delta_x = int(ratio * (target_x - self_x))
        delta_y = int(ratio * (target_y - self_y))

        if abs(delta_x) > self.MINIUM_DELTA:
            target_x = self_x + delta_x
        elif abs(target_x - self_x) > self.MINIUM_DELTA:
            target_x = int(0.5 * (self_x + target_x))

        if abs(delta_y) > self.MINIUM_DELTA:
            target_y = self_y + delta_y
        elif abs(target_y - self_y) > self.MINIUM_DELTA:
            target_y = int(0.5 * (self_y + target_y))

        self.move(target_x, target_y)

    def opacity_timeout(self):
        """
        先增加透明度，然后减少透明度
        :return:
        """
        if self.pause > 0:
            self.setWindowOpacity(self.start_opacity)
            if self.up_left > 0:
                self.up_left = 0
            if self.keep_left <= 0:
                self.down_left = self.down_max

            if self.patience > 0:
                self.patience -= 1
            else:
                self.pause = 0
            return

        self.fit_rb(0.1)

        if self.up_left > 0:
            self.up_left -= 1
            self.setWindowOpacity(self.windowOpacity() + self.opacity_step * self.up_ratio)
        elif self.keep_left > 0:
            self.keep_left -= 1
        elif self.down_left > 0:
            self.down_left -= 1
            self.setWindowOpacity(self.windowOpacity() - self.opacity_step)
        else:
            self.opacity_timer.stop()
            self.close()

    def closeEvent(self, event) -> None:
        if self.on_death:
            self.on_death()
        self.destroy()

    def enterEvent(self, event):
        self.lock_self()
        if self.all:
            for win in self.all:
                win.lock_self()

    def leaveEvent(self, event):
        self.unlock_self()
        if self.all:
            for win in self.all:
                win.unlock_self()

    def lock_self(self):
        self.pause += 1

    def unlock_self(self):
        self.pause -= 1
        if self.pause < 0:
            self.pause = 0

