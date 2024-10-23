# encoding=utf-8

import sys

def is_python3():
    py_version = sys.version_info[0]
    if str(py_version) == '3':
        return True
    
    return False

def is_python2():
    py_version = sys.version_info[0]
    if str(py_version) == '2':
        return True
    
    return False

# 数据安全处理，防止因为格式异常出现程序错误
def safe_list(item):
    safe_list = lambda x: x if isinstance(x, list) else []
    return safe_list(item)

# data filter
def obj_null_filter(obj, cls):
    filter_rule = lambda x: x if isinstance(x, cls) else None
    return filter_rule(obj)

def str_null_filter(str):
    filter_rule = lambda x : x if isinstance(x, str) else ''
    return filter(str)

# data type check
def check_cls(obj, cls):
    check_rule = lambda x: True if isinstance(x, cls) else False
    return check_rule(obj)