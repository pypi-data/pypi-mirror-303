#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
BASE : str = "base"


#--------------------------------------------------------------------------------
# 빌트인 확장 클래스.
# - 파이썬의 기본 시스템 내장 함수들은 빌트인 모듈로 접근하여 사용 가능.
# - bultins.print()와 print()은 동일 함수.
# - hasattr, getattr, setattr, delattr, vars, dir.
#--------------------------------------------------------------------------------
class Builtins:
	#--------------------------------------------------------------------------------
	# 출력.
	#--------------------------------------------------------------------------------
	@staticmethod
	def Print(*values : str) -> None:
		builtins.print(*values)


	#--------------------------------------------------------------------------------
	# 대상이 타입 인스턴스인지 여부 반환.
	# - instance = Hello()
	# - instance : 인스턴스
	# - instance.__class__ : 인스턴스의 클래스 타입 (class Hello)
	# - instance.__class__ == Hello : 동일
	#
	# - instance.__class__.__class__ : 클래스의 클래스 타입 (class type)
	# - instance.__class__.__class__ == type : 동일
	# - 타입은 "클래스의 메타클래스"로서 클래스는 타입의 인스턴스라고 할 수 있다.
	# - instance < class < type
	# - instance는 type과 직접적인 관련이 없기 때문에 같지 않다.
	#--------------------------------------------------------------------------------
	@staticmethod
	def IsType(obj : object) -> bool:
		if not builtins.isinstance(obj, builtins.type):
			return False
		return True


	#--------------------------------------------------------------------------------
	# 대상이 클래스 타입에 해당하는 인스턴스인지 여부 반환.
	#--------------------------------------------------------------------------------
	@staticmethod
	def IsInstanceType(obj : object, classType : Type) -> bool:
		if not builtins.isinstance(obj, classType):
			return False
		return True


	#--------------------------------------------------------------------------------
	# 대상이 클래스 타입 목록 중 하나에 해당하는 인스턴스인지 여부 반환.
	#--------------------------------------------------------------------------------
	@staticmethod
	def IsInstanceInTypes(obj : object, classTypes : List[Type]) -> bool:
		if not builtins.isinstance(obj, tuple(classTypes)):
			return False
		return True


	#--------------------------------------------------------------------------------
	# 실제 어트리뷰트 이름 반환.
	# - 존재한다면 실제 어트리뷰트 이름을 반환. (입력값과 동일할 수도 다를 수도 있음)
	# - 존재하지 않으면 빈문자열 반환.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetRealAttributeName(obj : object, attributeName : str) -> str:
		if not obj:
			return str()
		if not attributeName:
			return str()
		attributeNameLower : str = attributeName.lower()
		for realAttributeName in builtins.dir(obj):
			realAttributeNameLower : str = realAttributeName.lower()
			if attributeNameLower == realAttributeNameLower:
				return realAttributeName				
		return str()


	#--------------------------------------------------------------------------------
	# 어트리뷰트 설정. (혹은 생성)
	#--------------------------------------------------------------------------------
	@staticmethod
	def SetAttribute(obj : object, attributeName : str, value : Any, allowCreation : bool = True) -> bool:
		realAttributeName = Builtins.GetRealAttributeName(obj, attributeName)
		if realAttributeName:
			builtins.setattr(obj, attributeName, value)
			return True
		elif allowCreation:
			builtins.setattr(obj, attributeName, value)
			return True
		else:
			return False


	#--------------------------------------------------------------------------------
	# 어트리뷰트 제거.
	#--------------------------------------------------------------------------------
	@staticmethod
	def DeleteAttribute(obj : object, attributeName : str) -> bool:
		realAttributeName = Builtins.GetRealAttributeName(obj, attributeName)
		if not realAttributeName:
			return False
		
		builtins.delattr(realAttributeName)
		return True


	#--------------------------------------------------------------------------------
	# 어트리뷰트 반환.
	#--------------------------------------------------------------------------------
	@staticmethod
	def GetAttribute(obj : object, attributeName : str, defaultValue : Any = None) -> Any:
		if not obj:
			return defaultValue
		if not attributeName:
			return defaultValue
		realAttributeName : str = Builtins.GetRealAttributeName(obj, attributeName)
		if not realAttributeName:
			return defaultValue
		return builtins.getattr(obj, realAttributeName)


	#--------------------------------------------------------------------------------
	# 어트리뷰트의 존재 유무 판단.
	#--------------------------------------------------------------------------------
	@staticmethod
	def HasAttribute(obj : object, attributeName : str) -> bool:
		if not obj:
			return False
		if not attributeName:
			return False
		realAttributeName : str = Builtins.GetRealAttributeName(obj, attributeName)
		if not realAttributeName:
			return False
		return True