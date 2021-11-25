from typing import TypeVar, Generic, List, Optional
from structures.common.error import Error

Type = TypeVar('Type')


class Queue(Generic[Type]):
  """
  Queue implementation based
  on built-in  array.

  Methods:
    - push(e)
    - pop()
    - first()
    - isEmpty()
    - isFull()
    - len()
  """

  _data: List[Type] = []
  _size = 0
  DEFAULT_CAPACITY = 10

  _max_size: Optional[int]
  _is_fixed_size: bool = False

  _first_element_index: int = 0


  def __init__(self, max_size: Optional[int] = None):
    if max_size is not None:
      self._max_size = max_size
      self._is_fixed_size = True

    self._data = [None] * (max_size or self.DEFAULT_CAPACITY)


  def push(self, element: Type):
    if self.is_full():
      raise Error('[Queue] Queue is full, maybe you should not use fixed size.')

    if not self._is_fixed_size and self._size == len(self._data):
      self._resize_data_capacity(len(self._data) * 2)
      pass

    insert_index = (self._first_element_index + self._size) % len(self._data)
    self._data[insert_index] = element
    self._size += 1


  def pop(self) -> Optional[Type]:
    if self.is_empty():
      return None

    first_element = self._data[self._first_element_index]
    self._data[self._first_element_index] = None
    self._first_element_index = (self._first_element_index + 1) % len(self._data)
    self._size -= 1

    if not self._is_fixed_size and 0 < self._size < len(self._data) // 4:
      self._resize_data_capacity(
        len(self._data) * 2
      )

    return first_element


  def first(self) -> Optional[Type]:
    if self.is_empty():
      return None
    return self._data[self._first_element_index]


  def is_full(self) -> bool:
    if not self._is_fixed_size:
      return False
    return self._size == self._max_size


  def is_empty(self) -> bool:
    return self._size == 0


  def _resize_data_capacity(self, new_capacity: int):
    pass



if __name__ == '__main__':
  queue: Queue[int] = Queue()

  queue.push(1)
  queue.push(2)
  queue.push(3)
  queue.push(4)
  queue.push(5)
  queue.push(6)

  queue.pop()
  queue.pop()
  queue.pop()

  queue.push(7)
  queue.push(8)
  queue.push(9)
  queue.push(10)
  queue.push(11)
  queue.push(12)

  print(f'Queue: {queue._data}')
