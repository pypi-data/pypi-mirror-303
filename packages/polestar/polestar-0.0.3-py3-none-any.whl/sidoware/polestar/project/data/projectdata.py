#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from dataclasses import dataclass, field
from .configurationdata import ConfigurationData


#--------------------------------------------------------------------------------
# 프로젝트 데이터. (project.polestar)
#--------------------------------------------------------------------------------
@dataclass
class ProjectData:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	name : str = ""
	description : str = ""
	polestarVersion : str = ""
	createDate : str = ""
	updateDate : str = ""
	include : bool = False
	configurations : list[ConfigurationData] = field(default_factory = list)