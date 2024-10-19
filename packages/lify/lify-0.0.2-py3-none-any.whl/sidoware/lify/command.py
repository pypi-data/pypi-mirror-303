#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
# from dduk.core.builtins import Builtins


#--------------------------------------------------------------------------------
# 상수 목록.
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
# 커맨드 사용을 위한 클래스.
#--------------------------------------------------------------------------------
class Command:
	@staticmethod
	def NewProject():
		pass

	@staticmethod
	def DeleteProject():
		pass

	@staticmethod
	def UpdateProject():
		pass

	@staticmethod
	def RunProject():
		pass

	@staticmethod
	def BuildProject():
		pass

	@staticmethod
	def CleanupProject():
		pass

	@staticmethod
	def NewConfiguration():
		pass

	@staticmethod
	def DeleteConfiguration():
		pass

	@staticmethod
	def SetConfiguration():
		pass

	@staticmethod
	def GetConfigurations():
		pass