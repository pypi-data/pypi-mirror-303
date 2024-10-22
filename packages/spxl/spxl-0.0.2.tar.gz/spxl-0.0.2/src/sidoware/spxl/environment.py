#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import platform
from enum import Enum, auto
import subprocess
from .builtins import Builtins


#--------------------------------------------------------------------------------
# 플랫폼 타입.
#--------------------------------------------------------------------------------
class PlatformType(Enum):
	UNKNOWN = auto()
	
	# windows.
	WINDOWS = auto()

	# linux.
	LINUX = auto()
	ANDROID = auto()
	STEAMOS = auto()

	# apple.
	MACOS = auto()
	IOS = auto()
	IPADOS = auto()
	WATCHOS = auto()
	TVOS = auto()
	VISIONOS = auto()

	# web.
	WEBGL = auto()
	WEBGPU = auto()


#--------------------------------------------------------------------------------
# 현재 시스템의 플랫폼 타입 반환.
#--------------------------------------------------------------------------------
def GetPlatformType() -> PlatformType:
	systemName : str = platform.system()
	systemName = systemName.upper()
	if systemName == "WINDOWS":
		return PlatformType.WINDOWS
	elif systemName == "DARWIN":
		return PlatformType.MACOS
	elif systemName == "LINUX":
		return PlatformType.LINUX
	else:
		return PlatformType.UNKNOWN
	

#--------------------------------------------------------------------------------
# 현재 시스템에 설치된 파이썬 목록을 별도 콘솔에서 조회하여 반환.
#--------------------------------------------------------------------------------
def GetPythonInterpreters() -> list[str]:
	try:
		platformType : PlatformType = GetPlatformType()
		if platformType == PlatformType.WINDOWS:
			output : str = subprocess.check_output("where python", shell = True, text = True)
		else:
			output : str = subprocess.check_output("which -a python python3", shell = True, text = True)
		interpreters : list[str] = output.strip().split("\n")
		return interpreters
	except Exception as exception:
		return list()