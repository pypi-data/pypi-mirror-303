from rbpop.win_manager import WinManager, QPop
from rbpop.prefab import *
from rbpop.win_pop import PopWin




if __name__ == '__main__':
    import sys
    import random
    from PyQt5.QtWidgets import QApplication, QLabel
    from PyQt5.Qt import Qt

    class TestWin(PopWin):
        def initUI(self):
            self.resize(360, 120)
            color = f"rgb({random.randint(100, 200)}, {random.randint(150, 200)}, {random.randint(100, 150)})"
            self.setStyleSheet(f"background-color: {color};")
            self.setWindowOpacity(0.8)

            # Add a label, show self
            self.label = QLabel(self)
            self.label.setText(self.__class__.__name__ + '\n' + str(hex(id(self))))
            # Consolas 12, Center
            self.label.setStyleSheet("font-family: Consolas; font-size: 14px;")
            self.label.setAlignment(Qt.AlignCenter)
            # fit widget
            self.label.resize(self.size())

    app = QApplication(sys.argv)
    wm = WinManager()
    wm.add(TestWin(2000))
    wm.add(TestWin(3000))
    wm.add(TestWin(4000))

    sys.exit(app.exec_())








