#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from argparse import ArgumentParser


#--------------------------------------------------------------------------------
# 상수 목록.
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
# 커맨드 매니저.
#--------------------------------------------------------------------------------
class CommandManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self):
		pass


	#--------------------------------------------------------------------------------
	# 새 프로젝트 생성.
	#--------------------------------------------------------------------------------
	def ProjectNew(self, type : str, value : str) -> None:
		builtins.print(f"CommandManager.NewProject(type = {type}, value = {value})")


	#--------------------------------------------------------------------------------
	# 프로젝트 제거.
	#--------------------------------------------------------------------------------
	def ProjectDelete(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트 업데이트.
	#--------------------------------------------------------------------------------
	def ProjectUpdate(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트 실행.
	#--------------------------------------------------------------------------------
	def ProjectRun(self) -> None:
		pass

	#--------------------------------------------------------------------------------
	# 프로젝트 빌드.
	#--------------------------------------------------------------------------------
	def ProjectBuild(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트 임시파일 제거.
	#--------------------------------------------------------------------------------
	def ProjectClear(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트에 구성 생성.
	#--------------------------------------------------------------------------------
	def ConfigurationNew(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트에 구성 제거.
	#--------------------------------------------------------------------------------
	def ConfigurationDelete(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트에 구성 선택.
	#--------------------------------------------------------------------------------
	def ConfigurationSelect(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 프로젝트에 구성 목록 반환.
	#--------------------------------------------------------------------------------
	def GetConfigurations(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 도움말.
	#--------------------------------------------------------------------------------
	def Help(self, mainCommand : str = "", subCommand : str = "") -> None:
		pass

	
	#--------------------------------------------------------------------------------
	# 커맨드라인으로 기능 실행 요청을 받음.
	#--------------------------------------------------------------------------------
	@staticmethod
	def ExecuteFromCLI() -> None:

		# lify
		parser = ArgumentParser(description = "lify") #, add_help = False)
		# parser.add_argument("--help", "-H", action = "help", help = "Show help message and exit")

		# lify {command}
		subparsers = parser.add_subparsers(dest = "mainCommand")
		
		# lify project
		projectParser : ArgumentParser = subparsers.add_parser("project", help = "Project related commands") #, add_help = False)
		# projectParser.add_argument("--help", "-H", action = "help", help = "Show help message and exit")
		projectSubparsers = projectParser.add_subparsers(dest = "projectCommand")
		# lify project new
		newParser : ArgumentParser = projectSubparsers.add_parser("new", help = "Create a new project") #, add_help = False)
		# newParser.add_argument("--help", "-H", action = "help", help = "Show help message and exit")
		newGroupParser = newParser.add_mutually_exclusive_group(required = False)
		# lify project new --name
		newGroupParser.add_argument("--name", "-N", help = "The path to create the project")
		# lify project new --path
		newGroupParser.add_argument("--path", "-P", help = "The name of the project to create")

		# 명령어 변환.
		args = parser.parse_args()

		# 명령어 처리.
		commandManager = CommandManager()

		# 프로젝트 명령.
		if args.mainCommand == "project":
			# 생성.
			if args.projectCommand == "new":
				if args.name:
					commandManager.ProjectNew("name", args.name)
				elif args.path:
					commandManager.ProjectNew("path", args.path)
				else:
					commandManager.ProjectNew()
			else:
				commandManager.Help(args.mainCommand)
		else:
			commandManager.Help()