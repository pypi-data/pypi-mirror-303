# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Task"
"""
  * @File    :   Task.py
  * @Time    :   2023/06/04 21:24:10
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""


from datetime import datetime
from uuid import uuid4
from enum import StrEnum
from xy_string.utils import is_empty_string
from asyncio import StreamWriter, StreamReader
from io import (
    TextIOBase,
    StringIO,
    TextIOWrapper,
)
from typing import TextIO
import logging


class EMethod(StrEnum):
    POST = "POST"
    RECEIVE = "RECEIVE"
    CLOSE = "CLOSE"


class ESTD(StrEnum):
    INPUT = "input".upper()
    OUTPUT = "output".upper()
    ERROR = "error".upper()


class InputTimeoutError(Exception):
    pass


def interrupted(signum, frame):
    raise InputTimeoutError


class Task:
    std: ESTD = ESTD.OUTPUT
    write_io: StreamWriter | TextIO | TextIOBase | StringIO | TextIOWrapper | None = (
        None
    )
    read_io: TextIO | TextIOBase | StringIO | TextIOWrapper | StreamReader | None = None

    identifier: str = uuid4().hex
    arguments: str | bytes = ""
    data: str = ""
    time: datetime = datetime.now()
    seperate_line = f""
    command_timeout: float = 2
    encoding = "utf-8"

    def __init__(
        self,
        arguments: str | bytes,
        write_io: StreamWriter
        | TextIO
        | TextIOBase
        | StringIO
        | TextIOWrapper
        | None = None,
        read_io: TextIO
        | TextIOBase
        | StringIO
        | TextIOWrapper
        | StreamReader
        | None = None,
        identifier: str = uuid4().hex,
    ):
        self.write_io = write_io
        self.read_io = read_io
        self.arguments = arguments
        self.identifier = identifier

    def seperate(self) -> str | bytes:
        if isinstance(self.seperate_line, str):
            return f"{self.seperate_line}"
        elif isinstance(self.seperate_line, bytes):
            try:
                return f"{self.seperate_line.encode(self.encoding)}"
            except:
                return f"{self.seperate_line.encode()}"
        return b"\n"

    def parse_arguments(self) -> str:
        arguments = f"{self.seperate()}{self.arguments}{self.seperate()}"
        if isinstance(arguments, bytes):
            try:
                arguments = (
                    f"{self.seperate()}{self.arguments.decode(self.encoding)}{self.seperate()}"
                    if isinstance(self.arguments, bytes)
                    else ""
                )
            except:
                try:
                    arguments = (
                        (f"{self.seperate()}{self.arguments.decode()}{self.seperate()}")
                        if isinstance(self.arguments, bytes)
                        else ""
                    )
                except:
                    arguments = ""
        if not is_empty_string(arguments) and not arguments.endswith("\n"):
            arguments = f"{arguments}\n"
        return arguments

    async def run(self):
        arguments = self.parse_arguments()
        if self.write_io:
            try:
                if isinstance(self.write_io, StreamWriter):
                    if self.encoding and isinstance(self.encoding, str):
                        self.write_io.write(arguments.encode(self.encoding))
                        await self.write_io.drain() if hasattr(
                            self.write_io, "drain"
                        ) else None
                    else:
                        self.write_io.write(arguments.encode())
                        await self.write_io.drain() if hasattr(
                            self.write_io, "drain"
                        ) else None
                else:
                    if self.write_io.writable():
                        self.write_io.write(arguments)
                        self.write_io.flush() if hasattr(
                            self.write_io, "flush"
                        ) else None
            except Exception as exception:
                logging.error(f"exception: {exception} write_io {self.write_io}")
                pass
        if self.read_io:
            try:
                if isinstance(self.read_io, StreamReader):
                    data = await self.read_io.readline()
                    if isinstance(data, bytes):
                        if self.encoding and isinstance(self.encoding, str):
                            self.data = data.decode(self.encoding)
                        else:
                            self.data = data.decode()
                else:
                    if hasattr(self.read_io, "isatty") and not self.read_io.isatty():
                        data = self.read_io.readline()
                        if isinstance(data, bytes):
                            if self.encoding and isinstance(self.encoding, str):
                                self.data = data.decode(self.encoding)
                            else:
                                self.data = data.decode()
            except Exception as exception:
                logging.error(f"exception {exception} read_io {self.read_io}")
                pass


class InputTask(Task):
    std: ESTD = ESTD.INPUT


class OutputTask(Task):
    std: ESTD = ESTD.OUTPUT


class ErrorTask(Task):
    std: ESTD = ESTD.ERROR
