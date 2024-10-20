import re
import warnings

FT_DEPTH = 999

class InfiniteLoopError(Exception):
    pass

class FTGroupsCompileError(Exception):
    pass


class FTMatched:
    def __init__(self, matched:str, group0:str, string:str, pattern:str, span:tuple, groups:tuple, areas:tuple, *, expansion=None):

        self._string = string
        self._group0 = group0
        self._matched = matched
        self._pattern = pattern
        self._span = tuple(span)
        self._groups = tuple(groups)
        self._areas = tuple(areas)

        assert matched is not None, f'Matched can not be None.'

        # calc once
        self._lineno = self._string[:self._span[0]].count('\n') + 1
        self._lineno = self._calc_expansion(self._lineno, expansion)
        self._hash = hash((self._string, self._group0, self._matched, self._pattern, self._span, self._groups, self._areas))

    @staticmethod
    def _calc_expansion(no, expansion):
        """
        Calculate the expansion
        """
        if expansion is None:
            return no
        for k, v in expansion.items():
            if no > k:
                no -= v
        return no

    @property
    def string(self):
        return self._string

    @property
    def group0(self):
        return self._group0

    @property
    def matched(self):
        return self._matched

    @property
    def pattern(self):
        return self._pattern

    @property
    def span(self):
        return self._span

    @property
    def groups(self):
        return self._groups

    @property
    def areas(self):
        return self._areas

    # ex
    @property
    def lineno(self):
        """
        Return the line number of the matched. Start from 1
        """
        return self._lineno

    @property
    def lineidx(self):
        """
        Return the index of the matched in the line. Start from 0
        """
        return self._lineno - 1


    def __str__(self):
        return self._matched

    def __int__(self):
        return int(self._matched)

    def __float__(self):
        return float(self._matched)

    def __bool__(self):
        return bool(self._matched)

    def __repr__(self):
        return self._matched

    def __getitem__(self, item):
        return self._matched[item]

    def __len__(self):
        return len(self._matched)

    def __iter__(self):
        return self._matched.__iter__()

    def __contains__(self, item):
        return item in self._matched

    def __eq__(self, other):
        return self._matched == other

    def __ne__(self, other):
        return self._matched != other

    def __add__(self, other):
        return self._matched + other

    def __radd__(self, other):
        return other + self._matched

    def __mul__(self, other):
        return self._matched * other

    def __rmul__(self, other):
        return other * self._matched

    def __hash__(self):
        return self._hash


class Current:
    def __init__(self, parent):
        self.parent = parent
        self.id = None
        self.func = None
        self.groups = None
        self.areas = None
        self.embed = None
        self.replace = None

        # ---
        self.expansions = {}   # {int:int}
        self._last_pattern = None
        self._last_pattern_id = None

        # --- not safe
        self.last_position = None
        self.raw_txt = None
        self.matched = None

    def clear(self):
        self.expansions = {}   # {int:int}
        self._last_pattern = None
        self._last_pattern_id = None
        self.last_position = None
        self.raw_txt = None
        self.matched = None

    @property
    def offset(self):
        return self.last_position if self.last_position is not None else 0

    @property
    def pattern(self):
        if self._last_pattern_id == self.id:
            return self._last_pattern
        self._last_pattern = ""
        self._last_pattern_id = self.id
        for group in self.groups:
            self._last_pattern += f'({group})'

        return self._last_pattern

    def toid(self, id):
        if id not in self.parent.ids:
            warnings.warn(f'to: Id {self.id} not exists')
            return

        index = self.parent.ids.index(self.id)
        self.id = id
        self.func = self.parent.funcs[index]
        self.groups = self.parent.groupss[index]
        self.areas = self.parent.areass[index]
        self.embed = self.parent.embeds[index]
        self.replace = self.parent.replaces[index]

        self.last_position = None
        self.matched = None

    def toindex(self, index):
        if index < 0 or index >= len(self.parent.ids):
            warnings.warn(f'to: Index {index} out of range')
            return

        self.id = self.parent.ids[index]
        self.func = self.parent.funcs[index]
        self.groups = self.parent.groupss[index]
        self.areas = self.parent.areass[index]
        self.embed = self.parent.embeds[index]
        self.replace = self.parent.replaces[index]

        self.last_position = None
        self.matched = None

    def __str__(self):
        return f'{self.__class__.__name__}: id={self.id}, func={self.func}, groups={self.groups}, areas={self.areas}, embed={self.embed}, replace={self.replace}'


