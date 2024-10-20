from PyQt5.QtWidgets import QApplication

from rbpop.win_pop import PopWin
# 控制弹窗的显示


class WinManager:
    def __init__(self):
        self.win_list = []

    @property
    def offset(self):
        # sum of all win's height
        _sum = 0
        for win in self.win_list:
            _sum += win.geometry().height()
        return _sum

    def _start(self):
        for win in self.win_list:
            win.Start()
            win.show()

    def add(self, win:PopWin):
        win.offset = self.offset
        self.win_list.append(win)
        win.all = self.win_list
        win.on_death = lambda: self.remove(win)
        win.Start()
        win.show()

    def remove(self, win:PopWin):
        # try index
        _index = -1
        for i, w in enumerate(self.win_list):
            if w == win:
                _index = i
                break
        if _index == -1:
            return False
        _left, _right = self.win_list[:_index], self.win_list[_index+1:]
        _target = self.win_list[_index]
        _tar_height = _target.geometry().height()
        # win at right's offset should be changed
        for win in _right:
            win.offset -= _tar_height

        # remove
        self.win_list.pop(_index)
        return True

    def hide_all(self):
        for win in self.win_list:
            win.hide()

    def show_all(self):
        for win in self.win_list:
            win.show()


_GLOBAL_WM = [None]

def QPop(pop_win_inst:PopWin):
    if _GLOBAL_WM[0] is None:
        _GLOBAL_WM[0] = WinManager()

    _GLOBAL_WM[0].add(pop_win_inst)
