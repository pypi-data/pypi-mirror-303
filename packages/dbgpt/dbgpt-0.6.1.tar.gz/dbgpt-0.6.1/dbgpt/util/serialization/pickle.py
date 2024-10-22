import inspect
import traceback
import weakref
from types import FunctionType, MethodType, ModuleType

import cloudpickle


def check_serializable(obj, obj_name="Object"):
    result = _do_check_serializable(obj, obj_name)
    if result:
        raise ValueError(result)
