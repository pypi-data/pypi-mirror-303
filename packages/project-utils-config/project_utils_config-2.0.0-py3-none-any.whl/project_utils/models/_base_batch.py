import traceback

from typing import TypeVar, Generic, List, Union, Tuple

from project_utils.exception import BaseBatchException
from ._base_model import BaseModel

# 定义泛型
T = TypeVar("T", bound=BaseModel, covariant=True)
DATA_TYPE = Union[List[T], Tuple[T], None]


class BaseBatch(Generic[T]):
    __data: List[T]
    __code: List[str]
    __start: int
    __count: int
    __current: int

    def __init__(self, data: DATA_TYPE = None, skip: bool = False):
        self.__data = []
        self.__code = []
        self.__start = 0
        self.__count = 0
        self.__current = 0
        if data:
            for item in data:
                code: str = item if type(item) == str else item.to_code()
                if code not in self.__code:
                    self.__data.append(item)
                    self.__code.append(code)
                    self.__count += 1
                else:
                    if not skip:
                        raise BaseBatchException(
                            "Source data need remove repeat item.",
                            __file__, 34
                        )

    def to_data(self):
        return [item.to_dict() for item in self.__data]

    def add(self, data: T):
        if data.to_code() in self.__code:
            return -1
        self.__data.append(data)
        self.__code.append(data.to_code())
        self.__count += 1
        return 1

    def add_items(self, data: DATA_TYPE, skip: bool = False):
        if data is None:
            return -1
        for item in data:
            if item.to_code() not in self.__code:
                self.__data.append(item)
                self.__code.append(item.to_code())
                self.__count += 1
            else:
                if not skip:
                    return -1
        return 1

    def remove_from_index(self, index: int):
        if index > self.__count - 1:
            raise BaseBatchException("Element not find!", __file__, 65)
        element: T = self.__data.pop(index)
        self.__code.pop(index)
        self.__count -= 1
        return element

    def remove_from_element(self, element: T):
        try:
            code: str = element.to_code()
            print("t", element.to_dict())
            for item in self.__data:
                print("s", item.to_dict())
            index: int = self.__code.index(code)
        except Exception as e:
            raise BaseBatchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        element: T = self.__data.pop(index)
        self.__code.pop(index)
        self.__count -= 1
        return element

    def clear(self):
        self.__data.clear()
        self.__code.clear()
        self.__start = 0
        self.__count = 0
        self.__current = 0

    def edit(self, index: int, item: T):
        if index > self.__count - 1:
            raise BaseBatchException("Element not find!", __file__, 84)
        self.__data[index] = item
        self.__code[index] = item.to_code()

    def index(self, element: T):
        code: str = element.to_code()
        if code in self.__code:
            return self.__code.index(code)
        else:
            return -1

    def get_from_index(self, index: int):
        if index > self.__count - 1:
            raise BaseBatchException("Element not find!", __file__, 65)
        element: T = self.__data[index]
        return element

    def __iter__(self):
        self.__current = self.__start
        return self

    def __next__(self) -> Tuple[T, str]:
        if self.__current >= self.__count:
            self.__start = 0
            self.__current = 0
            raise StopIteration
        else:
            index: int = self.__current
            self.__current += 1
            return self.__data[index], self.__code[index]

    def __aiter__(self):
        return self.__iter__()

    async def __anext__(self) -> Tuple[T, str]:
        try:
            return self.__next__()
        except StopIteration:
            raise StopAsyncIteration
        except Exception:
            raise Exception

    @classmethod
    def from_data(cls, data: Union[List[dict], Tuple[dict], None], element_type: T = BaseModel, skip: bool = True):
        if data is None:
            return cls(data, skip=skip)
        else:
            result: List[T] = []
            for item in data:
                element: T = element_type.from_dict(**item)
                result.append(element, )
            return cls(result, skip=skip)

    @property
    def data(self):
        return self.__data

    @property
    def count(self):
        return self.__count
