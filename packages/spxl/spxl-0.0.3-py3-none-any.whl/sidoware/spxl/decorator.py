#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import inspect
from functools import wraps
from .builtins import Builtins



#--------------------------------------------------------------------------------
# 비공개 메서드를 위한 오버라이드 메서드 데코레이터 (인스턴스메서드 전용).
# - 동일 이름의 자식이 있으면 자식을 호출.
# - 동일 이름의 자식이 없으면 자신을 호출.
#--------------------------------------------------------------------------------
def overridemethod(targetMethod : Callable[..., Any]):
	@wraps(targetMethod)
	def Decorate(self, *args, **kwargs) -> Any:
		# 인자 없음 - 일반 함수 혹은 스태틱메서드 일 경우.
		if not args: return targetMethod(*args, **kwargs)

		argument = args[0]

		# 인자 있음 - 하지만 현재 호출한 메서드의 인스턴스나 현재 호출한 메서드의 클래스가 아닐 경우.
		# if not isinstance(argument, type) and not isinstance(argument, self.__class__): return targetMethod(*args, **kwargs)
		if not Builtins.IsInstanceInTypes(argument, [type, self.__class__]): return targetMethod(*args, **kwargs)

		# 첫번째 인자가 클래스 타입 일 경우 or 인스턴스 일 경우.
		isClassMethod = Builtins.IsType(argument, type)
		if isClassMethod:
			classType = args[0]
		else:
			classType = args[0].__class__
	
		# 메서드 이름 룰이 비공개 메서드 일 경우 or 공개 메서드 일 경우.
		methodName = targetMethod.__name__
		isPrivateMethod = methodName.startswith("__") and not methodName.endswith("__")
		if isPrivateMethod:
			methodName = methodName.split("__", 1)[-1]
			methodName = f"_{classType.__name__}__{methodName}"

		# 자식 에게 동일 이름의 함수가 있다면 호출.
		if Builtins.HasAttribute(classType, methodName):
			childMethod = Builtins.GetAttribute(classType, methodName)
			if childMethod is not targetMethod:
				return childMethod(*args, **kwargs)
			
		# 없으면 자신의 함수 호출.
		return targetMethod(*args, **kwargs)
	return Decorate


#--------------------------------------------------------------------------------
# 자식의 메소드가 오버라이드 한 것일 때 부모의 동일한 메소드를 대신 호출 해주는 함수.
#--------------------------------------------------------------------------------
def basemethod(self, *args, **kwargs) -> Any:
	currentFrame = inspect.currentframe()
	previouslyFrame = inspect.getouterframes(currentFrame)[1]
	methodName = previouslyFrame.function
	parentClass = self.__class__.__bases__[0]

	# 비공개 메서드 이름 장식 처리
	isPrivateMethod = methodName.startswith("__") and not methodName.endswith("__")
	if isPrivateMethod:
		methodName = methodName.split("__", 1)[-1]
		methodName = f"_{parentClass.__name__}__{methodName}"

	# 부모 클래스의 메서드를 가져와 호출
	if hasattr(parentClass, methodName):
		parentMethod = getattr(parentClass, methodName)
		return parentMethod(self, *args, **kwargs)
	else:
		raise AttributeError(f"{parentClass.__name__} object has no attribute {methodName}")