class FTFlag:
    NONE = 0
    REDO = 1  # redo the current after current finished.  This wont reset the 'lefts'
    SKIP = 2  # skip the current and go to next one
    STOP = 4  # stop the handle process

# Fomater Tool
class FT:
    VARIABLE = "[a-zA-Z_][a-zA-Z0-9_]*"
    NUMBER = "[0-9]*\.?[0-9]+"
    ALPHA = "[a-zA-Z_][a-zA-Z]*"
    INTEGER = "[0-9]+"
    COMMA = ","
    COLON = ":"
    SEMICOLON = ";"
    EQUAL = "="
    PLUS = "\+"
    MINUS = "-"
    MULTIPLY = "\*"
    DIVIDE = "/"
    POWER = "\^"
    LBRACKET = "\("
    RBRACKET = "\)"
    LBRACE = "\{"
    RBRACE = "\}"
    LBRACKET_S = "\["
    RBRACKET_S = "\]"
    LANGLE = "<"
    RANGLE = ">"
    DOLLAR = "\$"
    DOT = "\."
    QUESTION = "\?"

    # RE Special
    BLANK_CHAR = "\s"
    DIGIT_CHAR = "\d"
    WORD_CHAR = "\w"
    NBLANK_CHAR = "\S"
    NDIGIT_CHAR = "\D"
    NWORD_CHAR = "\W"
    ANY_CHAR = "(.|\n)"
    BLANK_NOT_NEWLINE = "[ \t\r\f\v]"
    BNN = BLANK_NOT_NEWLINE
    OP_ANYMORE = "*"
    OP_ATLEAST = "+"
    OP_MAYBE = "?"

    # #
    BLANK_ANYMORE = BLANK_CHAR + OP_ANYMORE
    BLANK_ATLEAST = BLANK_CHAR + OP_ATLEAST
    BLANK_MAYBE = BLANK_CHAR + OP_MAYBE

    def __init__(self):
        self._id = -1  # id
        self.ids = []  # list of ids
        self.funcs = []  # list of functions
        self.groupss = []  # list of groups
        self.areass = []  # list of areas
        self.embeds = []  # list of (is_)embeds
        self.replaces = []  # list of (is_)replaces

        # current
        self.current = Current(self)
        self.flag = FTFlag.NONE

    def link(self, other) -> 'FT':
        """
        Link other FT to this FT
        """
        new_ft = FT()
        new_ft.ids = self.ids + other.ids
        new_ft.funcs = self.funcs + other.funcs
        new_ft.groupss = self.groupss + other.groupss
        new_ft.areass = self.areass + other.areass
        new_ft.embeds = self.embeds + other.embeds
        new_ft.replaces = self.replaces + other.replaces
        return new_ft

    @property
    def id(self):
        self._id += 1
        return self._id

    def _get_id(self):
        return id(self) * 10 + self.id

    @staticmethod
    def WrapForward(eq:bool, pattern:str) -> str:
        return f'?{"=" if eq else "!"}({pattern})'

    WF = WrapForward

    @staticmethod
    def WrapBackward(eq:bool, pattern:str) -> str:
        return f'?<{"=" if eq else "!"}({pattern})'

    WB = WrapBackward

    @staticmethod
    def ToParttern(*groups, clean=True) -> str:
        # clean groups
        if clean:
            groups = FT._api_clean_groups(groups)
        return ''.join([f'({group})' for group in groups])


    @staticmethod
    def ToPartternWithAreas(*groups, areas=None) -> tuple[str, list[int]]:
        # clean groups
        groups = FT._api_clean_groups(groups)

        # areas
        areas = FT._api_auto_prexpand_area(areas, groups)

        # rshift areas
        areas = FT._api_groups_bracket_rshift(groups, areas)

        return FT.ToParttern(*groups, clean=False), areas

    @staticmethod
    def Extract(txt: str, *gs, areas=None) -> list[tuple[FTMatched]]:
        """
        Extract all matched without replace
        :return:
            [
                (areas[0], areas[1], ...),
                ...
            ]
        """
        _res = []
        ft = FT()
        ft.login(lambda *args: _res.append(args), *gs, areas=areas, replace=False)
        ft.handle(str(txt))
        return _res

    @staticmethod
    def _check_bracket(txt: str):
        """
        Check if any brackets in txt
        :param txt:
        :return:
        """
        if txt.find('(') != -1 and txt.find(')') != -1:
            warnings.warn(f'Should not use brackets in {txt}')
            return True
        return False

    @staticmethod
    def _expand_area(areas, size) -> list:
        """
        Expand area to a list
        :param areas:
        :param size: max value. If index over size, will raise Exception
        :return:
        """
        res = []
        for area in areas:
            if isinstance(area, int):
                res += [area]
            elif isinstance(area, tuple):
                if len(area) != 2:
                    raise Exception(f'Area {area} should be a tuple of (start, end)')
                start, end = area
                if start < 0 or start >= size:
                    raise Exception(f'Area {area} start {start} out of range')
                if end < 0 or end >= size:
                    raise Exception(f'Area {area} end {end} out of range')
                if start > end:
                    raise Exception(f'Area {area} start {start} should less than end {end}')
                res += list(range(start, end))
            else:
                raise Exception(f'Area {area} should be a tuple of (start, end) or a index')
        return res


    @staticmethod
    def _api_rm_useless_bracket(txt: str) -> str:
        """
        Remove completely enclosed brackets at the beginning and end of the string, and these brackets should be matching pairs.
        :param txt: The input string with brackets.
        :return: The string with useless brackets removed.
        """

        def _inner_fn(_txt):
            stack, lens = [], len(_txt)
            try:
                for i, char in enumerate(_txt):
                    if char == '(' and (i == 0 or _txt[i - 1] != '\\'):
                        stack.append((char, i))
                    elif char == ')' and (i == 0 or _txt[i - 1] != '\\'):
                        if len(stack) == 1 and stack[0][1] == 0 and i == lens - 1:
                            # 如果堆栈中只有一个元素，且这个元素是字符串的第一个字符，且当前字符是字符串的最后一个字符
                            return _txt[1:-1], True
                        elif stack[-1][0] == '(':
                            stack.pop()
                        else:
                            raise IndexError(f"ft:Brackets do not match at {i} of {_txt}")
            except IndexError as e:
                raise ValueError(f'ft:Brackets do not match in {_txt}') from e
            return _txt, False

        while True:
            txt, changed = _inner_fn(txt)
            if not changed:
                break
        return txt

    @staticmethod
    def _api_count_bracket(txt: str) -> int:
        """
        Count the number of brackets without '\'
        * Ignore ?=, ?!, ?<=, ?<! and (
        :param txt:
        :return:
        """
        count = 0
        for i in range(len(txt)):
            if txt[i] == '(' and (i == 0 or txt[i - 1] != '\\'):
                # 排除正向前瞻和负向前瞻
                if i >= 3 and txt[i-3:i] in ['?<!', '?<=']:
                    continue
                if i >= 2 and txt[i-2:i] in ['?!', '?=']:
                    continue
                count += 1
        return count

    @staticmethod
    def _api_groups_bracket_rshift(gs, areas) -> list:
        """
        rshift the areas if a groups' element have brackets
        """
        lena, copya = len(areas), areas.copy()
        for i, g in enumerate(gs):
            br_cnt = FT._api_count_bracket(g)
            if br_cnt > 0:
                # while t < lena:
                for t in range(lena):
                    if areas[t] > i:  # 考虑areas中超过该index的情况
                        copya[t] += br_cnt
                        t += 1

        return copya


    @staticmethod
    def _api_auto_prexpand_area(areas, groups) -> list:
        # areas
        if areas is None:
            areas = list(range(len(groups)))
        else:
            areas = FT._expand_area(areas, len(groups))
        return areas

    @staticmethod
    def _api_clean_groups(groups) -> tuple:
        # clean groups
        _tmp_groups = list(groups)
        for i, group in enumerate(groups):
            try:
                _tmp_groups[i] = FT._api_rm_useless_bracket(group)
            except ValueError as e:
                raise ValueError(f'ft.login: Unmatched brackets in {group}') from e
        groups = tuple(_tmp_groups)
        return groups

    @staticmethod
    def _try_compile_groups(groups):
        pattern = FT.ToParttern(*groups)
        re.compile(pattern)     # if occur any error, will raise exception

    def login(self, fn, *groups: str, areas: list = None, embed:bool=False, replace:bool=True) -> int:
        """
        Login a function
        :param fn:
        :param groups: can be empty
        :param areas: list of area, each area is a tuple of (start, end) or a index
        :param embed: if embed, groups must have more than 3 items. And rfind first-element when matched.
        :param replace: if replace, will replace the old one
        :return: id

        * Special，you can only pass in a param:func. This will be regard as a simply pass function, and call it without any params.
        """
        # for group in groups:
        #     self._check_bracket(group)

        # check exists
        if fn in self.funcs:
            warnings.warn(f'Function {fn} already exists')

        # check groups
        if groups:  # not pass-in mode.
            if groups in self.groupss:
                warnings.warn(f'Groups {groups} already exists')

            # clean groups
            groups = self._api_clean_groups(groups)

            # areas
            areas = self._api_auto_prexpand_area(areas, groups)

            # rshift areas
            areas = self._api_groups_bracket_rshift(groups, areas)

            # embed
            if embed:
                if len(groups) < 3:
                    raise Exception(f'Groups at embed mode should have more than 3 elements.')
                if not replace:
                    raise Exception(f'Embed mode should use replace=True to avoid infinite loop.')

        # compile check
        try:
            self._try_compile_groups(groups)
        except Exception as e:
            raise FTGroupsCompileError(f'FT.login: Groups compile failed:\n\t{groups}\n\npattern:\n\t{self.ToParttern(*groups)}\n\ndetails:\n\t{e}') from e

        # add
        _id = self._get_id()
        self.ids.append(_id)
        self.funcs.append(fn)
        self.groupss.append(groups)
        self.areass.append(areas)
        self.embeds.append(embed)
        self.replaces.append(replace)

        return _id

    def logout(self, *ids: int):
        """
        logout fn or groups
        :param ids: id return from .login
        :return:
        """
        for identy in ids:
            if identy not in self.ids:
                warnings.warn(f'logout: Id {identy} not exists')
                continue
            index = self.ids.index(identy)
            self.ids.pop(index)
            self.funcs.pop(index)
            self.groupss.pop(index)
            self.areass.pop(index)
            self.embeds.pop(index)
            self.replaces.pop(index)


    @staticmethod
    def _tuple_fall_ele_to_str(fall_ele:tuple|str) -> str:
        """
        Convert fall element to str
        """
        if isinstance(fall_ele, tuple):
            # check only one element is not ''
            _cnt, _the = 0, ""
            for e in fall_ele:
                if e != '':
                    _cnt += 1
                    _the = e
            if _cnt != 1:
                raise Exception(f'Embed with tuple pats should have only one element not \'\'.\n\tget:\n\t\t{fall_ele}')
            return _the
        return fall_ele

    def _consistent_forward_match(self, pat: str, txt: str, full_check_pat:str) -> tuple:
        """
        一致性向前匹配目标，并要求匹配到的目标往后仍然符合整体匹配
        :param pat:
        :param txt:
        :param full_check_pat: 总体检查模式
        :return: full matched (start, end) or None
        """
        raw_txt = txt
        fall = re.findall(pat, txt)
        fall.reverse()
        cut_content = ""
        for index, ele in enumerate(fall):
            # 支持'|'分割导致的tuple格式的find
            ele = self._tuple_fall_ele_to_str(ele)
            _pos = txt.rfind(ele)
            if _pos == -1:
                raise Exception(f'Program meet an strange critical error. Re find a element:{ele}, but rfind report -1;')
            cut_content = txt[_pos:] + cut_content
            full_matched = re.fullmatch(full_check_pat, cut_content)
            if full_matched is not None:
                # _debug_str = raw_txt[_pos:len(raw_txt)]
                return _pos, len(raw_txt)
            txt = txt[:_pos]
        return None

    def _consistent_backward_match(self, pat: str, txt: str, full_check_pat:str) -> tuple:
        """
        一致性向后匹配目标，并要求匹配到的目标往前仍然符合整体匹配
        :param pat:
        :param txt:
        :param full_check_pat: 总体检查模式
        :return: full matched (start, end) or None
        """
        raw_txt = txt
        fall = re.findall(pat, txt)
        cut_content = ""
        for index, ele in enumerate(fall):
            # 支持'|'分割导致的tuple格式的find
            ele = self._tuple_fall_ele_to_str(ele)
            _pos = txt.find(ele)
            if _pos == -1:
                raise Exception(f'Program meet an strange critical error. Re find a element:{ele}, but rfind report -1;')
            cut_content += txt[:_pos + len(ele)]
            full_matched = re.fullmatch(full_check_pat, cut_content)
            if full_matched is not None:
                # _debug_str = raw_txt[:_pos + len(ele)]
                return 0, len(cut_content)
            txt = txt[_pos + len(ele):]
        return None


    def _handle_matched(self, matched:re.Match) -> str:
        # get each groups
        cares = matched.groups()
        # create params
        params = []
        for area in self.current.areas:
            if not isinstance(area, int):
                raise Exception(f'Area {self.current_areas} should be a list[int].')

            # area is index, index 0 is total, need +1 to get the correspond group
            _span = matched.span(area + 1)
            _span = (self.current.offset + _span[0], self.current.offset + _span[1])
            ftm = FTMatched(matched.group(area + 1), matched.group(), self.current.raw_txt, matched.re.pattern, _span, self.current.groups, self.current.areas, expansion=self.current.expansions)
            params.append(ftm)
        # call
        return str(self.current.func(*params))

    def _handle_current_once(self, raw_txt: str) -> str:
        """
        Handle current once.
        return changed_txt or None
        """

        self.current.raw_txt = raw_txt

        if self.current.last_position is not None:
            txt = raw_txt[self.current.last_position:]
            offset = self.current.last_position
        else:
            txt = raw_txt
            offset = 0
