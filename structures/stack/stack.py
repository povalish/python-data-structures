from typing import TypeVar, Generic, List, Optional
from structures.common.error import Error

Type = TypeVar('Type')


class Stack(Generic[Type]):
  """
  Stack implementation based
  on built-in dynamic array.

  Methods:
    - push(e)
    - pop()
    - top()
    - isEmpty()
    - isFull()
    - len()
  """

  _data: List[Type] = []

  _max_size: Optional[int] = None
  _actual_size: int = 0

  _is_fixed_size: bool = False


  def __init__(self, max_size: Optional[int] = None):
    if max_size:
      self._max_size = max_size
      self._is_fixed_size = True
      self._data = [None] * max_size


  def push(self, e: Type):
    if self._is_fixed_size:
      if self.is_full():
        raise Error(f'[Stack] Can not push {repr(e)}. Stack is overflowed')
      self._data[self._actual_size] = e
    else:
      self._data.append(e)

    self._actual_size += 1


  def pop(self) -> Type:
    if self.is_empty():
      raise Error('[Stack] Can not pop element. Stack is empty.')

    if self._is_fixed_size:
      last_index = self._actual_size - 1
      last_element = self._data[last_index]

      self._data[last_index] = None
      self._actual_size -= 1

      return last_element

    last_element = self._data.pop()
    self._actual_size -= 1

    return last_element


  def top(self) -> Type:
    if self.is_empty():
      raise Error('[Stack] Can not get top element. Stack is empty.')

    return self._data[-1]


  def is_full(self) -> bool:
    if not self._is_fixed_size:
      return False
    else:
      return self._actual_size == self._max_size


  def is_empty(self) -> bool:
    return self._actual_size == 0


  def __len__(self):
    return self._actual_size



if __name__ == '__main__':
  stack = Stack(10)

  stack.push(1)
  stack.push(2)
  stack.push(3)

  popped = stack.pop()

  print(f'Popped {popped}')
