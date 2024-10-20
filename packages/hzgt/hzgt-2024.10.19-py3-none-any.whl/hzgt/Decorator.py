# -*- coding: utf-8 -*-

import datetime
import time
import inspect
import logging
import os
from functools import wraps


def vargs(valid_params: dict):
    """
    根据其有效集合验证函数参数

    >>> from hzgt import vargs
    >>> @vargs({'mode': {'read', 'write', 'append'}, 'type': {'text', 'binary'}, 'u': [1, 2, 3]})
    >>> def process_data(mode, type, u="1"):
    ...      print(f"Processing data in {mode} mode and {type} type, {u}")
    >>> process_data(mode='read', type='text')  # 正常执行
    >>> # process_data(mode='delete', type='binary')  # 抛出ValueError
    >>> # process_data(mode='read', type='image')  # 抛出ValueError
    >>> process_data(mode="read", type="text", u="2")


    :param valid_params: dict: 键为 arg/kargs 名称，值为 有效值的集合/列表

    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数的参数名称
            func_args = func.__code__.co_varnames[:func.__code__.co_argcount]

            # 验证位置参数
            for i, arg in enumerate(args):
                if func_args[i] in valid_params and arg not in valid_params[func_args[i]]:
                    raise ValueError(
                        f"值 '{func_args[i]} = {arg}' 无效: 有效集合为: {valid_params[func_args[i]]}")

            # 验证关键字参数
            for param_name, valid_set in valid_params.items():
                if param_name in kwargs and kwargs[param_name] not in valid_set:
                    raise ValueError(
                        f"值 '{param_name} = {kwargs[param_name]}' 无效: 有效集合为: {valid_set}")

            return func(*args, **kwargs)

        return wrapper

    return decorator



def gettime(func):
    """
    使用方法：装饰器

    在需要显示运算时间的函数前加@gettime

    :param func:
    :return: None
    """
    from .strop import restrop_list
    @wraps(func)
    def get(*args, **kwargs):
        start = datetime.datetime.now()
        starttime = time.time()
        print(restrop_list(["=== ",
                            "开始时间 ", start.strftime('%Y-%m-%d  %H:%M:%S'),
                            "     %s.%s()" % (func.__module__, func.__name__),
                            ],
                           [1,
                            -1, 3,
                            5,
                            ])
              )

        _result = func(*args, **kwargs)  # func

        end = datetime.datetime.now()
        spentedtime = time.time() - starttime
        print(restrop_list(["=== ",
                            "结束时间 ", end.strftime('%Y-%m-%d  %H:%M:%S'),
                            "     总耗时 ", f"{spentedtime:.2f}", " s"
                            ],
                           [1,
                            -1, 4,
                            -1, 5, -1
                            ])
              )
        return _result

    return get


@vargs({"loglevel": {"debug", "info", "warning", "error", "critical"}})
def timelog(loglevel="debug", encoding="utf-8"):
    """
        使用方法：装饰器

    在需要日志的函数前加 @timelog()

    loglevel
        * "debug": logging.DEBUG,
        * "info": logging.INFO,
        * "warning": logging.WARNING,
        * "error": logging.ERROR,
        * "critical": logging.CRITICAL

    :param loglevel: str 日志等级

    :return: None
    """

    LOG_LEVEL = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def timelog(func):
        def RetrieveName():
            stacks = inspect.stack()  # 获取函数调用链
            return stacks[-1].filename, stacks[-1].lineno

        logger = logging.getLogger(__name__)
        logger.setLevel(LOG_LEVEL[loglevel])
        rten = RetrieveName()
        formatter = logging.Formatter(f"%(asctime)s - [{rten[0]}][line:{rten[1]}] - %(levelname)s: %(message)s")

        # 文件输出渠道
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # 创建目录&.log文件
        log_dir = os.path.join(os.getcwd(), "logs")
        lt = time.localtime(time.time())
        yearmonth = time.strftime('%Y%m', lt)
        day = time.strftime('%d', lt)
        full_path = os.path.join(log_dir, yearmonth)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        log_path = os.path.join(full_path, day + ".log")

        file_handler = logging.FileHandler(log_path, encoding=encoding)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        @wraps(func)
        def inner(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                logger.info(f"func: {func.__name__} {args} -> {res}")
                return res
            except Exception as err:
                logger.error(f"func: {func.__name__} {args} -> {err}")
                return err

        return inner

    return timelog