#'(\\$[ \t\r\x0c\x0b]*)(.+)(?=([ \t\r\x0c\x0b]*\\$))([ \t\r\x0c\x0b]*\\$)'
        # search
        matched = re.search(self.current.pattern, txt)


        # not matched
        if matched is None:
            self.current.last_position = None
            return

        span = (matched.start() + offset, matched.end() + offset)
        _raw_span = span

        # if embed, rfind first-element and find the neg-element
        if self.current.embed:
            gfe = self.current.groups[0]
            content = matched.group()
            cfm = self._consistent_forward_match(gfe, content, self.current.pattern)
            if cfm is not None:
                span = cfm

            gne = self.current.groups[-1]
            content = content[span[0]:]
            cbm = self._consistent_backward_match(gne, content, self.current.pattern)
            if cbm is not None:
                span = (span[0], cbm[1] + span[0])

            # update matched
            content = matched.group()[span[0]:span[1]]
            matched = re.fullmatch(self.current.pattern, content)

            # add bias refer to raw_txt
            span = (span[0] + _raw_span[0], span[1] + _raw_span[0])

        # general mode
        rep = self._handle_matched(matched)
        if self.current.replace:
            loop_check = re.search(self.current.pattern, rep)
            if loop_check is not None:
                warnings.warn(f'Infinite loop detected in your replace txt: {rep}. Which matched by {matched} in: \t{self.current}')

        # first exit point
        self.current.last_position = span[1] + 1
        if not self.current.replace:
            return raw_txt

        # replace
        txt = raw_txt[:span[0]] + rep + raw_txt[span[1]:]
        self.current.last_position = None  # reset if replace
        return txt


    def handle(self, txt: str, depth=FT_DEPTH):
        self.current.clear()    # clear current
        lens = len(self.funcs), len(self.groupss)
        assert lens[0] == lens[1], f'Length of funcs, groups not equal: {lens}'
        for i in range(lens[0]):
            self.current.toindex(i)
            lefts = depth
            if i == 8:
                __ = 0  # debug position

            while True:  # 完全由内部控制
                # check pass-in mode
                if len(self.current.groups) == 0:
                    # simply exec
                    self.current.func()
                else:
                    # loop-match
                    while lefts > 0:
                        lefts -= 1
                        ret = self._handle_current_once(txt)
                        if ret is None:
                            break
                        txt = ret

                        if self.flag & FTFlag.STOP:
                            # self.flag &= ~FTFlag.STOP  # Change at outer while
                            break

                        if self.flag & FTFlag.SKIP:
                            self.flag &= ~FTFlag.SKIP
                            break

                        if lefts == 0:
                            raise InfiniteLoopError(f'Infinite loop detected in {self.current}')


                # flag check
                if self.flag & FTFlag.STOP:
                    self.flag &= ~FTFlag.STOP
                    break
                elif self.flag & FTFlag.REDO:
                    self.flag &= ~FTFlag.REDO
                    continue
                else:
                    break

        return txt

    def logexpn(self, valid_no:int, bias_no:int):
        """
        记录 expansion信息
        * 只在当前handle周期内有效
        最终，当某个计算得到的no > valid_no时，将会-bias_no
        * 理论上, valid_no在同一周期内不会重复，具有唯一性
        """
        self.current.expansions[valid_no] = bias_no


    # call
    def __call__(self, txt: str):
        return self.handle(txt)

    def __str__(self):
        return f'{self.__class__.__name__}: funcs={self.funcs}, groups={self.groupss}, areas={self.areass}'

    def __len__(self):
        return len(self.funcs)

    def __iter__(self) -> Current:
        for i in range(len(self.funcs)):
            self.current.toindex(i)
            yield self.current

    def __add__(self, other):
        return self.link(other)

    def __iadd__(self, other):
        _new = self.link(other)
        self.ids = _new.ids
        self.funcs = _new.funcs
        self.groupss = _new.groupss
        self.areass = _new.areass
        self.embeds = _new.embeds
        self.replaces = _new.replaces
        return self

