#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Iterator, Optional, Sequence, Type, TypeVar, Union, Tuple, Any, List, Dict, Set, cast, overload
from enum import Enum
from .builtins import Builtins
from .baseclass import BaseClass as Object


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
EMPTY : str = ""


#--------------------------------------------------------------------------------
# 타입 별칭 정의 목록.
#--------------------------------------------------------------------------------
NodeEventFunction = Callable[..., Any] # function은 3.10에 존재하지 않음.


#--------------------------------------------------------------------------------
# 노드 이벤트 타입.
#--------------------------------------------------------------------------------
class NodeEventType(Enum):
	CREATEEVENT = "__OnCreateEvent" # callable[[None], None]
	DESTROYEVENT = "__OnDestroyEvent" # callable[[None], None]
	PARENTCHANGEEVENT = "__OnParentChangeEvent" # callable[[Node, Node], None]
	SIBLINGCHANGEEVENT = "__OnSiblingChangeEvent" # callable[[Node], None]
	CHILDCHANGEEVENT = "__OnChildChangeEvent" # callable[[Node], None]


#--------------------------------------------------------------------------------
# 노드 클래스.
#--------------------------------------------------------------------------------
class Node(Object):
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__parent : Node
	__children : list[Node]
	__isAlive : bool
	__events : dict[NodeEventType, set[NodeEventFunction]]


	#--------------------------------------------------------------------------------
	# 부모 프로퍼티 반환.
	#--------------------------------------------------------------------------------
	@property
	def Parent(self) -> Node:
		return self.__parent


	#--------------------------------------------------------------------------------
	# 부모 프로퍼티 설정.
	#--------------------------------------------------------------------------------
	@Parent.setter
	def Parent(self, parent : Node) -> None:
		if self.__parent is not parent:

			# 부모 변경 이벤트.
			self.NotifyEvent(NodeEventType.PARENTCHANGEEVENT, self.__parent, parent)
			if self.__parent:
				self.__parent.RemoveChild(self)
			self.__parent = parent
			if self.__parent:
				self.__parent.AddChild(self)


	#--------------------------------------------------------------------------------
	# 자식 프로퍼티 반환. (신규 리스트 생성 후 얕은 복사로 반환되므로 수정 불가)
	#--------------------------------------------------------------------------------
	@property
	def Children(self) -> list[Node]:
		return list(self.__children)
	

	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self, name : str, value : Any = None) -> None:
		base = super()
		base.__init__()
		
		self.Name = name
		self.Value = value
		self.__parent = None
		self.__children = list()
		self.__events = dict()
		self.__isAlive = True

		# 이벤트 목록 초기화.
		for nodeEventType in NodeEventType:
			self.__events[nodeEventType] = set()
		self.__events[NodeEventType.CREATEEVENT].add(self.__OnCreateEvent)
		self.__events[NodeEventType.DESTROYEVENT].add(self.__OnDestroyEvent)
		self.__events[NodeEventType.PARENTCHANGEEVENT].add(self.__OnParentChangeEvent)
		self.__events[NodeEventType.SIBLINGCHANGEEVENT].add(self.__OnSiblingChangeEvent)
		self.__events[NodeEventType.CHILDCHANGEEVENT].add(self.__OnChildChangeEvent)

		# 생성 이벤트.
		self.NotifyEvent(NodeEventType.CREATEEVENT)

	#--------------------------------------------------------------------------------
	# 파괴됨.
	#--------------------------------------------------------------------------------
	def __del__(self) -> None:
		base = super()
		base.__del__()
		

	#--------------------------------------------------------------------------------
	# 자식 추가.
	#--------------------------------------------------------------------------------
	def AddChild(self, child : Node) -> None:
		if child in self.__children:
			return
		
		self.__children.append(child)
		child.__parent = self

		# 자식 변경 이벤트.
		self.NotifyEvent(NodeEventType.CHILDCHANGEEVENT, child)


	#--------------------------------------------------------------------------------
	# 자식 제거.
	#--------------------------------------------------------------------------------
	def RemoveChild(self, child : Node) -> None:
		if child not in self.__children:
			return
		
		self.__children.remove(child)
		child.__parent = None

		# 자식 변경 이벤트.
		self.NotifyEvent(NodeEventType.CHILDCHANGEEVENT, child)


	#--------------------------------------------------------------------------------
	# 형제 노드 순서 설정.
	#--------------------------------------------------------------------------------
	def SetSiblingByIndex(self, index : int, newSibling : Node) -> None:
		siblings = self.GetSiblings()
		if index < 0 or index >= len(siblings):
			raise IndexError("Sibling index out of range.")
		self.__parent.__children[self.__parent.__children.index(siblings[index])] = newSibling
		newSibling.Parent = self.__parent

		# 형제 변경 이벤트.
		self.NotifyEvent(NodeEventType.SIBLINGCHANGEEVENT, newSibling)


	#--------------------------------------------------------------------------------
	# 형제 목록 반환.
	#--------------------------------------------------------------------------------
	def GetSiblings(self) -> list[Node]:
		if self.__parent is None:
			return list()
		return [child for child in self.__parent.Children if child != self]


	#--------------------------------------------------------------------------------
	# 순서에 대한 형제 노드 반환
	#--------------------------------------------------------------------------------
	def GetSiblingByIndex(self, index : int) -> Node:
		siblings = self.GetSiblings()
		if index < 0 or index >= len(siblings):
			raise IndexError("Sibling index out of range.")
		return siblings[index]


	#--------------------------------------------------------------------------------
	# 조상 노드 찾기.
	#--------------------------------------------------------------------------------
	def FindAncestor(self, path : str) -> Node:
		parts = path.split("/")
		current : Node = self
		for part in reversed(parts):
			if part == ".":
				continue
			if current is None or current.Name != part:
				return None
			current = current.Parent
		return current


	#--------------------------------------------------------------------------------
	# 형제 노드 찾기.
	#--------------------------------------------------------------------------------
	def FindSibling(self, name : str) -> Node:
		for sibling in self.GetSiblings():
			if sibling.Name == name:
				return sibling
		return None


	#--------------------------------------------------------------------------------
	# 자손 노드 찾기.
	#--------------------------------------------------------------------------------
	def FindDescendant(self, path : str) -> Node:
		parts : list[str] = path.split("/")
		current : Node = self
		for part in parts:
			if part == ".":
				continue
			found = False
			for child in current.Children:
				if child.Name == part:
					current = child
					found = True
					break
			if not found:
				return None
		return current


	#--------------------------------------------------------------------------------
	# 복제.
	#--------------------------------------------------------------------------------
	def Clone(self) -> Node:
		clonedNode = Node(self.Name, self.Value)
		for child in self.Children:
			clonedChild = child.Clone()
			clonedNode.AddChild(clonedChild)
		return clonedNode


	#--------------------------------------------------------------------------------
	# 파괴.
	#--------------------------------------------------------------------------------
	def Destroy(self, ) -> None:
		if self.__isAlive:
			return
		self.__isAlive = False

		self.NotifyEvent(NodeEventType.DESTROYEVENT)
		for child in list(self.__children):
			child.Destroy()
		if self.__parent:
			self.__parent.RemoveChild(self)
			self.__parent = None
		self.__children.clear()


	#--------------------------------------------------------------------------------
	# 노드가 생성됨.
	#--------------------------------------------------------------------------------
	def __OnCreateEvent(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 노드가 파괴됨.
	#--------------------------------------------------------------------------------
	def __OnDestroyEvent(self) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 부모 노드가 변경됨.
	#--------------------------------------------------------------------------------
	def __OnParentChangeEvent(self, previouslyParentNode : Node, nextParentNode : Node) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 형제 노드가 변경됨.
	#--------------------------------------------------------------------------------
	def __OnSiblingChangeEvent(self, siblingNode : Node) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 자식 노드가 변경됨.
	#--------------------------------------------------------------------------------
	def __OnChildChangeEvent(self, childNode : Node) -> None:
		pass


	#--------------------------------------------------------------------------------
	# 이벤트 통지.
	#--------------------------------------------------------------------------------
	def NotifyEvent(self, nodeEventType : str, *args, **kwargs) -> None:
		for callback in self.__events[nodeEventType]:
			if not callback:
				continue
			callback(*args, **kwargs)


	#--------------------------------------------------------------------------------
	# 전체 이벤트 초기화.
	# - 전체를 초기화하지만 함수 목록 객체 자체를 삭제하진 않는다.
	#--------------------------------------------------------------------------------
	def ClearAllEvents(self) -> None:
		for nodeEventType, callbacks in self.__events.items():
			callbacks.clear()


	#--------------------------------------------------------------------------------
	# 이벤트 초기화.
	#--------------------------------------------------------------------------------
	def ClearEvent(self, nodeEventType : NodeEventType) -> None:
		callbacks = self.__events[nodeEventType]
		callbacks.clear()


	#--------------------------------------------------------------------------------
	# 이벤트 재설정.
	#--------------------------------------------------------------------------------
	def SetEvent(self, nodeEventType : NodeEventType, nodeEvent : NodeEventFunction) -> None:
		events = self.__events[nodeEventType]
		events.clear()
		events.update(nodeEvent)


	#--------------------------------------------------------------------------------
	# 이벤트 추가.
	#--------------------------------------------------------------------------------
	def AddEvent(self, nodeEventType : NodeEventType, nodeEvent : NodeEventFunction) -> None:
		events = self.__events[nodeEventType]
		if nodeEvent not in events:
			events.update(nodeEvent)


	#--------------------------------------------------------------------------------
	# 이벤트 제거.
	#--------------------------------------------------------------------------------
	def RemoveEvent(self, nodeEventType : NodeEventType, nodeEvent : NodeEventFunction) -> None:
		events = self.__events[nodeEventType]
		events.discard(nodeEvent)


	#--------------------------------------------------------------------------------
	# 반복문 순회.
	#--------------------------------------------------------------------------------
	def __iter__(self) -> Iterator:
		yield self
		for child in self.__children:
			yield from iter(child)


	#--------------------------------------------------------------------------------
	# 다른 노드의 구조를 복제.
	#--------------------------------------------------------------------------------
	def CopyStructure(self, otherNode : Node) -> None:
		self.Name = otherNode.Name
		self.Value = otherNode.Value
		for child in otherNode.Children:
			newChild = Node(child.Name, child.Value)
			self.AddChild(newChild)
			newChild.CopyStructure(child)


	#--------------------------------------------------------------------------------
	# 문자열 변환.
	#--------------------------------------------------------------------------------
	def __repr__(self) -> str:
		return f"Node(Name={self.Name}, Value={self.Value})"