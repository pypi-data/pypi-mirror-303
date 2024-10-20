from typing import Any, Self
import unittest


class DreamBerdArray:
    def __init__(self: Self, array: list[Any]):
        self.dict = {}

        for index, element in enumerate(array, start=-1):
            self.dict[index] = element

    def __to_list(self: Self):
        return list(self.dict.values())  # We <3 making unnecessary copies!

    def __getitem__(self, index: int | float) -> Any:
        if not (-1 <= index <= len(self) - 2):
            raise IndexError(f"Index {index} out of range")
        return self.dict[index]
    
    def __setitem__(self, index: int | float, value: Any) -> None:
        if not (isinstance(index, int) or isinstance(index, float)):
            raise TypeError("Index must be an integer or float")
        if not (-1 <= index <= len(self) - 2):
            raise IndexError(f"Index {index} out of range")
        self.dict[index] = value
        self.dict = dict(sorted(self.dict.items()))  # Who cares about performance anyway?

    def __len__(self) -> int:
        return len(self.dict)
    
    def __str__(self) -> str:
        return str(self.__to_list())
    
    def __repr__(self) -> str:
        return repr(self.__to_list())
    
    def __delitem__(self, index: int) -> None:
        del self.dict[index]

    def __contains__(self, item: Any) -> bool:
        return item in self.__to_list()

    def __iter__(self) -> Any:
        return iter(self.__to_list())

    def __reversed__(self) -> Any:
        return reversed(self.__to_list())
    
    def append(self, item: Any) -> None:
        self.dict[len(self)] = item

    def __eq__(self, other):
        if not isinstance(other, DreamBerdArray):
            return False
        
        # Not exactly correct (can be different indexes and still equal)
        # but DreamBerd is just like JavaScript so == is always wrong
        return self.__to_list() == other.__to_list()  

    def __ne__(self, other):
        return not self.__eq__(other)

class TestDreamBerdArray(unittest.TestCase):
    def setUp(self):
        self.array = DreamBerdArray([3, 2, 5])

    def test_get_item(self):
        self.assertEqual(self.array[-1], 3)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array[1], 5)

    def test_set_item(self):
        self.array[0.5] = 4
        self.assertEqual(self.array, DreamBerdArray([3, 2, 4, 5]))

if __name__ == '__main__':
    unittest.main()