class FRemove(FT):
    """
    Remove data by format
    """

    def __init__(self):
        super().__init__()

    def login(self, *groups: str):
        super().login(lambda *args: "", *groups, replace=True)


class FDict(FT):
    """
    Get Dict data by format
    """

    def __init__(self):
        super().__init__()
        self.dict = {}

    def _hook_key_val(self, *args, key_id=None, val_id=None, val_default=None):
        assert key_id is not None, f'key_id should not be None'
        key = args[key_id]
        if val_id is None:
            val = val_default
        else:
            val = args[val_id]
        self.dict[key] = val
        return ''

    def login(self, key_id, val_id, *groups: str, areas: list = None, val_default=None, replace=False):
        fn = lambda *args: self._hook_key_val(*(str(it) for it in args), key_id=key_id, val_id=val_id, val_default=val_default)
        super().login(fn, *groups, areas=areas, replace=replace)

    # dict functions
    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __contains__(self, item):
        return item in self.dict

    def __len__(self):
        return len(self.dict)

    def __iter__(self):
        return self.dict.__iter__()

    def __str__(self):
        return self.dict.__str__()

    def __bool__(self):
        return bool(self.dict)

    def clear(self):
        self.dict.clear()

    def pop(self, key):
        return self.dict.pop(key)

    def get(self, key, default=None):
        return self.dict.get(key, default)

    def todict(self):
        return self.dict.copy()


