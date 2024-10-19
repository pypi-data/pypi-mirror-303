#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from dataclasses import dataclass


#--------------------------------------------------------------------------------
# 패키지 데이터.
#--------------------------------------------------------------------------------
@dataclass
class PackageData:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	name : str = ""
	version : str = ""
	createDate : str = ""
	updateDate : str = ""