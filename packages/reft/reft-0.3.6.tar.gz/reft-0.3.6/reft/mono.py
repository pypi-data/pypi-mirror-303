import ast
import warnings

from reft.ft import *
try:
    from PyQt5.QtWidgets import QWidget
    from mono_ui import QMonoWidget
except ImportError:
    pass

__doc__ = """
mono.py - based on reft
用来处理一种类似unity mono的attributes的标注语言嵌入
*允许嵌入到任何代码中，用于控制目标代码的最终内容
*可以支持python eval exec、if branch等
*使用Attributes修饰Variable，可以提供创建Inspector的PyQt5 Widget的API

ESO eval EEO

VSO express VEO

XSO
ASO attribute1|attribute2... AEO 
exec 
XEO

IFSO eval
...
EFSO eval
...
ELSO
...
IFEO

* 不支持LOOP
"""

_DEBUG_MODE = False

class FTMonoAttrNotValidWarning(UserWarning):
    pass

class FTMonoInfiniteExecLoop(Exception):
    pass


class FTMonoAttrToMultiExecs(Exception):
    pass

class FTMonoEvalError(Exception):
    def __init__(self, raw:FTMatched, env:dict):
        txt = f" Failed to eval: '{raw}' at lineno {raw.lineno} with environ:\n\t{env}"
        super().__init__(txt)

class MonoAttr:
    def __init__(self, name, value, *attrs, lineno=None):
        self._name = name
        self._value = value
        self._attrs = attrs
        self._lineno = lineno
        self._readonly = False
        for a in attrs:
            if 'readonly' in a.lower():
                self._readonly = True
                break

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def readonly(self) -> bool:
        return self._readonly

    @property
    def attrs(self):
        return self._attrs

    @property
    def lineno(self):
        return self._lineno if self._lineno is not None else -1

    def iterall(self, func):
        """
        遍历更新所有的属性
        """
        _news = []
        for i, attr in enumerate(self._attrs):
            try:
                _news.append(func(attr))
            except Exception as e:
                raise ValueError(f"MonoAttr.iterall:Failed to update attr {attr} with error: {e}")
        self._attrs = tuple(_news)

    def __str__(self):
        return f"({self._name}={self._value})[{'|'.join(self._attrs)}]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self._name == other._name

    def __hash__(self):
        return hash(self._name)

    def __getitem__(self, item):
        return self._attrs[item]

    def __iter__(self):
        return iter(self._attrs)





def api_parse_python_single_line_vardef(s: str, env: dict = None) -> tuple[str, any] | str | None:
    """
    解析python单行变量定义
    * 1. 只支持单行
    * 2. 只支持变量定义(包括赋值)
    * 3. 使用提供的env字典来计算变量值
    * 4. 返回变量名和变量值(如果有)

    * env传入None时，不会计算变量值，只返回变量名
    """
    try:
        # 解析字符串为AST
        tree = ast.parse(s, mode='exec')
    except SyntaxError:
        # 如果解析失败，返回None
        return None

    # 遍历AST节点
    for node in ast.walk(tree):
        # 检查是否是赋值语句
        if isinstance(node, ast.Assign):
            # 检查是否只有一个目标（即一个变量）
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                var_name = node.targets[0].id
                if env is None:
                    return var_name
                # 将AST节点转换为可执行代码
                code = compile(ast.Expression(node.value), filename="<ast>", mode="eval")
                # 使用env字典计算变量值
                var_value = eval(code, env)
                return var_name, var_value
    return None