class FSet(FT):
    """
    Get Set data by format
    """

    def __init__(self):
        super().__init__()
        self.set = set()

    def _hook_set(self, *args, val_id=None):
        assert val_id is not None, f'val_id should not be None'
        self.set.add(args[val_id])
        return ''.join(args)

    def login(self, val_id: int, *groups: str, areas: list = None, replace=False):
        fn = lambda *args: self._hook_set(*(str(it) for it in args), val_id=val_id)
        super().login(fn, *groups, areas=areas, replace=replace)

    # set functions
    def add(self, item):
        self.set.add(item)

    def remove(self, item):
        self.set.remove(item)

    def discard(self, item):
        self.set.discard(item)

    def pop(self):
        return self.set.pop()

    def clear(self):
        self.set.clear()

    def __contains__(self, item):
        return item in self.set

    def __len__(self):
        return len(self.set)

    def __iter__(self):
        return self.set.__iter__()

    def __str__(self):
        return self.set.__str__()

    def __bool__(self):
        return bool(self.set)

    def toset(self):
        return self.set.copy()


class FList(FT):
    """
    Get List data by format
    """

    def __init__(self):
        super().__init__()
        self.list = []

    def _hook_list(self, *args, val_id=None):
        assert val_id is not None, f'val_id should not be None'
        self.list.append(args[val_id])
        return ''.join(args)

    def login(self, val_id: int, *groups: str, areas: list = None, replace=False):
        fn = lambda *args: self._hook_list(*(str(it) for it in args), val_id=val_id)
        super().login(fn, *groups, areas=areas, replace=replace)

    # list functions
    def append(self, item):
        self.list.append(item)

    def remove(self, item):
        self.list.remove(item)

    def pop(self, index=-1):
        return self.list.pop(index)

    def clear(self):
        self.list.clear()

    def __contains__(self, item):
        return item in self.list

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __iter__(self):
        return self.list.__iter__()

    def __str__(self):
        return self.list.__str__()

    def __bool__(self):
        return bool(self.list)

    def tolist(self):
        return self.list.copy()




