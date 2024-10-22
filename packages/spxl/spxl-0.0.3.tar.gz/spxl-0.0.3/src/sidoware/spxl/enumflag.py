#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
import builtins
from enum import Flag, auto


#--------------------------------------------------------------------------------
# 열거체 플래그.
# - 선언 : flags : InheritedEnumFlag = InheritedEnumFlag.A
# - 추가 : flags |= InheritedEnumFlag.B
# - 제거 : flags &= ~InheritedEnumFlag.A
# - 포함 여부 : if InheritedEnumFlag.A in flags:
# - 포함 여부 : if flags & InheritedEnumFlag.A:
# - 조합 비교 : if flags == flags:
# - 전체 제거 : flags = InheritedEnumFlag(0)
# - 특정 플래그만 남기고 전체 제거 : flags &= InheritedEnumFlag.A
# - 미포함 목록 얻기 : unflags = ~flags
#--------------------------------------------------------------------------------
T = TypeVar("T", bound = "EnumFlag")
class EnumFlag(Flag):
    #--------------------------------------------------------------------------------
    # auto() 처리가 거듭제곱이 되도록 확장.
    #--------------------------------------------------------------------------------
    def _generate_next_value_(name, start : int, count : int, last_values : list[Any]) -> int:
        return 1 << count
    

    #--------------------------------------------------------------------------------
    # 없음.
    #--------------------------------------------------------------------------------
    @classmethod
    def Nothing(classType : Type[T]) -> T:
        return classType(0)


    #--------------------------------------------------------------------------------
    # 전부.
    #--------------------------------------------------------------------------------
    @classmethod
    def Everything(classType : Type[T]) -> T:
        return classType(~0)