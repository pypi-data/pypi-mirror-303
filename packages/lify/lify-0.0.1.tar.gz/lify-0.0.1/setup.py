#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
import os
import setuptools


#--------------------------------------------------------------------------------
# 상수 목록.
#--------------------------------------------------------------------------------
UTF8 : str = "utf-8"
READ : str = "r"


#--------------------------------------------------------------------------------
# 참조 메타 데이터 목록.
#--------------------------------------------------------------------------------
NAME : str = "lify"
VERSION : str = "0.0.1" # 접두어 v 붙여도 알아서 정규화하면서 제거됨.
AUTHOR : str = "sidoware"
AUTHOR_EMAIL : str = "developer@sidoware.com"
DESCRIPTION : str = "python crossplatform project manager"
LONG_DESCRIPTION_CONTENT_TYPE : str = "text/markdown"
URL : str = "https://sidoware.com"
PYTHON_REQUIRES : str = ">=3.7"
LONGDESCRIPTION : str = str()
with open(file = "README.md", mode = READ, encoding = UTF8) as file: LONGDESCRIPTION = file.read()


#--------------------------------------------------------------------------------
# 빌드.
#--------------------------------------------------------------------------------
setuptools.setup(
	name = NAME,
	version = VERSION,
	author = AUTHOR,
	author_email = AUTHOR_EMAIL,
	description = DESCRIPTION,
	long_description = LONGDESCRIPTION,
	long_description_content_type = LONG_DESCRIPTION_CONTENT_TYPE,
	url = URL,
	packages = setuptools.find_packages(where = "src"),
	include_package_data = True,
	package_dir = { "": "src" },
	package_data = {
		"": [
			"res/*"
		],
	},
	scripts = [

	],
	entry_points = {
		"console_scripts": [
			# "lify=sidoware.lify.command:Command"
		]
	},
	install_requires = [
	],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	],
	python_requires = PYTHON_REQUIRES
)