class FBranch(FT):
    """
    if-else branch
    if true, replace with true_fn(can be None, mean remove it)
    if false, replace with false_fn(can be None, mean remove it)
    """

    def _hook_branch(self, *args, cond_vids=None, cond_fn=None, true_vids=None, true_fn=None, false_vids=None, false_fn=None):
        if cond_vids is None or cond_fn is None:
            raise Exception(f'Condition vid and fn should not be None')
        # condition
        params = []
        for vid in cond_vids:
            if vid >= len(args):
                raise Exception(f'Condition vid {vid} out of range(len = {len(args)})')
            params.append(args[vid])

        if cond_fn(*params):
            # true
            if true_vids is not None and true_fn is not None:
                params = []
                for vid in true_vids:
                    if vid >= len(args):
                        raise Exception(f'True vid {vid} out of range(len = {len(args)})')
                    params.append(args[vid])
                return true_fn(*params)
            else:
                return ''
        else:
            # false
            if false_vids is not None and false_fn is not None:
                params = []
                for vid in false_vids:
                    if vid >= len(args):
                        raise Exception(f'False vid {vid} out of range(len = {len(args)})')
                    params.append(args[vid])
                return false_fn(*params)
            else:
                return ''


    def login(self, cond_vids, cond_fn, true_vids, true_fn, false_vids, false_fn, *groups, areas: list = None):
        """
        :param cond_vids: condition value ids
        :param cond_fn: condition function. return is bool(not a str)
        :param true_vids: true value ids. pass None if no false
        :param true_fn: true function. pass None if no false
        :param false_vids: false value ids. pass None if no false
        :param false_fn: false function. pass None if no false
        :param groups:
        :param areas:
        :return:
        """
        fn = lambda *args: self._hook_branch(*args, cond_vids=cond_vids, cond_fn=cond_fn, true_vids=true_vids, true_fn=true_fn, false_vids=false_vids, false_fn=false_fn)
        super().login(fn, *groups, areas=areas, replace=True, embed=True)


