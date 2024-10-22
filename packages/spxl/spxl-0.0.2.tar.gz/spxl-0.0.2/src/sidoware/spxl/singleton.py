#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
from .builtins import Builtins


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
# 싱글톤 익셉션.
#--------------------------------------------------------------------------------
class SingletonException(Exception):
	"""싱글톤 인스턴스를 외부에서 직접 생성하려고 할 때 발생하는 예외."""
	pass


#--------------------------------------------------------------------------------
# 싱글톤 클래스.
# - 이 클래스를 상속 받은 클래스는 외부에서 생성자를 호출해서 할당하려고 하면 예외가 발생한다.
# - DerivedClass(Singleton): pass
# - DerivedClass.GetInstance() # OK
# - newInstance = DerivedClass() # ERROR : SingletonException
#--------------------------------------------------------------------------------
T = TypeVar("T", bound = "Singleton")
class Singleton():
	#--------------------------------------------------------------------------------
	# 클래스 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__Instance : Optional[T] = None
	__IsLocked : bool = True


	#--------------------------------------------------------------------------------
	# 인스턴스 할당.
	#--------------------------------------------------------------------------------
	def __new__(classType) -> Any:
		if classType.__IsLocked:
			raise SingletonException()
		classType.__Instance = super(Singleton, classType).__new__(classType)
		return classType.__Instance


	#--------------------------------------------------------------------------------
	# 인스턴스 반환.
	# - 없으면 생성해서 반환.
	#--------------------------------------------------------------------------------
	@classmethod
	def GetInstance(classType : Type[T]) -> T:
		if not classType.__Instance:
			classType.__IsLocked = False
			classType.__Instance = classType()
			classType.__IsLocked = True
		return classType.__Instance