def api_ftmono_handle_execs(execs: list[FTMatched], env: dict, overide_dict:dict, depth=FT_DEPTH) -> dict:
    """
    处理execs
    * 1. 轮流处理execs, 记录结果没有报错的index
    * 2. 如果某轮处理全部报错，那么停止处理
    """
    _passed = []  # 记录总的通过的index
    _aimnum = len(execs)  # 目标处理次数
    _left = depth  # 剩余的处理次数

    # empty check
    if not _aimnum: return {}

    # loop
    while _left > 0:
        _left -= 1
        _epoch_passed = []      # 记录本轮通过的index
        _epoch_errors = []      # 记录本轮错误的内容
        _error_contents = []    # 记录本轮错误的exec的内容
        for i, s in enumerate(execs):
            ftm: FTMatched = s
            lineno, content = ftm.lineno, str(ftm)
            if i in _passed: continue  # skip passed items
            try:
                exec(content, env)
                _epoch_passed.append(i)
                env.update(overide_dict)
            except Exception as e:
                _epoch_errors.append((i, e))
                _error_contents.append(content)
        if not _epoch_passed:
            _lefts = [f"lineno:{lineno}" for i in range(len(execs)) if i not in _passed]
            _erros = "\n\t\t\t".join([str(i) + ": " + str(e) for i, e in _epoch_errors])
            _envs = {k: v for k, v in env.items() if not k.startswith("__")}
            _cots = "\n\t\t\t".join([f"{i}: {c}" for i, c in enumerate(_error_contents)])
            raise FTMonoInfiniteExecLoop("Infinite Exec Loop Detected" +
                                         f"\n\tenvironments: \n\t\t{_envs}" +
                                         f"\n\tlefts: \n\t\t{_lefts}" +
                                         f"\n\terrors: \n\t\t{_erros}" +
                                         f"\n\tcontents: \n\t\t{_cots}")
        _passed.extend(_epoch_passed)
        if len(_passed) == _aimnum:
            break
    return env



