#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import os
from uuid import uuid1, uuid4
from enum import Enum, auto
from .builtins import Builtins
from .environment import PlatformType, GetPlatformType


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
EMPTY : str = ""
HYPHEN : str = "-"
SLASH : str = "/"
BACKSLASH : str = "\\"
TILDE : str = "~"
ROOTMARKERS : list[str] = [
	# 저장소.
	".svn",				# Subversion (SVN) version control system folder.
	".p4config",		# Perforce configuration file.
	".p4ignore",		# Perforce ignore patterns file.
	".git",				# Git version control system folder.
	".hg",				# Mercurial version control system folder.

	# 개발환경.
	".vscode",			# Visual Studio Code settings directory.
	".vs",				# Visual Studio settings directory.
	".idea",			# JetBrains IDE (PyCharm, IntelliJ IDEA, etc.) settings directory.

	# 파이썬 루트 파일.
	"setup.py",			# Python project setup script.
	"requirements.txt",	# Python project dependencies file.
	"Pipfile",			# Python project Pipenv dependency management file.
	"pyproject.toml",	# Python project configuration file.
	
	# "package.json",  # Node.js project configuration file.
	# "composer.json", # PHP project Composer configuration file.
	# "CMakeLists.txt",# CMake project configuration file.
	# "Makefile",      # Unix/Linux project build automation script.
	# "Cargo.toml",    # Rust project configuration file.
	# "gradle.build",  # Gradle project build script.
	# "pom.xml",       # Maven project configuration file.
	# ".terraform",    # Terraform configuration directory.
	# "Gemfile",       # Ruby project dependency management file.
	# "Rakefile",      # Ruby project build automation script.
	# "config.yml",    # Common YAML configuration file.
	# "config.yaml",   # Common YAML configuration file.
	# ".circleci",     # CircleCI configuration directory.
	# ".travis.yml",   # Travis CI configuration file.
]


#--------------------------------------------------------------------------------
# 프로젝트 패스.
#--------------------------------------------------------------------------------
class UUIDType(Enum):
	UUID1 = auto() # 호스트의 네트워크 주소와 현재 시간 기반으로 UUID를 생성. (6f5c62f0-7ea4-11ec-9c2b-0242ac130003 - 앞에서 세그룹은 타임스탬프 비트 (하위 > 중간 > 상위), 네번째그룹은 랜덤클럭시퀀스+노드정보기반, 다섯번째그룹은 호스트의 맥주소)
	# UUID2 = auto() # MD5 해시 기반 UUID를 생성.
	UUID4 = auto() # 랜덤하게 UUID를 생성. (f47ac10b-58cc-4372-a567-0e02b2c3d479 - 완전랜덤값, 3번쨰부분의 첫숫자는 무조건4, 네번째부분의 첫비트는 고정값)
	# UUID5 = auto() # SHA-1 해시 기반 UUID를 생성.


