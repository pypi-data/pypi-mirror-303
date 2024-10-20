"""
支持以下attrs-inspector:
* attr可以使用动态参数，传入VSO xxx VEO来指定动态参数
* 可以被ifbr语句控制

如果名称前有**，表示可以多次出现在一个vardef前

Type(X)  ;# 允许指定基础类型
    X can be one of the following types:
    - int   (QSpinBox)
    - float (QDoubleSpinBox)
    - str   (QLineEdit)
    - bool  (QCheckBox)
    * None会被解释为str类型的""
Range(X[, Y[, S) ;# 允许指定范围
    - X: 当只有一个参数时，表示最大值；否则表示最小值
    - Y: 最大值
    - S: 步长 必须>0
    * 这实质上会创建一个python range对象，所以范围的取值是左闭右开的 [X, Y)
    * 当描述符与Type(int)结合时，提升QSpinBox为QSlider，且步长默认值为1
    * 当描述符与Type(float)结合时，提升QDoubleSpinBox为QSlider，且步长默认值为0.01
    * 当描述符与Type(int|float)结合并且S的类型不匹配时，会抛出异常
    * 当描述符与Type(str|bool)结合时，会抛出异常
Enum(X, Y, Z, ...) ;# 强制要求输入必须为枚举值
    * X, Y, Z, ...: 枚举值
    * 当描述符与Type(int|float|str)结合时，提升QXXX为QComboBox
    * QComboBox和QSlider互相冲突，最终会以QComboBox为准
    * 当描述符与Type(bool)结合时，会抛出异常
Color(fg[, bg) ;# 设置整个控件的全局前景色和全局背景色
    * fg: 前景色
    * bg: 背景色
    * 支持 #RRGGBB, rgb(r, g, b) 格式
Tooltip(X) ;# 设置控件的提示信息
Label(X) ;# 设置别名标签
    * 如果没有设置别名标签，会使用变量名作为标签的文本
**Group([X[,color) ;# 接下来的控件会被分组到Group:X中
    * X: 分组的标题
    * color: 分组的前景色
    * 当没有指定X时，接下来的控件会重新回到上一级分组
    * 一个Group是可以被折叠起来的
**Header(X[, color) ;# 在此处插入一个标题，例如 X:
    * X: 标题
    * color: 前景色
**Title(X[, color) ;# 在此处插入一个标题，例如 X:
    * X: 标题
    * color: 前景色
    * Title是一个比Header拥有更大字体和特殊阴影效果的标题
**Separator() ;# 在此处插入一个分隔符
**Space([x) ;# 在此处插入一个空白控件，高度为x.
    * x: 高度
    * 当没有指定x时，高度为标准间距
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox, QLineEdit, QCheckBox, QComboBox, QPushButton, QApplication, QFrame, QScrollArea
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QRect, pyqtSignal
from PyQt5.QtGui import QFont, QPainter, QPen, QColor, QBrush, QPixmap, QIcon
from reft._mono_qsliders import QDoubleSlider, QIntSlider
from reft._mono_qshadows import QShadowLabel
from reft.mono import Mono, MonoAttr
from reft._rangef import rangef, find_closest
from qwork import QTextEdit
import warnings
import types
import sys
import re

warnings.filterwarnings("ignore", category=DeprecationWarning)
BUILTIN_TYPES = (
    int, float, complex, str, bool, bytes, bytearray, memoryview,
    tuple, list, dict, set, frozenset,
    types.FunctionType, types.BuiltinFunctionType, types.MethodType,
    types.LambdaType, types.CodeType, types.ModuleType,
    types.TracebackType, types.FrameType, types.GeneratorType,
    types.CoroutineType
)


def str_crop(s, size=200):
    s = str(s)
    if len(s) > size:
        return s[:size] + '...'
    return s


def _is_builtin_instance(inst) -> bool:
    """
    检查对象 inst 是否是 Python 的内置类型实例。

    参数:
    inst -- 要检查的对象

    返回:
    如果是内置类型实例，则返回 True，否则返回 False
    """
    # 定义一个元组，包含所有内置类型的类型

    # 检查 inst 的类型是否在这个元组中
    return isinstance(inst, BUILTIN_TYPES)


def api_hide_layout_widgets(layout):
    for i in range(layout.count()):
        item = layout.itemAt(i)
        widget = item.widget()
        if widget:
            widget.hide()
        else:
            if item.layout():
                api_hide_layout_widgets(item.layout())


def api_show_layout_widgets(layout):
    for i in range(layout.count()):
        item = layout.itemAt(i)
        widget = item.widget()
        if widget:
            if getattr(widget, 'ad', {}).get('when', True):
                widget.show()
            else:
                widget.hide()
        else:
            if item.layout():
                api_show_layout_widgets(item.layout())


def api_create_triangle_pixel(size: int, color: QColor = QColor("black"), direct="down"):
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


def api_merge_colors(*qc):
    # 初始化颜色累加器
    red_sum, green_sum, blue_sum, alpha_sum = 0, 0, 0, 0
    count = 0  # 权重和

    # 累加所有颜色的 RGB 和 Alpha 值
    for color in qc:
        if isinstance(color, tuple):
            weight, color = color
        else:
            weight = 1
        red_sum += color.red() * weight
        green_sum += color.green() * weight
        blue_sum += color.blue() * weight
        alpha_sum += color.alpha() * weight
        count += weight

    # 计算平均值
    if count > 0:
        red_avg = red_sum // count
        green_avg = green_sum // count
        blue_avg = blue_sum // count
        alpha_avg = alpha_sum // count
    else:
        # 如果没有传入任何颜色，返回一个默认的透明颜色
        return QColor(0, 0, 0, 0)

    # 创建并返回新的 QColor 对象
    return QColor(red_avg, green_avg, blue_avg, alpha_avg)


class FTMonoaRuntimeEvalError(Exception):
    def __init__(self, monoa, msg):
        txt = f"\n\t{str(msg)}\n\n\tLineno:{monoa.lineno}, Target:\n\t\t{monoa}"
        super().__init__(txt)


class FTQMonoWidgetRecvObjectError(Exception):
    pass


class FTMonoaRuntimeUnexpectedColor(FTMonoaRuntimeEvalError):
    pass


class FTMonoaRuntimeDismatchedEnumType(FTMonoaRuntimeEvalError):
    pass


class FTMonoaRuntimeDismatchedRangeType(FTMonoaRuntimeEvalError):
    pass

class FTMonoNotWhenTimeError(Exception):  # 非when时试图创建错误
    def __init__(self, monoa):
        txts = ["Trying to create a QMonoWidget when it's not a right time. Mono-Attr are:"]
        for k, v in monoa.items():
            txts.append(f"\t{k}: {v}")

        super().__init__("\n".join(txts))


def _default_color(FG_COLOR, FG_ALPHA, BG_COLOR, BG_ALPHA) -> tuple:
    if FG_COLOR is None:
        fg = None
    else:
        fg = QColor(FG_COLOR)
        fg.setAlpha(FG_ALPHA)
    if BG_COLOR is None:
        bg = None
    else:
        bg = QColor(BG_COLOR)
        bg.setAlpha(BG_ALPHA)

    if fg is None and bg is None:
        return None
    return (fg, bg)


class MonoaRuntime:
    BG_ALPHA = 15
    BG_COLOR = "#FFFF00"
    FG_ALPHA = 200
    FG_COLOR = None
    DEFAULTS = {
        "type": None,
        "range": None,
        "nolbl": None,  # label 不显示
        "nobar": None,  # range bar 不显示
        "lines": None,  # str模式下启用多行
        "enum": None,
        "color": _default_color(FG_COLOR, FG_ALPHA, BG_COLOR, BG_ALPHA),
        "tooltip": None,
        "label": None,
        "group": None,
        "header": None,
        "title": None,
        "readonly": False,
        "separator": None,
        "space": None,
        "when": True
    }
    INSPECTOR_KEYS = ('group', 'header', 'title', 'separator', 'space')

    def __init__(self):
        self.monoa_env = {}
        self.monoa_env['Type'] = self.Type
        self.monoa_env['Range'] = self.Range
        self.monoa_env['Nolbl'] = self.NoLbl
        self.monoa_env['Nobar'] = self.NoBar
        self.monoa_env['Lines'] = self.Lines
        self.monoa_env['Enum'] = self.Enum
        self.monoa_env['Color'] = self.Color
        self.monoa_env['Tooltip'] = self.Tooltip
        self.monoa_env['Label'] = self.Label
        self.monoa_env['Group'] = self.Group
        self.monoa_env['Header'] = self.Header
        self.monoa_env['Title'] = self.Title
        self.monoa_env['Readonly'] = self.Readonly
        self.monoa_env['Separate'] = self.Separator
        self.monoa_env['Separator'] = self.Separator
        self.monoa_env['Space'] = self.Space
        self.monoa_env['Spacer'] = self.Space
        self.monoa_env['When'] = self.When
        self.cmonoa = None

        # expand
        self.monoa_env.update(self._lower_keyword_expand(self.monoa_env))
        self.monoa_env.update(self._upper_keyword_expand(self.monoa_env))

    @staticmethod
    def _lower_keyword_expand(_d) -> dict:
        return {k.lower(): v for k, v in _d.items()}

    @staticmethod
    def _upper_keyword_expand(_d) -> dict:
        return {k.upper(): v for k, v in _d.items()}

    @staticmethod
    def _remove_builtins(_d) -> dict:
        return {k: v for k, v in _d.items() if not k.startswith('__')}

    def Type(self, x):
        if isinstance(x, str):
            x = x.lower()
            if x == 'int':
                return {"type": int}
            elif x == 'float':
                return {"type": float}
            elif x == 'str':
                return {"type": str}
            elif x == 'bool':
                return {"type": bool}
            else:
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{x}' is not supported.")
        elif x in (int, float, str, bool):
            return {"type": x}
        raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{x}' is not supported.")

    def Range(self, x, y=None, s=1):
        if y is None:
            _range = rangef(0, x, s)
        else:
            # y must be greater than x
            if y <= x:
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"End of range must be greater than start. but got range({x}, {y})")
            _range = rangef(x, y, s)

        # s must be greater than 0
        if s <= 0:
            raise FTMonoaRuntimeEvalError(self.cmonoa, f"Step of range must be greater than 0. but got step({s})")
        return {"range": _range}

    def Enum(self, *args):
        if not args:
            raise FTMonoaRuntimeEvalError(self.cmonoa, f"Enum must have at least one argument.")
        return {"enum": list(args)}

    def Color(self, fg=None, bg=None):
        fg = fg or self.FG_COLOR
        if fg is not None:
            fg = fg.strip()
            if not fg.startswith('#'):
                raise FTMonoaRuntimeUnexpectedColor(self.cmonoa, f"Foreground color must be in #RRGGBB format. but got fg={fg}")
            fg = QColor(fg)
            fg.setAlpha(self.FG_ALPHA)
        bg = bg or self.BG_COLOR
        if bg is not None:
            bg = bg.strip()
            if not bg.startswith('#'):
                raise FTMonoaRuntimeUnexpectedColor(self.cmonoa, f"Background color must be in #RRGGBB format. but got bg={bg}")
            bg = QColor(bg)
            bg.setAlpha(self.BG_ALPHA)
        return {"color": (fg, bg)}

    def Tooltip(self, x):
        return {"tooltip": x}

    def Label(self, x):
        return {"label": x}

    def NoLbl(self):
        return {"nolbl": True}

    def NoBar(self):
        return {"nobar": True}

    def Lines(self):
        return {"lines": True}

    def Group(self, x="", fg=None):
        if x is not None:
            if not isinstance(x, str):
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"Group name must be str. but got group={x}, type={type(x)}")

        fg = fg or self.FG_COLOR
        if fg is not None:
            fg = fg.strip()
            if not fg.startswith('#'):
                raise FTMonoaRuntimeUnexpectedColor(self.cmonoa, f"Foreground color must be in #RRGGBB format. but got fg={fg}")
            fg = QColor(fg)
            fg.setAlpha(self.FG_ALPHA)

        return {"group": (x, fg)}

    def Header(self, x, fg=None):
        if not isinstance(x, str):
            raise FTMonoaRuntimeEvalError(self.cmonoa, f"Header name must be str. but got header={x}, type={type(x)}")

        fg = fg or self.FG_COLOR
        if fg is not None:
            fg = fg.strip()
            if not fg.startswith('#'):
                raise FTMonoaRuntimeUnexpectedColor(self.cmonoa, f"Foreground color must be in #RRGGBB format. but got fg={fg}")
            fg = QColor(fg)
            fg.setAlpha(self.FG_ALPHA)
        return {"header": (x, fg)}

    def Title(self, x, fg=None):
        _ = self.Header(x, fg)
        v = _['header']
        return {"title": v}

    def Readonly(self):
        return {"readonly": True}

    def Separator(self):
        return {"separator": True}

    def Space(self, x=20):
        if x is not None:
            if not isinstance(x, int):
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"Space height must be int. but got space={x}, type={type(x)}")
        return {"space": x}

    def When(self, x):
        if not isinstance(x, bool):
            try:
                x = bool(x)
            except:
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"'When' condition must be bool. but got when={x}, type={type(x)}. \n\tWhich Can not be transformed to bool.")
        return {"when": x}

    def _check_range_with_type(self, _range, _type):
        """
        * 当描述符与Type(int|float)结合并且S的类型不匹配时，会抛出异常
        * 当描述符与Type(str|bool)结合时，会抛出异常
        """
        if _range is None:
            return True
        start, stop, step = _range.start, _range.stop, _range.step
        start, stop, step = start if start is not None else 0, stop, step if step is not None else 1
        if _type == int:
            if not isinstance(start, int):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.start must be int. but got range.start={start}")
            if not isinstance(stop, int):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.stop must be int. but got range.stop={stop}")
            if not isinstance(step, int):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.step must be int. but got range.step={step}")
        elif _type == float:
            if isinstance(start, int):
                start = float(start)
            elif not isinstance(start, float):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.start must be float. but got range.start={start}")
            if isinstance(stop, int):
                stop = float(stop)
            elif not isinstance(stop, float):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.stop must be float. but got range.stop={stop}")
            if isinstance(step, int):
                step = float(step)
            elif not isinstance(step, float):
                raise FTMonoaRuntimeDismatchedRangeType(self.cmonoa, f"Type of range.step must be float. but got range.step={step}")
        else:
            raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{_type}' is not supported for Range.")
        return True

    def _check_enum_with_type(self, _enum, _type, _value):
        """
        * 当描述符与Type(int|float|str)结合时，提升QXXX为QComboBox
        * 当描述符与Type(bool)结合时，会抛出异常
        """
        if _enum is None:
            return True
        if _type == bool:
            raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{_type}' is not supported for Enum.")
        elif _type == str:
            if _value not in _enum:
                _enum.insert(0, _value)

        # check each one
        for e in _enum:
            if not isinstance(e, _type):
                raise FTMonoaRuntimeDismatchedEnumType(self.cmonoa, f"Type of Enum must be {_type}. but got Enum={_enum}")

        return True

    def __call__(self, monoa: MonoAttr, monoe: dict) -> tuple[dict, list]:
        """
        解析一个MonoAttr对象，返回一个dict对象，包含了关键单元属性信息; 以及一个list对象，包含了所有的检视信息。
        list对象的每一个元素都是一个tuple对象，包含了检视信息的key和检视信息的内容。
        """
        monoa.iterall(_api_prehandle_single_attr)
        lst, res, self.cmonoa = [], {}, monoa
        env = monoe.copy()
        for expression in monoa:
            try:
                _ = eval(expression, self.monoa_env, env)
            except Exception as e:
                envl = self._remove_builtins(env)
                envg = self._remove_builtins(self.monoa_env)
                raise FTMonoaRuntimeEvalError(self.cmonoa,
                                              f"Error while evaluating expression: {expression} - {e}\n\n\tcurrent globals: {str_crop(envg)}\n\tcurrent locals: {str_crop(envl)}")

            # save into res
            if not isinstance(_, dict):
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"Expression '{expression}' must return a dict object.")
            k = list(_)[0]
            if k in self.INSPECTOR_KEYS:
                lst.append((k, _[k]))
            else:
                res.update(_)

        # add name and value
        res['name'] = monoa.name
        res['value'] = monoa.value

        if res['name'] == 'cmp0':
            a = 0  # debug

        # fill default values
        for k, v in self.DEFAULTS.items():
            if k not in res:
                res[k] = v

        # check type
        if res['type'] is None and monoa.value is None:
            res['type'] = str
            monoa.value = ""
        else:
            is_monoa_value_valid = isinstance(monoa.value, (int, float, str, bool))
            if not is_monoa_value_valid:
                raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{type(monoa.value)}' of value '{monoa.value}' is not supported.")
            if res['type'] is None:
                res['type'] = type(monoa.value)
            if res['type'] != type(monoa.value):
                try:
                    monoa.value = res['type'](monoa.value)
                except Exception as e:
                    raise FTMonoaRuntimeEvalError(self.cmonoa, f"Type '{res['type']}' is not supported.")
        # cross check
        self._check_range_with_type(res['range'], res['type'])
        self._check_enum_with_type(res['enum'], res['type'], monoa.value)

        return res, lst


def _api_prehandle_single_attr(attr: str):
    """
    每一条attr都应当为一条python函数执行语句，所以第一步是补全()
    """
    attr = attr.strip()
    # re check
    if attr.endswith(')'):
        return attr
    return attr + '()'


def _api_diagnose_attr_type(obj, monoa: MonoAttr):
    param, value = monoa.name, monoa.value

    for attr in monoa:
        attr = attr.lower()


MONO_FONT = QFont('Consolas', 12, QFont.Bold)
MONO_HEADER_FONT = QFont('Consolas', 13, QFont.Bold)
MONO_TITLE_FONT = QFont('Consolas', 14, QFont.Bold)
MONO_INSPECTOR_FONT = QFont('Consolas', 16, QFont.Bold)


class QMonoWithoutBorder:
    ...


class QMonoRectBorder(QMonoWithoutBorder):
    ...


class QMonoRoundRectBorder(QMonoWithoutBorder):
    ...


class QMonoWidget(QWidget):
    paramChanged = pyqtSignal(str, object)

    def __init__(self, attr_dict: dict, parent=None, *, border=QMonoWithoutBorder):
        super().__init__(parent)
        self.ad = attr_dict  # attr_dict
        self._name = self.ad['name']
        self._value = self.ad['value']
        self._last_emit_value = self._value
        self._rootL = QVBoxLayout()
        self._rootL.setContentsMargins(4, 4, 6, 6)
        self._rootL.setSpacing(4)
        self._mainL = QHBoxLayout()
        self._mainL.setContentsMargins(2, 2, 4, 4)
        self._mainL.setSpacing(2)
        self.setLayout(self._rootL)
        self._rootL.addLayout(self._mainL)
        self._border = border
        assert issubclass(self._border, QMonoWithoutBorder), f"Border must be subclass of QMonoWithoutBorder."

        # ---
        self._uis = []
        self._int_float_vc_flag = False
        self._bool_vc_flag = False
        self._str_vc_flag = False

        self.initUI()

        # --- set default value
        self._set_default_value()

    def initUI(self):
        self._create_ui()
        if not self.ad['when']:
            self.setVisible(False)


    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._set_default_value(value=v)

    @property
    def whenable(self):
        return self.ad['when']

    @property
    def readonly(self):
        return self.ad['readonly']

    def _set_default_value(self, *_, value=None):
        # value = value or self.ad['value']
        if value is None:
            value = self.ad['value']
        if self.ad['type'] in (float, int):
            self._int_float_value_changed(value)
        elif self.ad['type'] == bool:
            self._bool_value_changed(value)
        elif self.ad['type'] == str:
            self._str_value_changed(value)
        else:
            raise FTQMonoWidgetRecvObjectError(f"Type of object is not supported in single QMonoWidget.")

    def _select_main_widget(self):
        if self.ad['type'] == int:
            return QSpinBox
        elif self.ad['type'] == float:
            return QDoubleSpinBox
        elif self.ad['type'] == str:
            return QLineEdit if not self.ad['lines'] else QTextEdit
        elif self.ad['type'] == bool:
            return QCheckBox
        elif self.ad['type'] == object:
            raise FTQMonoWidgetRecvObjectError(f"Type of object is not supported in single QMonoWidget.")
        else:
            raise TypeError(f"Type '{self.ad['type']}' is not supported.")

    def _create_ui(self):
        self._lbl = QLabel((self.ad['label'] if self.ad['label'] else self.ad['name']))
        self._lbl.setFont(MONO_FONT)
        self._mainL.addWidget(self._lbl)

        self._mwd = self._select_main_widget()()
        self._mwd.setFont(MONO_FONT)
        self._mainL.addWidget(self._mwd)

        self._btn = QPushButton("O")
        self._btn.setFont(QFont('Arial', 10))
        self._btn.setFixedSize(22, 22)
        self._btn.clicked.connect(self._set_default_value)
        self._mainL.addWidget(self._btn)

        # no label
        if self.ad['nolbl']:
            self._lbl.hide()
            self._lbl.setText("")
            self._lbl.setFixedSize(0, 0)

        # change input-limit
        if isinstance(self._mwd, (QSpinBox, QDoubleSpinBox)):
            self._mwd.setRange(-2147483648, 2147483647)
            self._mwd.setSingleStep(1 if self.ad['type'] == int else 0.01)

        # check range
        if self.ad['range'] and not self.ad['enum']:  # python range
            assert isinstance(self._mwd, (QSpinBox, QDoubleSpinBox)), f"Range is not supported for type '{self.ad['type']}'"
            start, stop, step = self.ad['range'].start, self.ad['range'].stop, self.ad['range'].step
            start, stop, step = start if start is not None else 0, stop, step if step is not None else 1
            self._mwd.setRange(start, stop)
            self._mwd.setSingleStep(step)

            if not self.ad['nobar']:
                self._qsl = QIntSlider(Qt.Horizontal, start, stop, step) if self.ad['type'] == int else QDoubleSlider(Qt.Horizontal, start, stop, step)
                self._qsl.monoChanged.connect(self._int_float_value_changed)
                self._uis.append(self._qsl)
                self._rootL.addWidget(self._qsl)
            else:
                self._qsl = None
        else:
            self._qsl = None

        # check enum
        if self.ad['enum']:
            assert isinstance(self._mwd, (QSpinBox, QDoubleSpinBox, QLineEdit)), f"Enum is not supported for type '{self.ad['type']}'"
            self._mcb = QComboBox()
            self._mcb.setFont(MONO_FONT)
            self._mcb.addItems([str(it) for it in self.ad['enum']])
            self._mcb.currentIndexChanged.connect(self._combo_value_changed)
            self._uis.append(self._mcb)
            self._rootL.addWidget(self._mcb)

            # as readonly
            self._mwd.setReadOnly(True)
        else:
            self._mcb = None

        # posthandle
        self._uis.append(self._lbl)
        self._uis.append(self._mwd)
        self._uis.append(self._btn)

        # transparent
        for ui in self._uis:
            ui.setAttribute(Qt.WA_TranslucentBackground)

        # re label
        if self.ad['label']:
            self._lbl.setText(self.ad['label'])

        # readonly
        if self.ad['readonly']:
            for ui in self._uis:
                # if hasattr(ui, 'setReadOnly'):
                #     ui.setReadOnly(True)
                # else:
                ui.setEnabled(False)

        # tooltips
        if self.ad['tooltip']:
            for ui in self._uis:
                ui.setToolTip(self.ad['tooltip'])

        # color
        if self.ad['color']:  # fg, bg
            fg, bg = self.ad['color']
            readonly = self.ad['readonly']
            if fg is not None:
                fg = QColor(fg.red(), fg.green(), fg.blue(), fg.alpha() if not readonly else int(fg.alpha() * 0.7))
            for ui in self._uis:
                txt = ""
                if fg is not None:
                    txt += f"color:rgba({fg.red()}, {fg.green()}, {fg.blue()}, {fg.alpha()});"
                if not isinstance(ui, (QLineEdit, QSpinBox, QDoubleSpinBox, QPushButton, QComboBox)):
                    # Bg can only be set to other widgets
                    if bg is not None:
                        txt += f"{ui.__class__.__name__}" + "{" + f"background-color:rgba({bg.red()}, {bg.green()}, {bg.blue()}, {bg.alpha()}); + " + "}"
                        txt += f"{ui.__class__.__name__}:focus" + "{" + f"background-color:rgba({bg.red()}, {bg.green()}, {bg.blue()}, {bg.alpha()}); + " + "}"
                if txt:
                    ui.setStyleSheet(txt)

        if isinstance(self._mwd, (QSpinBox, QDoubleSpinBox)):
            self._mwd.valueChanged.connect(self._int_float_value_changed)
        elif isinstance(self._mwd, QCheckBox):
            self._mwd.setText("")
            self._mwd.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px; };" + self._mwd.styleSheet())
            self._mwd.setMaximumSize(20, 20)
            self._mwd.stateChanged.connect(self._bool_value_changed)
        elif isinstance(self._mwd, QLineEdit):
            self._mwd.textChanged.connect(self._str_value_changed)
        elif isinstance(self._mwd, QTextEdit):
            self._mwd.lostFocus.connect(self._str_value_changed_texteidt)

    def _int_float_value_changed(self, value, *args):
        if self._int_float_vc_flag: return
        self._int_float_vc_flag = True

        if self._mcb:  # check this first
            if value in self.ad['enum']:
                self._mcb.setCurrentIndex(self.ad['enum'].index(value))
            else:
                idx, value = find_closest(value, self.ad['enum'])
                self._mcb.setCurrentIndex(idx)

        self._mwd.setValue(value)
        if self._qsl:
            self._qsl.setValue(value)

        self._value = value
        self._int_float_vc_flag = False
        self._param_value_changed()

    def _bool_value_changed(self, value):
        if self._bool_vc_flag: return
        self._bool_vc_flag = True

        self._mwd.setChecked(value)
        self._value = bool(value)

        self._bool_vc_flag = False
        self._param_value_changed()

    def _str_value_changed_texteidt(self):
        self._str_value_changed(self._mwd.toPlainText())

    def _str_value_changed(self, value):
        if self._str_vc_flag: return
        self._str_vc_flag = True

        self._mwd.setText(value)
        self._value = value

        self._str_vc_flag = False
        self._param_value_changed()

    def _param_value_changed(self):
        if self._last_emit_value == self._value:
            return
        self._last_emit_value = self._value
        self.paramChanged.emit(self._name, self._value)

    def _combo_value_changed(self, index):
        value = self.ad['enum'][index]
        if isinstance(self._mwd, (QSpinBox, QDoubleSpinBox)):
            self._int_float_value_changed(value)
        elif isinstance(self._mwd, QLineEdit):
            self._str_value_changed(value)
        else:
            raise TypeError(f"Type '{self.ad['type']}' is not supported with checkbox.")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 获取窗口的大小
        rect = self.rect()
        rect.adjust(0, 0, -4, -4)

        # # 绘制底色
        # base_color = QColor("#888888")
        # base_color.setAlpha(200)
        # painter.setPen(QPen(base_color, 1, Qt.SolidLine))
        # painter.setBrush(Qt.NoBrush)
        # painter.translate(1, 1)  # 偏移
        # painter.drawRoundedRect(rect, 4, 4)
        # base_color.setAlpha(100)
        # painter.translate(1, 1)  # 偏移
        # painter.drawRoundedRect(rect, 4, 4)
        # painter.translate(-2, -2)  # 恢复原位置

        # 设置阴影的颜色和透明度
        shadow_color = QColor("#848080")
        shadow_color.setAlpha(50)
        shadow_fill_color = QColor("#FFFF00") if (self.ad['color'] is None or self.ad['color'][1] is None) else self.ad['color'][1]
        if self.readonly:
            r, g, b = shadow_fill_color.red(), shadow_fill_color.green(), shadow_fill_color.blue()
            average = (r + g + b) // 3
            shadow_fill_color = QColor(int(r * 0.5 + average * 0.5), int(g * 0.5 + average * 0.5), int(b * 0.5 + average * 0.5), shadow_fill_color.alpha())
        shadow_fill_color.setAlpha(25)
        # 融合颜色

        # 绘制底色
        painter.translate(3, 3)
        painter.setPen(QPen(shadow_color, 1, Qt.SolidLine))
        painter.setBrush(QBrush(shadow_fill_color))
        painter.drawRoundedRect(rect, 4, 4)
        painter.translate(-3, -3)  # 恢复原位置

        # 绘制圆角矩形边框
        border_color = QColor("#000000")
        border_color.setAlpha(150)
        painter.setPen(QPen(border_color, 1, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(rect, 4, 4)
        painter.translate(1, 1)
        border_color.setAlpha(100)
        painter.setPen(QPen(border_color, 1, Qt.SolidLine))
        painter.drawRoundedRect(rect, 4, 4)
        painter.translate(1, 1)
        border_color.setAlpha(50)
        painter.setPen(QPen(border_color, 1, Qt.SolidLine))
        painter.drawRoundedRect(rect, 4, 4)
        painter.translate(-2, -2)

        # 在这里添加其他绘制逻辑
        # ...

        # 调用基类的 paintEvent 以进行正常的绘制
        super().paintEvent(event)


class QMonoSeparator(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)


class QMonoSpacer(QWidget):
    def __init__(self, height: int = 20, parent=None):
        super().__init__(parent)
        self.setFixedHeight(height)


GROUP_INDENT = 32
INSPECTOR_SPACE = 2


class QMonoGroup(QWidget):
    def __init__(self, title: str, color: QColor, parent=None):
        super().__init__(parent)
        icon_color = QColor(color.red() // 4, color.green() // 4, color.blue() // 4, color.alpha())
        self.RIGHT_TRIANGLE = api_create_triangle_pixel(16, icon_color, direct="right")
        self.DOWN_TRIANGLE = api_create_triangle_pixel(16, icon_color, direct="down")
        self._color = color
        if not title.endswith(":"):
            title += ":"
        self._title = title
        self._title_hide = title[:-1]
        self._rootL = QVBoxLayout()
        self._rootL.setContentsMargins(0, 0, 0, 0)
        self._rootL.setSpacing(0)
        self._is_visible = True  # 用于跟踪组件是否可见
        self._title_layout = self._build_title()
        self._setup_header()

        self._mainL = QVBoxLayout()
        self._mainL.setContentsMargins(GROUP_INDENT, 0, 0, 0)
        self._mainL.setSpacing(INSPECTOR_SPACE)

        self._rootL.addLayout(self._mainL)
        self._done_first_paint_flag = False

        self._lst_svisible = False

        self.setLayout(self._rootL)

    def any_whenables(self):
        _any_whenable = False
        for i in range(self._mainL.count()):
            item = self._mainL.itemAt(i)
            if not item: continue
            widget = item.widget()
            if not widget: continue
            if not hasattr(widget, 'whenable'): continue
            _any_whenable = _any_whenable or widget.whenable
            if _any_whenable:
                break
        return _any_whenable

    @property
    def title(self):
        return self._title

    def _build_title(self):
        _l = QHBoxLayout()
        w = QLabel(self._title)
        w.setFont(MONO_HEADER_FONT)
        w.setStyleSheet(f"color:rgba({self._color.red()}, {self._color.green()}, {self._color.blue()}, {self._color.alpha()});")
        self._label_widget = w
        _l.addWidget(w)
        # add a space
        _l.addStretch()
        return _l

    def _setup_header(self):
        self.toggle_button = QPushButton()
        self.toggle_button.setFixedSize(20, 20)  # 设置按钮大小
        self.toggle_button.setStyleSheet("border: none;")  # 移除按钮边框
        self.toggle_button.clicked.connect(self.toggle_visibility)  # 绑定点击事件

        # 设置按钮的初始方向
        self.toggle_button.setIcon(QIcon(self.DOWN_TRIANGLE))
        self.toggle_button.setIconSize(self.toggle_button.size())

        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.toggle_button)
        self.title_layout.addLayout(self._title_layout)
        self.title_layout.addStretch()

        # 标题布局
        self._rootL.addLayout(self.title_layout)

    def toggle_visibility(self):
        self.setSubVisible(not self._is_visible)

    def setSubVisible(self, visible:bool=None):
        if visible is None:
            visible = self._is_visible
        self._is_visible = visible
        if visible:
            self.toggle_button.setIcon(QIcon(self.DOWN_TRIANGLE))
            # self._rootL.addLayout(self._mainL)
            api_show_layout_widgets(self._mainL)
            self._label_widget.setText(self._title)
        else:
            self.toggle_button.setIcon(QIcon(self.RIGHT_TRIANGLE))
            # self._rootL.removeItem(self._mainL)
            api_hide_layout_widgets(self._mainL)
            self._label_widget.setText(self._title_hide)

    @property
    def main_layout(self):
        return self._mainL

    def firstStart(self):
        self.setSubVisible(False)

    def paintEvent(self, a0):
        if not self._done_first_paint_flag:
            self.firstStart()
            self._done_first_paint_flag = True
        super().paintEvent(a0)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self._is_visible:
            # draw indent line, start at (GROUP_INDENT - 2, self._label_widget.height() + 2)
            _color = QColor(self._color.red(), self._color.green(), self._color.blue(), self._color.alpha() // 2)
            painter.setPen(QPen(_color, 1, Qt.DashLine))
            painter.drawLine(10, self._label_widget.height() + 2, 10, self.height() - 2)
        else:
            # draw after label
            shd_width, pdelta = 48, 12
            geo = self._label_widget.geometry()
            _color = QColor(self._color.red(), self._color.green(), self._color.blue(), self._color.alpha() // 8)
            painter.setPen(Qt.NoPen)
            painter.setBrush(_color)
            shd_rect = QRect(geo.right() + 8, geo.top() + 2, shd_width, geo.height() - 4)
            painter.drawRoundedRect(shd_rect, 2, 2)
            # draw point x3
            _color.setAlpha(_color.alpha() * 4)
            painter.setBrush(_color)
            for i in range(3):
                painter.drawEllipse(QPoint(shd_rect.left() + pdelta * (i + 1), shd_rect.center().y() + 2), 3, 3)


QMONO_INSPECTOR_TITLE_COLOR = QColor(32, 144, 245, 225)


class _QMonoInspector_Area(QWidget):
    rebuildTriggered = pyqtSignal(Mono)

    def __init__(self, mono_target: Mono, parent=None):
        super().__init__(parent)
        self._raw = mono_target.monos
        self.mra = MonoaRuntime()
        self._monos = []
        self._ispts = []
        for m in self._raw:
            mono, ispt = self.mra(m, mono_target.env)
            self._monos.append(mono)
            self._ispts.append(ispt)

        self._mono_widgets = []
        self._group_widgets = {}  # 这是一个按照path来存储group的dict对象 # list[QMonoGroup, dict]  # 树结构
        self._current_group: QWidget = None  # 当前的group
        self._rootL = QVBoxLayout()
        self._rootL.setContentsMargins(2, 2, 0, 2)
        self._rootL.setSpacing(INSPECTOR_SPACE)
        self.setLayout(self._rootL)
        self._create_ui()

        self.rebuildTriggered.connect(self.rebuild)
        self._on_rebuild_flag = False

    @property
    def rebuild_flag(self):
        return self._on_rebuild_flag

    def rebuild(self, mono_target: Mono):
        self._on_rebuild_flag = True
        self._raw = mono_target.monos
        self._monos = []
        self._ispts = []
        for m in self._raw:
            mono, ispt = self.mra(m, mono_target.env)
            self._monos.append(mono)
            self._ispts.append(ispt)

        params_dict = {}
        for mono in self._monos:
            params_dict[mono['name']] = {
                'value':mono['value'],
                'when':mono['when'],
            }

        for qmono in self._mono_widgets:
            _new = params_dict.get(qmono.name, {
                'value':qmono.value,
                'when':qmono.ad['when'],
            })
            qmono.setVisible(_new['when'])
            qmono.ad['when'] = _new['when']
            if qmono.readonly:
                qmono.value = _new['value']

        self._hide_empty_group()
        self._on_rebuild_flag = False

    @staticmethod
    def _parse_group_path(group_path: str) -> list:
        pat = "[/\\.]"
        return [it.strip() for it in re.split(pat, group_path) if it.strip()]

    def _locate_group(self, group_path: str, color: QColor = None) -> QMonoGroup:
        """
        根据group_path来定位group对象，如果group_path为空，则返回None
        """
        plst = self._parse_group_path(group_path)
        if not plst:
            self._current_group = None
            return None

        # path不为空，因此current必然不为self._group_widgets
        current = self._group_widgets
        self._current_group = None
        for p in plst:
            if p not in current:
                self._set_group(p, color)
                current[p] = [self._current_group, {}]

            self._current_group = current[p][0]
            current = current[p][1]

        return self._current_group

    @property
    def monos(self):
        return self._monos

    def _add_header(self, title: str = "", color: QColor = None, *, font=MONO_HEADER_FONT, _sys_widget_type=QLabel, _sys_widget_args=()):
        _l = QHBoxLayout()
        # add a space
        w = QMonoSeparator(self)
        _l.addWidget(w)

        # add a title
        if not title.endswith(":"):
            title += ":"
        w = _sys_widget_type(title, *_sys_widget_args)
        w.setFont(font)
        if color is not None and isinstance(w, QLabel):
            w.setStyleSheet(f"color:rgba({color.red()}, {color.green()}, {color.blue()}, {color.alpha()});")
        _l.addWidget(w)

        # add a space
        w = QMonoSeparator(self)
        _l.addWidget(w)

        # add into
        self._add_layout_into(_l)

    def _add_title(self, title: str = "", color: QColor = None):
        if color is None:
            color = QColor(0, 0, 0, MonoaRuntime.FG_ALPHA)
        return self._add_header(title, color, font=MONO_TITLE_FONT, _sys_widget_type=QShadowLabel, _sys_widget_args=(color, None, 2))

    def _add_separator(self):
        w = QMonoSeparator(self)
        self._add_widget_into(w)

    def _add_space(self, height: int = 20):
        w = QMonoSpacer(height)
        self._add_widget_into(w)

    def _set_group(self, title: str, color: QColor = None):
        if color is None:
            color = QColor(0, 0, 0, MonoaRuntime.FG_ALPHA)
        if not title.endswith(":"):
            title += ":"
        w = QMonoGroup(title, color)
        self._add_widget_into(w)
        self._current_group = w

    def _hide_empty_group(self, target:dict=None):
        if target is None:
            target = self._group_widgets

        _removes = []
        for k, v in target.items():
            if isinstance(v, list):
                grp:QMonoGroup = v[0]
                if not grp.any_whenables():
                    grp.setVisible(False)
                    # self._rootL.removeWidget(grp)
                    # grp.deleteLater()
                    # _removes.append(k)
                else:  # 恢复显示
                    grp.setVisible(True)
                    grp.setSubVisible()  # 恢复上次的状态
                    self._hide_empty_group(v[1])

        # for k in _removes:
        #     target.pop(k)



    def _create_inspects(self, isp: list):
        for idx, (k, v) in enumerate(isp):
            if k == 'group' and v is not None:
                if self._current_group is None or self._current_group.title != str(v[0]):
                    self._locate_group(str(v[0]), v[1])
            elif k == 'header' and v is not None:
                self._add_header(*v)  # title, color
            elif k == 'title' and v is not None:
                self._add_title(*v)  # title, color
            elif k == 'space' and v is not None:
                self._add_space(v)
            elif k == 'separator' and v is True:
                self._add_separator()

    def _create_ui(self):
        for i, (m, isp) in enumerate(zip(self._monos, self._ispts)):
            self._create_inspects(isp)
            # if not m['when']:
            #     continue
            w = QMonoWidget(m)
            self._mono_widgets.append(w)
            self._add_widget_into(w)

        # add a stretch
        self._rootL.addStretch()

        # remove empty group
        self._hide_empty_group()  # TODO: 修复这个问题

    def _add_widget_into(self, w):
        if self._current_group is None:
            self._rootL.addWidget(w)
        else:
            self._current_group.main_layout.addWidget(w)

    def _add_layout_into(self, l):
        if self._current_group is None:
            self._rootL.addLayout(l)
        else:
            self._current_group.main_layout.addLayout(l)

    @property
    def params(self):
        res = {}
        for w in self._mono_widgets:
            res[w.name] = w.value
        return res


class QMonoInspector(QWidget):
    paramsChanged = pyqtSignal(dict)
    paramChanged = pyqtSignal(str, object)

    # 内部有且只有一个QMonoInspector_Area被一个QScrollArea包裹，只提供一个竖直滚动条
    def __init__(self, mono: Mono, parent=None):
        super().__init__(parent)
        self._mono = mono
        self._inner = _QMonoInspector_Area(mono)
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._scroll.setFrameShape(QFrame.NoFrame)
        self._scroll.setWidget(self._inner)
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._add_mono_title("Mono Inspector:")
        self._layout.addWidget(self._scroll)
        self.setLayout(self._layout)

        # connect
        for w in self._inner._mono_widgets:
            w.paramChanged.connect(self._any_param_changed)

    def _any_params_changed(self, name: str, value: object):
        if self._inner.rebuild_flag:
            return
        self.paramsChanged.emit(self.params)

    def _any_param_changed(self, name: str, value: object):
        if self._inner.rebuild_flag:
            return
        self.paramChanged.emit(name, value)
        self._any_params_changed(name, value)

    def _add_mono_title(self, title: str = "Mono Inspector:"):
        _l = QHBoxLayout()
        w = QShadowLabel(title, QMONO_INSPECTOR_TITLE_COLOR, None, 2)
        w.setFont(MONO_INSPECTOR_FONT)
        _l.addWidget(w)
        # add a space
        _l.addStretch()
        self._layout.addLayout(_l)

    def rebuildmono(self, s, **params):
        self._mono.handle(s, **params)
        self._inner.rebuild(self._mono.monos)

    @property
    def rebuildTrigger(self):
        return self._inner.rebuildTriggered

    @property
    def monos(self):
        return self._inner.monos

    @property
    def params(self):
        return self._inner.params

    @property
    def qmonos(self):
        return self._inner._mono_widgets.copy()

    def closeEvent(self, a0):
        print("Inspector closed. Params:\n\t", self.params)
        self.close()


class QMonoLogo(QWidget):
    """
    一个简单的Logo控件，用于显示Logo
    """

    def __init__(self, logo_str: str = "Mono Inspector", parent=None, align=Qt.AlignCenter):
        super().__init__(parent)
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self.setLayout(self._layout)
        self._add_mono_title(logo_str, align)

    def _add_mono_title(self, title: str = "Mono Inspector:", align=Qt.AlignCenter):
        _l = QHBoxLayout()
        if align == Qt.AlignLeft:
            _l.addStretch()
        w = QShadowLabel(title, QMONO_INSPECTOR_TITLE_COLOR, None, 2)
        w.setFont(MONO_INSPECTOR_FONT)
        _l.addWidget(w)
        if align == Qt.AlignRight:
            _l.addStretch()
        self._layout.addLayout(_l)


def _TestSingleUI(monoa: MonoAttr, monoe: dict):
    mar = MonoaRuntime()
    attr_dict = mar(monoa, monoe)
    print("Parsed :\t")
    for k, v in attr_dict.items():
        print(f"\t{k}:\t{v}")
    app = QApplication(sys.argv)
    w = QMonoWidget(attr_dict)
    w.setWindowTitle("Test")
    w.show()
    sys.exit(app.exec_())


def _TestInspector(mono: Mono):
    app = QApplication(sys.argv)
    w = QMonoInspector(mono)
    w.setWindowTitle("Test")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    mono = Mono(
        "//\s*>", "\n",
        "\$", "\$",
        "/*\s*>", "\*/",
        "//\s*\[", "\]",
        "//\s*\?", '//\s*:\?', "//\s*:", "//\s*\$",
        COMMENT=r";#", CSO=r"/*\s*#", CEO=r"\*/",
        ENV=r"import math"
    )

    with open('counter.v5.v', 'r', encoding="utf-8") as f:
        test = f.read()

    with open('saved.v', 'w', encoding="utf-8") as f:
        f.write(mono.handle(test, WIDTH=10, add_en=True))

    # test1
    # monos = mono.monos
    # if len(monos) > 0:
    #     one = monos[0]
    #     print(f"mono-attr:\t{one}")
    #     _TestSingleUI(one, mono.env)

    # test2
    _TestInspector(mono)
