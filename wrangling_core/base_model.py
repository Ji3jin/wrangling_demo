# *-* encoding=utf-8 *-*
from enum import Enum, unique


@unique
class DataType(Enum):
    NUM = 'data_type_num'
    FLOAT = 'data_type_float'
    STRING = 'data_type_string'
    DATETIME = 'data_type_datetime'


@unique
class ObjType(Enum):
    ROW = 0
    COLUMN = 1
    CELL = 2


CHECK_TYPE = ((DataType.NUM,'int64'), (DataType.FLOAT,'float64'))
