#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
from .builtins import Builtins
from .baseclass import BaseClass as Object
from .basemetaclass import BaseMetaClass as Meta


#--------------------------------------------------------------------------------
# 공유 클래스의 메타클래스 (클래스 타입 클래스).
#--------------------------------------------------------------------------------
class MetaClass(Meta):
	#--------------------------------------------------------------------------------
	# 클래스 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__Instances : Dict[Type[MetaClass], SharedClass] = dict()


	#--------------------------------------------------------------------------------
	# 인스턴스 할당 요청 됨(생성자 호출됨).
	#--------------------------------------------------------------------------------
	def __call__(classType, *args: Any, **kwds: Any) -> Any:
		if classType in classType.__Instances:
			instance = classType.__Instances[classType]
			return instance
		else:
			instance = super().__call__(*args, **kwds)
			classType.__Instances[classType] = instance

			
#--------------------------------------------------------------------------------
# 공유 클래스 (싱글톤 클래스).
# - 어디서 생성해도 항상 같은 인스턴스를 반환.
# - class ChildClass(SharedClass): pass
# - value1 = ChildClass()
# - value2 = ChildClass()
# - value1 == value2
#--------------------------------------------------------------------------------
T = TypeVar("T", bound = "SharedClass")
class SharedClass(Object, metaclass = MetaClass):
	#--------------------------------------------------------------------------------
	# 인스턴스 반환.
	# - 없으면 생성해서 반환.
	#--------------------------------------------------------------------------------
	@classmethod
	def GetSharedInstance(classType : Type[T]) -> T:
		return classType()