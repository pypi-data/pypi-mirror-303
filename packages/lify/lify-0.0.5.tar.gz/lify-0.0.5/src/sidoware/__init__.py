#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
import pkgutil
import sys


#--------------------------------------------------------------------------------
# 다른 sidoware 패키지와 네임스페이스 공유.
#--------------------------------------------------------------------------------
__path__ = pkgutil.extend_path(__path__, __name__)


#--------------------------------------------------------------------------------
# 패키지 안의 클래스 별칭 목록.
#--------------------------------------------------------------------------------
# from .core import *
from .lify import *
# from .lify import ProjectData, ConfigurationData, PackageData, ProjectManager, CommandManager


#--------------------------------------------------------------------------------
# 독립 모듈로 추가.
#--------------------------------------------------------------------------------
sys.modules["lify"] = sys.modules["sidoware.lify"]
