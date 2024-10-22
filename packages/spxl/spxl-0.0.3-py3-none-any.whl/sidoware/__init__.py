#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
import pkgutil
import sys
# import builtins
# import os
# from uuid import uuid1, uuid4
# import inspect
# from functools import wraps


#--------------------------------------------------------------------------------
# 다른 sidoware 를 루트로 삼는 패키지와 네임스페이스 공유.
#--------------------------------------------------------------------------------
__path__ = pkgutil.extend_path(__path__, __name__)


#--------------------------------------------------------------------------------
# 패키지 안의 클래스 별칭 목록.
#--------------------------------------------------------------------------------
# from .spxl.common import *
# from .spxl.core import *
# from .spxl.managers import *
from .spxl import AnonymousObject, UnnamedClass
from .spxl import BaseClass, Object
from .spxl import BaseMetaClass, MetaClass, Meta
from .spxl import BaseRepository, Repository
from .spxl import Builtins
from .spxl import Constant
from .spxl import overridemethod, basemethod
from .spxl import EnumFlag, auto
from .spxl import PlatformType, GetPlatformType
from .spxl import NodeEventType, Node
from .spxl import Path
from .spxl import SharedClass
from .spxl import Singleton, SingletonException
