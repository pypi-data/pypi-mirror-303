#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from dataclasses import dataclass, field
from .packagedata import PackageData


#--------------------------------------------------------------------------------
# 구성 데이터. (configuration)
#--------------------------------------------------------------------------------
@dataclass
class ConfigurationData:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	name : str = ""
	description : str = ""
	createDate : str = ""
	updateDate : str = ""
	interpreterVersion : str = ""
	interpreterPath : str = ""
	buildType : str = "" # exec, library, docker
	usingPackages : list[PackageData] = field(default_factory = list)