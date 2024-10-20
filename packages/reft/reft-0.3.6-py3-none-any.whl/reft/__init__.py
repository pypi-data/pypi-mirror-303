from reft.ft import re, FT, FDict, FSet, FList, FRemove, FTMatched
from reft.ft import strip as _reinsertfn_strip
from reft.mono import Mono
try:
    from reft.mono_ui import QMonoWidget, QMonoInspector, QMonoLogo
except ImportError:
    QMonoWidget = QMonoInspector = QMonoLogo = None

# insert into re
re.strip = _reinsertfn_strip

__version__ = '0.3.x'


