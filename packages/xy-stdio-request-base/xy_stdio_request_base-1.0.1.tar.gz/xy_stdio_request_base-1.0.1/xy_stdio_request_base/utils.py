# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "utils"
"""
  * @File    :   utils.py
  * @Time    :   2023/06/12 22:38:05
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

import signal


def handle(
    signum,
    frame,
):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
    raise RuntimeError


async def arun_timout(
    func,
    timeout=3,
    *args,
    **kwargs,
):
    try:
        signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
        signal.alarm(timeout)  # 设置 num 秒的闹钟
        result = await func(*args, **kwargs)
        signal.alarm(0)  # 关闭闹钟
        return result
    except RuntimeError as e:
        return None


def run_timeout(
    func,
    timeout=3,
    *args,
    **kwargs,
):
    try:
        signal.signal(
            signal.SIGALRM,
            handle,
        )  # 设置信号和回调函数
        signal.alarm(timeout)  # 设置 num 秒的闹钟
        result = func(
            *args,
            **kwargs,
        )
        signal.alarm(0)  # 关闭闹钟
        return result
    except RuntimeError as e:
        return None


def arun_decorator(timeout):
    def wrap(func):
        async def async_run(
            *args,
            **kwargs,
        ):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(timeout)  # 设置 num 秒的闹钟
                result = await func(*args, **kwargs)
                signal.alarm(0)  # 关闭闹钟
                return result
            except RuntimeError as e:
                return None

        return async_run

    return wrap


def run_decorator(timeout):
    def wrap(func):
        def run(*args, **kwargs):
            try:
                signal.signal(
                    signal.SIGALRM,
                    handle,
                )  # 设置信号和回调函数
                signal.alarm(timeout)  # 设置 num 秒的闹钟
                print("func", func)
                result = func(
                    *args,
                    **kwargs,
                )
                signal.alarm(0)  # 关闭闹钟
                return result
            except RuntimeError as e:
                return None

        return run

    return wrap