#--------------------------------------------------------------------------------
# 프로젝트 패스.
#--------------------------------------------------------------------------------
class Path:
	#--------------------------------------------------------------------------------
	# 대상 파일을 기준으로 상위 경로로 거슬러 올라가며 프로젝트 루트 경로 찾기.
	# - rootMarkers를 None으로 두면 일반적으로 루트 디렉터리에 반드시 존재하는 저장소 디렉터리나 셋팅 파일 등을 기준으로 검색.
	# - rootMarkers를 커스텀 할 경우 루트 디렉터리에만 존재하는 독자적인 파일 혹은 디렉터리를 마커로 두고 그 이름을 입력.
	# - start의 경우 검색을 시작할 대상 파일로, 해당 파일의 조상 중에는 반드시 루트 폴더를 식별할 수 있는 이름의 마커가 존재해야함.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetRootPath(start : str, rootMarkers : list[str] = None) -> str:
		current = os.path.abspath(start)
		if os.path.isfile(current):
			current = os.path.dirname(current)
		if not rootMarkers: rootMarkers = ROOTMARKERS
		while True:
			if any(os.path.exists(os.path.join(current, marker)) for marker in rootMarkers):
				return current.replace(BACKSLASH, SLASH)
			parent = os.path.dirname(current)
			if parent == current: break
			current = parent
		raise FileNotFoundError("Project root not found.")
	

	#--------------------------------------------------------------------------------
	# 현재 사용자 전용 데이터 공간 경로 찾기. (윈도우는 사용상 주의!!)
	# - 윈도우 (사용자) : C:\Users\{사용자이름}
	# - 윈도우 (서비스) : C:\WINDOWS\system32\config\systemprofile
	# - 리눅스 : /home/{사용자이름}
	# - 맥OS : /Users/{사용자이름}
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetUserPath() -> str:
		userPath : str = os.path.expanduser(TILDE)
		userPath = userPath.replace(BACKSLASH, SLASH)
		return userPath


	#--------------------------------------------------------------------------------
	# 현재 사용자 전용 애플리케이션 데이터 공간 경로 찾기. (윈도우는 사용상 주의!!)
	# - 윈도우 (사용자) : C:\Users\{사용자이름}\AppData\Local
	# - 윈도우 (서비스) : C:\WINDOWS\system32\config\systemprofile\AppData\Local
	# - 리눅스 : /home/{사용자이름}/.cache
	# - 맥OS : /Users/{사용자이름}/Library/Caches
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetUserCachePath() -> str:
		platformType : PlatformType = GetPlatformType()
		userPath : str = Path.GetUserPath()
		userCachePath : str = str()
		if platformType == PlatformType.WINDOWS:
			userCachePath = os.path.join(userPath, "AppData", "Local").replace(BACKSLASH, SLASH)
		elif platformType == PlatformType.LINUX:
			userCachePath = os.path.join(userPath, ".cache")
		elif platformType == PlatformType.MACOS:
			userCachePath = os.path.join(userPath, "Library", "Caches")
		return userCachePath


	#--------------------------------------------------------------------------------
	# 모든 사용자 공용 데이터 저장 공간 경로 찾기.
	# - 윈도우 : C:\Users\Public
	# - 리눅스 : /usr/local/share
	# - 맥OS : /Users/Shared
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetSharedPath() -> str:
		platformType : PlatformType = GetPlatformType()
		sharedPath : str = str()
		if platformType == PlatformType.WINDOWS:
			sharedPath = os.path.join("C:\\", "Users", "Public").replace(BACKSLASH, SLASH)
		elif platformType == PlatformType.LINUX:
			sharedPath = os.path.join("/", "usr", "local", "share")
		elif platformType == PlatformType.MACOS:
			sharedPath = os.path.join("/", "Users", "Shared")
		return sharedPath


	#--------------------------------------------------------------------------------
	# 애플리케이션 전용 데이터 저장 공간의 경로 찾기.
	# - 뒤에 애플리케이션 등의 고유 이름으로 된 폴더를 만들어서 사용할 것.
	# - 윈도우 : C:\ProgramData
	# - 리눅스 : /var/lib
	# - 맥OS : /Library/Application Support
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetApplicationDataPath() -> str:
		platformType : PlatformType = GetPlatformType()
		applicationDataPath : str = str()
		if platformType == PlatformType.WINDOWS:
			applicationDataPath = os.path.join("C:\\", "ProgramData").replace(BACKSLASH, SLASH)
		elif platformType == PlatformType.LINUX:
			applicationDataPath = os.path.join("/", "var", "lib")
		elif platformType == PlatformType.MACOS:
			applicationDataPath = os.path.join("/", "Library", "Application Support")
		return applicationDataPath


	#--------------------------------------------------------------------------------
	# 애플리케이션 전용 데이터 저장 공간에서의 추가 경로 찾기.
	# - 예를 들어 Path.GetApplicationDataPathWithRelativePath("Users", "계정이름", "MyApplication") 식으로 내 애플리케이션 경로를 입력.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetApplicationDataPathWithRelativePaths(*relativePaths : str) -> str:
		platformType : PlatformType = GetPlatformType()
		applicationDataPath : str = Path.GetApplicationDataPath()
		absolutePath : str = str()
		if platformType == PlatformType.WINDOWS:
			absolutePath = os.path.join(applicationDataPath, *relativePaths).replace(BACKSLASH, SLASH)
		elif platformType == PlatformType.LINUX:
			absolutePath = os.path.join(applicationDataPath, *relativePaths)
		elif platformType == PlatformType.MACOS:
			absolutePath = os.path.join(applicationDataPath, *relativePaths)
		return absolutePath


	#--------------------------------------------------------------------------------
	# 기본경로 + 디렉터리 이름으로 된 새 경로를 만들어서 반환.
	#--------------------------------------------------------------------------------
	@staticmethod
	def CreateDirectory(basePath : str, directoryName : str) -> str:
		path = os.path.join(basePath, directoryName)
		os.makedirs(path, exist_ok = True)
		platformType : PlatformType = GetPlatformType()
		if platformType == PlatformType.WINDOWS:
			return path.replace(BACKSLASH, SLASH)
		else:
			return path
		

	#--------------------------------------------------------------------------------
	# 기본경로 + 무작위 디렉터리 이름으로 된 새 경로를 만들어서 반환.
	# - 디렉터리 이름은 uuid1, uuid4를 기준으로 한 36문자. (하이픈 4개 포함 일 경우)
	#--------------------------------------------------------------------------------
	@staticmethod
	def CreateRandomDirectoryByUUIDType(basePath : str, uuidType : UUIDType = UUIDType.UUID4, useHyphens : bool = False) -> str:
		# 랜덤값 생성.
		randomName : str = str()
		if uuidType == UUIDType.UUID1:
			uuid = uuid1()
		elif uuidType == UUIDType.UUID4:
			uuid = uuid4()

		# 하이픈 사용.
		if useHyphens:
			randomName = str(uuid).replace(HYPHEN, EMPTY)
		else:
			randomName = str(uuid)

		# 디렉터리 생성.
		return Path.CreateDirectory(basePath, randomName)
		

	#--------------------------------------------------------------------------------
	# 파일의 전체경로를 경로, 파일이름으로 분리.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetSplitFilePathToPathFileName(filePath : str) -> tuple[str, str]:
		path, fileName = os.path.split(filePath)
		return fileName
	

	#--------------------------------------------------------------------------------
	# 파일의 전체경로를 경로, 파일이름으로 분리.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetSplitFilePathToPathFileName(filePath : str) -> tuple[str, str]:
		path, fileName = os.path.split(filePath)
		return fileName
	

	#--------------------------------------------------------------------------------
	# 파일의 전체경로를 경로, 이름, 확장자로 분리.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetSplitFilePathToPathNameExtension(filePath : str, useLowerExtension : bool = True) -> tuple[str, str, str]:
		path, fileName = os.path.split(filePath)
		name, extension = os.path.splitext(fileName)
		if useLowerExtension:
			extension = extension.lower()
		return path, name, extension