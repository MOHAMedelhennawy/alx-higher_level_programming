#!/usr/bin/python3
"""MyInt inhertid from int class"""


class MyInt(int):
    """Write a class MyInt that inherits from int"""

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
