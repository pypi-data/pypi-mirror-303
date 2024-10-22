#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
# from __future__ import annotations
# from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
# import builtins
# import os
# from uuid import uuid1, uuid4
# from enum import Enum, auto
# import inspect
# from functools import wraps
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import pkgutil
from .anonymousclass import AnonymousObject, UnnamedClass
from .baseclass import BaseClass
from .basemetaclass import BaseMetaClass
from .baserepository import BaseRepository
from .builtins import Builtins
from .constant import Constant
from .decorator import overridemethod, basemethod
from .enumflag import EnumFlag
from .environment import PlatformType, GetPlatformType
from .node import NodeEventType, Node
from .path import Path
from .sharedclass import SharedClass
from .singleton import Singleton, SingletonException


#--------------------------------------------------------------------------------
# 다른 sidoware 패키지와 네임스페이스 공유.
#--------------------------------------------------------------------------------
__path__ = pkgutil.extend_path(__path__, __name__)


#--------------------------------------------------------------------------------
# 패키지 안의 클래스 별칭 목록.
#--------------------------------------------------------------------------------
from .baseclass import BaseClass as Object
from .basemetaclass import BaseMetaClass as MetaClass
from .basemetaclass import BaseMetaClass as Meta
from .baserepository import BaseRepository as Repository


# #--------------------------------------------------------------------------------
# # 공개 인터페이스 목록.
# #--------------------------------------------------------------------------------
# __all__ = [
# 	#--------------------------------------------------------------------------------
# 	# anonymousclass.
# 	"AnonymousObject",
# 	"UnnamedClass",

# 	#--------------------------------------------------------------------------------
# 	# baseclass.
# 	"BaseClass",
# 	"Object",

# 	#--------------------------------------------------------------------------------
# 	# basemetaclass.
# 	"BaseMetaClass",
# 	"MetaClass",
# 	"Meta",

# 	#--------------------------------------------------------------------------------
# 	# baserepository.
# 	"BaseRepository",
# 	"Repository",
	
# 	#--------------------------------------------------------------------------------
# 	# builtins.
# 	"Builtins",

# 	#--------------------------------------------------------------------------------
# 	# constant.
# 	"Constant",

# 	#--------------------------------------------------------------------------------
# 	# decorator.
# 	"overridemethod",
# 	"basemethod",

# 	#--------------------------------------------------------------------------------
# 	# enumflag.
# 	"EnumFlag",

# 	#--------------------------------------------------------------------------------
# 	# environment.
# 	"PlatformType",
# 	"GetPlatformType",

# 	#--------------------------------------------------------------------------------
# 	# node.
# 	"NodeEventType",
# 	"Node",

# 	#--------------------------------------------------------------------------------
# 	# path.
# 	"Path",

# 	#--------------------------------------------------------------------------------
# 	# sharedclass.
# 	"SharedClass",

# 	#--------------------------------------------------------------------------------
# 	# singleton.
# 	"Singleton",
# 	"SingletonException"
# ]