class Mono:
    @staticmethod
    def _api_count_newline(*strs):
        _ = 0
        for s in strs:
            _ += str(s).count('\n')
        return _

    def __init__(self, ESO, EEO, VSO, VEO,
                 XSO=None, XEO=None, ASO=None, AEO=None,
                 *, COMMENT=';', CSO="/\*", CEO="\*/", ENV: str = None):
        """
        '
        ESO exec EEO  ; 该语句必须在一行内

        VSO express VEO  ; 嵌入表达式结果到目标

        '
        XSO
        exec
        XEO

        '
        ASO attribute AEO  ; 只能用在eval语句前，并且只作用于渲染eval中定义的变量
        ESO eval EEO

        '   ; 根据表达式控制目标代码的分支
        IFSO eval
        ...
        EFSO eval
        ...
        ELSO ;else
        ...
        IFEO

        * ES?可以和XS?一致。程序会根据包含内容是否有多行自动推断
        * 如果不指定XSO XEO，那么会默认和ESO EEO一致
        * 如果不指定ASO AEO，那么会忽略attribute
        * 如果不指定IFSO EFSO ELSO IFEO，那么会忽略if else
        * 如果不指定LPSO LPBK LPCT LPEO，那么会忽略loop

        * 默认使用;作为注释符号，可以通过comment参数修改
        * 默认使用/\* \*/作为注释符号，可以通过CSO CEO参数修改

        * env: 用于在构造eval和exec用的虚拟环境时执行的代码。一般可以指定为几条import语句
        """
        self._ESO = ESO
        self._EEO = EEO
        self._VSO = VSO
        self._VEO = VEO
        self._XSO = XSO or ESO
        self._XEO = XEO or EEO
        self._ASO = ASO or None
        self._AEO = AEO or None
        self._COMMENT = COMMENT
        self._CSO = CSO
        self._CEO = CEO
        self._ENV = ENV
        assert isinstance(ESO, str), f"Mono's Exec-Line Start Operator must be a string, but got {ESO}"
        assert isinstance(EEO, str), f"Mono's Exec-Line End Operator must be a string, but got {EEO}"
        assert isinstance(VSO, str), f"Mono's eval-Value Start Operator must be a string, but got {VSO}"
        assert isinstance(VEO, str), f"Mono's eval-Value End Operator must be a string, but got {VEO}"
        assert isinstance(XSO or ESO, str), f"Mono's Exec-MultipleLines Start Operator must be a string, but got {XSO}"
        assert isinstance(XEO or EEO, str), f"Mono's Exec-MultipleLines End Operator must be a string, but got {XEO}"
        assert ASO is None or isinstance(ASO, str), f"Mono's Attribute Start Operator must be a string, but got {ASO}"
        assert AEO is None or isinstance(AEO, str), f"Mono's Attribute End Operator must be a string, but got {AEO}"
        assert isinstance(COMMENT, str), f"Mono's Comment Operator must be a string, but got {COMMENT}"
        assert isinstance(CSO, str), f"Mono's Comment Start Operator must be a string, but got {CSO}"
        assert isinstance(CEO, str), f"Mono's Comment End Operator must be a string, but got {CEO}"
        assert isinstance(ENV, str), f"Mono's Env must be a string, but got {ENV}"

        # ------------------------------
        self._dgs = self._build_gs()
        self._ft = self._build_ft()
        self._sft = self._build_sft()
        self._env = self._build_env()
        self._overenv = {}  # 用于指定覆盖内容的env
        self._execs = []  # 用于存储运行时exec-multilines  # list[FTMatched]
        self._exevs = []  # 用于存储运行时exec-line的内容  # list[FTMatched]
        self._attrs = []  # 用于存储运行时attr的内容  # list[FTMatched]
        self._binding = []  # 用于存储attr和exec的绑定关系  # list[MonoAttr]

    @property
    def dgs(self):
        return self._dgs

    @property
    def ft(self):
        return self._ft

    @property
    def monos(self):
        return self._binding.copy()

    @property
    def attrs(self):
        return self._binding.copy()

    @property
    def readonlys(self) -> list[str]:  # 识别被readonly修饰的参数
        res = []
        for attr in self._binding:
            if attr.readonly:
                res.append(attr.name)
        return res

    @property
    def dict(self):
        initial = self._build_env()
        current = self.env
        return {k: v for k, v in current.items() if k not in initial and not k.startswith("__")}

    @property
    def types(self):
        return {k: type(v) for k, v in self.dict.items()}

    @property
    def keys(self):
        dfs = self.dict
        return list(dfs.keys())

    @property
    def env(self):
        return self._env.copy()

    @property
    def envs(self):
        """
        获取一个用于展示的env
        """
        return {k: v for k, v in self._env.items() if not k.startswith("__")}

    @property
    def with_attrubute(self):
        return self._ASO is not None and self._AEO is not None

    def _build_gs(self):
        """
        根据设定值创建Groups
        """
        # 捕获 ESO express_line EEO  的格式
        epgs, epids = [f"{self._ESO}{FT.BNN}*", f".+?", f"?=({FT.BNN}*{self._EEO})", f"{FT.BNN}*{self._EEO}"], [0, 1, 3]
        # 捕获 XSO express_line XEO  的格式
        xpgs, xvids = [f"{self._XSO}{FT.BNN}*", f"{FT.ANY_CHAR}+?", f"?=({FT.BNN}*{self._XEO})", f"{FT.BNN}*{self._XEO}"], [0, 1, 3]
        # 捕获 VSO express_line VEO  的格式
        vlgs, vlids = [f"{self._VSO}{FT.BNN}*", f".+?", f"?=({FT.BNN}*{self._VEO})", f"{FT.BNN}*{self._VEO}"], [0, 1, 3]
        # 捕获 ASO attribute AEO  的格式
        apgs, aaids = [f"{self._ASO}{FT.BNN}*", f".+", f"?=({FT.BNN}*{self._AEO})", f"{FT.BNN}*{self._AEO}"], [0, 1, 3]

        # 创建移除comment的group
        rmgs0, rmgs1 = [self._COMMENT, ".*"], [self._CSO, f"{FT.ANY_CHAR}+", f"{FT.WF(True, self._CEO)}", self._CEO]

        return {
            'exec': [epgs, epids],
            'execs': [xpgs, xvids],
            'eval': [vlgs, vlids],
            'attr': [apgs, aaids],
            'rmgs': [rmgs0, rmgs1],
        }

    def _build_ft(self):
        """
        根据设定值创建FT
        """
        ft = FT()
        ft.login(lambda *args: "", *self._dgs['rmgs'][0], areas=[1])            # 0
        ft.login(self._hook_comments, *self._dgs['rmgs'][1], areas=[0, 1, 3])   # 1
        ft.login(self.clear)  # Pass-In mode login. 用于重置状态          # 2
        ft.login(self._exec_line_hook, *self._dgs['exec'][0], areas=self._dgs['exec'][1])   # 3
        ft.login(self._exec_multilines_hook, *self._dgs['execs'][0], areas=self._dgs['execs'][1])  # 4
        ft.login(self._handle_execs)  # Pass-In mode login. 用于处理exec        # 6
        ft.login(self._update_env)  # Pass-In mode login. 用于处理后续之前更新env     # 5
        ft.login(self._eval_hook, *self._dgs['eval'][0], areas=self._dgs['eval'][1])        # 6
        if self.with_attrubute:
            ft.login(self._attr_hook, *self._dgs['attr'][0], areas=self._dgs['attr'][1])        # 7
            ft.login(self._handle_attr)  # Pass-In mode login. 用于处理attr                             # 8
        # clear multiple lines
        # ft.login(lambda *args: '', "(\n[ \t]*)(\n[ \t]*)+")
        # ft.login(lambda *args: '', "^(\n[ \t]*)+")  # clear start

        return ft

    def _build_sft(self):
        """
        创建Slave FT
        """
        sft = FT()
        sft.login(lambda *args: "", *self._dgs['rmgs'][0], areas=[1])
        sft.login(self._hook_comments, *self._dgs['rmgs'][1], areas=[0, 1, 3])
        sft.login(self._eval_hook, *self._dgs['eval'][0], areas=self._dgs['eval'][1])
        # # clear multiple lines
        # sft.login(lambda *args: '\n', "(\n[ \t]*){2,}\n")
        # sft.login(lambda *args: '', "^(\n[ \t]*)+")  # clear start

        return sft

    def _manual_rmv_multilines(self, s: str):
        """
        手动移除多余的换行符
        """
        while True:
            _hash = hash(s)
            s = re.sub("(\r?\n[ \t]*)(\r?\n[ \t]*)(\r?\n[ \t]*)+", "\n\n", s)
            if _hash == hash(s):
                break
        return s


    def _build_env(self):
        """
        创建虚拟环境
        """
        env = {}
        if self._ENV:
            exec(self._ENV, env)
        return env

    def _update_env(self):
        """
        更新env. 用于在处理eval replace之前更新env
        """
        self._env.update(self._overenv)

    def clear(self):
        """
        清空执行环境
        """
        self._execs.clear()
        self._exevs.clear()
        self._attrs.clear()
        self._binding.clear()
        self._env = self._build_env()

    @staticmethod
    def _triple_wrap_newlines(_0, raw_s, rep_s, _1, *, rep=True):
        """
        对经典的三个group进行补充换行符的处理。
        * 有助于你保持lineno
        * rep: 是否使用rep_s插入到目标输出中
        """
        raws_cnt, reps_cnt = Mono._api_count_newline(raw_s), Mono._api_count_newline(rep_s)
        _0_cnt, _1_cnt = Mono._api_count_newline(_0), Mono._api_count_newline(_1)
        if not rep:
            assert raws_cnt == reps_cnt, f"raws_cnt:{raws_cnt} reps_cnt:{reps_cnt}\nThis is a reft-lib error. Not user's\ndetail: Should pass in same raw_s and rep_s if use rep=False."
            return (_0_cnt + reps_cnt + _1_cnt) * '\n'
        else:
            if reps_cnt > raws_cnt:  # 目标替换的内容比原内容的换行符更多
                added = reps_cnt - raws_cnt
                if added > _1_cnt:  # _0是不能被优化的，它会影响rep_s的lineno，只能登记'膨胀信息'到current
                    _vno, _bno = _1.lineno, added - _1_cnt
                    _1_cnt = 0
                else:
                    _1_cnt -= added
            return _0_cnt * '\n' + str(rep_s) + _1_cnt * '\n'

    def _hook_comments(self, _0, s: FTMatched, _1):
        """
        处理comments
        """
        return self._triple_wrap_newlines(_0, s, s, _1, rep=False)

    def _exec_line_hook(self, _0, s: FTMatched, _1):
        """
        处理eval
        """
        if _DEBUG_MODE: print("exec", s)
        self._exevs.append(s)
        return self._triple_wrap_newlines(_0, s, s, _1, rep=False)

    def _exec_multilines_hook(self, _0, s: FTMatched, _1):
        """
        处理exec
        """
        if _DEBUG_MODE: print("execs", s)
        self._execs.append(s)
        return self._triple_wrap_newlines(_0, s, s, _1, rep=False)

    def _handle_execs(self, depth=FT_DEPTH):
        self._env = api_ftmono_handle_execs(self._exevs + self._execs, self._env, self._overenv, depth=depth)
        if _DEBUG_MODE: print("execs passed, env=", self.envs)

    def _eval_hook(self, _0, s: FTMatched, _1):
        """
        处理eval
        """
        if _DEBUG_MODE: print("eval", s)

        # handle eval
        try:
            _ev = eval(str(s), self._env)
        except Exception as e:
            raise FTMonoEvalError(s, self.envs)
        return self._triple_wrap_newlines(_0, s, _ev, _1, rep=True)

    def _attr_hook(self, _0, s: FTMatched, _1):
        """
        处理attr
        """
        if _DEBUG_MODE: print("attr", s)

        self._attrs.append(s)
        return self._triple_wrap_newlines(_0, s, s, _1, rep=False)

    def _handle_attr(self):
        """
        处理attr(self._attrs)
        * 1. 每个s:FTMatched都有一个lineno的属性。把一个或多个attr绑定到一个exec-line上。
        * 2. exec-multilines可以打断attr的绑定, 此时抛出异常FTMonoAttrToMultiExecs
        * self._execs multilines; self._exevs line
        * 均为list[FTMatched]
        * 使用api_parse_python_single_line_vardef获取变量名
        :return: dict  # {var_name of _exevs: [s of _attr]}

        例如:
        // [Type(BOOL)]
        // [READONLY]
        //> add_en=False

        exevs: ["add_en=False"], attrs: ["Type(BOOL)", "READONLY"] execs: []
        return {"add_en": ["Type(BOOL)", "READONLY"]}
        """
        _items = []
        TYPE_EXEV, TYPE_EXECS, TYPE_ATTRS = 0, 1, 2
        for s in self._exevs:
            s._MONO_TYPE = TYPE_EXEV
            _items.append(s)
        for s in self._execs:
            s._MONO_TYPE = TYPE_EXECS
            _items.append(s)
        for s in self._attrs:
            s._MONO_TYPE = TYPE_ATTRS
            _items.append(s)

        _items.sort(key=lambda x: x.lineno)  # 按照行号排序

        _res = []
        _acc_attrs = []  # 用于存储当前尚未被打断的连续的attr列表
        for i, s in enumerate(_items):
            if s._MONO_TYPE == TYPE_ATTRS:
                # 将a|b|c ... 转换为 [a, b, c, ...]:list
                s_lst = [i.strip() for i in str(s).split('|') if i.strip()]

                # 分敛符合变量名的开头和以数字和非_符号开头的符号
                _new, _errs = [], []
                for it in s_lst:
                    if it[0].isalpha() or it[0] == '_':
                        _new.append(it)
                    else:
                        _errs.append(it)

                # 抛出警告
                for it in _errs:
                    print(f"Warning: '{it}' is not a valid variable name. It will be ignored.")
                s_lst = _new

                _acc_attrs.extend(s_lst)
            elif s._MONO_TYPE == TYPE_EXEV:
                if _acc_attrs:
                    var_name, var_value = api_parse_python_single_line_vardef(str(s), self.env)  # 获取变量名和当前值(*如果没有指定覆盖参数，那么就是默认值)
                    if var_name:
                        _res.append(MonoAttr(var_name, var_value, *_acc_attrs, lineno=s.lineno))
                        _acc_attrs = []  # 重置属性列表
            elif s._MONO_TYPE == TYPE_EXECS and _acc_attrs:
                raise FTMonoAttrToMultiExecs(f"Attrubites can not bind to multiple-execs.\n\nWaiteds:{_acc_attrs}\n\ncurrent execs:{s}")
            # else:  # 不应该出现这种情况
            #     raise

        if _DEBUG_MODE: print("attrs passed, res=", _res)
        self._binding = _res

    def handle(self, s, **params):
        """
        处理目标代码，并返回处理后的结果。
        * 使用params来传递覆盖的参数
        """
        self._overenv = params

        # remove redonlys
        for k in self.readonlys:
            self._overenv.pop(k, None)

        res = self._ft.handle(s)
        self._overenv = {}
        return self._manual_rmv_multilines(res)

    def build(self, s) -> str | None:
        """
        解析目标代码，并将有关结果存储在self中. 解析失败时返回错误str
        """
        try:
            self._ft.handle(s)
        except Exception as e:
            return str(e)

    def slaveHandle(self, s) -> str:
        """
        根据已有的环境对目标代码进行处理。
        该处理不会改变env，意味着只有eval和ifbr可以被处理
        """
        res = self._sft.handle(s)
        return self._manual_rmv_multilines(res)




if __name__ == '__main__':
    mono = Mono(
        "//\s*>", "\n",
        "\$", "\$",
        None, "//\s*<",
        "//\s*\[", "\]",
        "//\s*\?", '//\s*:\?', "//\s*:", "//\s*\$",
        COMMENT=r";#", CSO=r"/*#", CEO=r"\*/",
        ENV=r"import math"
    )

    with open('counter.v5.v', 'r', encoding="utf-8") as f:
        test = f.read()

    with open('saved.v', 'w', encoding="utf-8") as f:
        f.write(mono.handle(test, WIDTH=10, add_en=True))

    print(mono.monos)
