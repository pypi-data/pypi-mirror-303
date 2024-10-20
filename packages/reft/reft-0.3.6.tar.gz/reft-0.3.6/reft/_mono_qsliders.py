from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import pyqtSignal, QEvent

class QDoubleSlider(QSlider):
    RATIO = 1000000
    MINIMUM = -2147483647  # use this as real minimum value
    monoChanged = pyqtSignal(float)

    def __init__(self, direction, minimum: float, maximum: float, step: float, parent=None):
        super().__init__(direction, parent)
        self.bias = 0
        self._last_value = self.MINIMUM
        self._on_super_value_changed_flag = False
        self._min, self._max, self._step = minimum, maximum, step
        self.range_max, self.step = self._fit_bounds()
        super().setValue(self.MINIMUM)
        super().valueChanged.connect(self._super_value_changed)

    def _super_value_changed(self, value: int):
        if self._on_super_value_changed_flag:return
        self._on_super_value_changed_flag = True
        # calc a rounded value
        delta = value - self.MINIMUM

        half_step = self.step // 2

        if delta % self.step >= half_step:
            value = self.MINIMUM + int(delta / self.step + 0.5) * self.step
        else:
            value = self.MINIMUM + int(delta / self.step) * self.step

        if value < self.MINIMUM:
            value = self.MINIMUM
        elif value > self.range_max:
            value = self.range_max

        if value == self._last_value:
            self._on_super_value_changed_flag = False
            return

        self._last_value = value
        super().setValue(value)

        rel_value = (value + self.bias) / self.RATIO
        self.monoChanged.emit(rel_value)

        self._on_super_value_changed_flag = False
        return value

    def _fit_bounds(self) -> tuple[int, int]:
        if self._step <= 0:
            raise ValueError("Step cannot be less than or equal to 0.")
        if self._min >= self._max:
            raise ValueError("Minimum cannot be greater than or equal to maximum.")

        minimum = int(self._min * self.RATIO)
        maximum = int(self._max * self.RATIO)
        step = int(self._step * self.RATIO)
        delta = minimum - self.MINIMUM

        self.bias = delta

        super().setMinimum(self.MINIMUM)
        super().setMaximum(maximum - delta)
        super().setSingleStep(step)
        super().setPageStep(step)
        return (maximum - delta, step)

    def value(self) -> float:
        return (super().value() + self.bias) / self.RATIO

    def setValue(self, value: float):
        super().setValue(int(value * self.RATIO - self.bias))
        self.monoChanged.emit(value)

    def setMinimum(self, minimum: float):
        self._min = minimum
        self.range_max, self.step = self._fit_bounds()

    def setMaximum(self, maximum: float):
        self._max = maximum
        self.range_max, self.step = self._fit_bounds()

    def setSingleStep(self, step: float):
        self._step = step
        self.range_max, self.step = self._fit_bounds()

    def setPageStep(self, a0):
        raise NotImplementedError("Page step is not supported in QDoubleSlider.")


class QIntSlider(QSlider):
    monoChanged = pyqtSignal(int)

    def __init__(self, direction, minimum: int, maximum: int, step: int=1, parent=None):
        super().__init__(direction, parent)
        self._last_value = minimum
        self._on_super_value_changed_flag = False
        super().setMinimum(minimum)
        super().setMaximum(maximum)
        super().setSingleStep(step)
        super().setPageStep(step)
        super().setValue(minimum)
        super().valueChanged.connect(self._super_value_changed)

    def _super_value_changed(self, value: int):
        if self._on_super_value_changed_flag:return
        self._on_super_value_changed_flag = True
        # calc a rounded value
        minimum = self.minimum()
        maximum = self.maximum()
        delta = value - minimum
        step = self.singleStep()

        half_step = step // 2

        if delta % step >= half_step:
            value = minimum + int(delta / step + 0.5) * step
        else:
            value = minimum + int(delta / step) * step

        value = int(value + .5)

        if value < minimum:
            value = minimum
        elif value > maximum:
            value = maximum

        if value == self._last_value:
            self._on_super_value_changed_flag = False
            return

        self._last_value = value
        super().setValue(value)

        self.monoChanged.emit(value)

        self._on_super_value_changed_flag = False
        return value

    def setSingleStep(self, step: int):
        super().setSingleStep(step)
        super().setPageStep(step)

    def setPageStep(self, a0):
        raise NotImplementedError("Page step is not supported in QDoubleSlider.")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
    from PyQt5.QtCore import Qt

    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    double_slider = QDoubleSlider(Qt.Horizontal,0.0, 100.0, 5.0)
    double_slider.monoChanged.connect(lambda value: print(f"Value: {value:.6f}"))
    layout.addWidget(double_slider)

    int_slider = QIntSlider(Qt.Horizontal,0, 100, 5)
    int_slider.monoChanged.connect(lambda value: print(f"Value: {value}"))
    layout.addWidget(int_slider)

    window.setLayout(layout)
    window.show()
    app.exec_()