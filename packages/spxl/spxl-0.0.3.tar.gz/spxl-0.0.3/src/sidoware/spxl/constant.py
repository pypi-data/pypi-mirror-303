#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
from .builtins import Builtins


#--------------------------------------------------------------------------------
# 상수 클래스.
#--------------------------------------------------------------------------------
class Constant:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__constantDictionary : Dict[str, Any]


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__constantDictionary = dict()


	#--------------------------------------------------------------------------------
	# 상수 설정.
	#--------------------------------------------------------------------------------
	def Set(self, constName : str, constValue : Any) -> None:
		constName = constName.upper()
		if constName in self.__constantDictionary: 
			raise ValueError(f"Cannot overwrite constant: {constName}")
		self.__constantDictionary[constName] = constValue


	#--------------------------------------------------------------------------------
	# 상수 반환.
	#--------------------------------------------------------------------------------
	def Get(self, constName : str) -> Any:
		constName = constName.upper()
		if constName not in self.__constantDictionary:
			raise KeyError(f"Constant not found: {constName}")
		return self.__constantDictionary[constName]


	#--------------------------------------------------------------------------------
	# 인스턴스의 멤버 설정.
	#--------------------------------------------------------------------------------
	def __setattr__(self, name : str, value : Any) -> None:
		# 언더바로 시작하는 멤버 변수는 별도로 할당된 추가 멤버 변수 혹은 클래스 내부 멤버 변수로 가정.
		# 일반적인 set 어트리뷰트로 처리.
		if name.startswith("_"):
			base = super()
			base.__setattr__(name, value)
		# 그 외는 상수로 판정.
		else:
			self.Set(name, value)


	#--------------------------------------------------------------------------------
	# 인스턴스의 멤버 제거.
	#--------------------------------------------------------------------------------
	def __delattr__(self, name : str) -> None:
		constName = name.upper()
		if constName in self.__constantDictionary:
			raise TypeError(f"Cannot delete constant: {constName}")
		

# #--------------------------------------------------------------------------------
# # 모듈에 인스턴스를 할당. (수준 있는 꼼수)
# #--------------------------------------------------------------------------------
# moduleName : str = __name__
# sys.modules[moduleName] = Constant()