if __name__ == '__main__':
    test = """
        Pip 和 Conda 是 Python 的两大软件包管理工具，它们的官方源在国内访问困难，下载速度非常慢。一般情况下我们使用的都是国内的镜像源，例如清华大学的 TUNA 镜像站、阿里云的镜像站。
    
    但是有些软件包体积非常大，安装的时候从镜像站下载下来仍然需要等待很长时间，如果正巧遇到镜像站负载高峰导致下载速度缓慢，那更是雪上加霜。
    
    为了防止配环境的时候软件包下载等待时间过长，$SINGLE:114$可行的方法就是搭建$SINGLE1:514$本地镜像源，在下载的时候直接从本地镜像源下载，速度能够达到内网带宽。如果是千兆内网，那么理论可以达到 125MB/s，这个速度即使是$SINGLE2:9$ GB 的软件包，也能在半分钟内装好。
    """
    ft = FDict()
    ft.login(0, 1, FT.DOLLAR, FT.VARIABLE, FT.COLON, FT.NUMBER, FT.DOLLAR, areas=[1, 3])
    # print(ft(test))
    # print(ft)

    test = """
    // $if myFunctionA(114):
        1
    // #else
        // $if ctypes.dll(0x44H00F)(DWordData(514)):
            2
        // #else
            3
        // #
        
        // $if 114 > 514:
            4
        // #else
            5
        // #
    // #
    """
    ft = FBranch()
    gs = [
        "//\s*\$if\s+", "[^:]+", ":", "(.|\n)+", "?=//\s*#", "//\s*#else\s*", "(.|\n)+", "?=//\s*#", "//\s*#"
    ]
    ft.login([1], lambda x: eval(x), [3], lambda x: x, [6], lambda x: x, *gs)

    print(ft(test))


# ------------------------------------------------------------------------------------------------------------------------------------- #
# Re new function
def strip(txt:str, __chars:str=None) -> str:
    """
    Strip txt by pattern
    """
    if isinstance(txt, FTMatched):
        txt = txt.matched

    if __chars is None:
        return txt.strip()

    pat_start = f'^[{__chars}]+'
    pat_end = f'[{__chars}]+$'

    start = re.sub(pat_start, '', txt)
    end = re.sub(pat_end, '', start)
    return end


