from enum import IntEnum, auto, Enum


class CodeEnum(Enum):
    """
    word操作类型
    """
    SUCCESS = "SUCCESS"
    REEOR = "REEOR"
    PARAM_ERROR = "PARAM_ERROR"
    INNER_REEOR = "INNER_REEOR"
