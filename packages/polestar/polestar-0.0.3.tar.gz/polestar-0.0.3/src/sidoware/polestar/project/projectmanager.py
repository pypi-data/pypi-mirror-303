#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from .data import ProjectData, ConfigurationData, PackageData


#--------------------------------------------------------------------------------
# 프로젝트 매니저.
#--------------------------------------------------------------------------------
class ProjectManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__projectData : ProjectData


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__projectData = ProjectData()


	#--------------------------------------------------------------------------------
	# 프로젝트 파일 생성됨.
	#--------------------------------------------------------------------------------
	def CreateProject(self, path : str) -> bool:
		path = path
		name = path
		extension = path

		projectData = ProjectData()
		projectData.name = name
		projectData.configurations = list()
		return False
	

	#--------------------------------------------------------------------------------
	# 프로젝트 파일 생성됨.
	#--------------------------------------------------------------------------------
	def CreateConfiguration(self, configurationData : ConfigurationData) -> bool:
		return False