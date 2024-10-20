# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Base"
"""
  * @File    :   Base.py
  * @Time    :   2023/06/03 10:29:52
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

import asyncio
import sys
import logging
from asyncio.queues import Queue
from asyncio import new_event_loop, AbstractEventLoop
from threading import Thread
from uuid import uuid4
from .Task import ErrorTask, InputTask, OutputTask
from xy_string.utils import is_empty_string

from asyncio import StreamWriter, StreamReader
from io import (
    TextIOBase,
    StringIO,
    TextIOWrapper,
)
from typing import TextIO


class Base:
    stdout: StreamWriter | TextIO | TextIOBase | StringIO | TextIOWrapper | StreamReader | None = (
        sys.stdout
    )
    stderr: StreamWriter | TextIO | TextIOBase | StringIO | TextIOWrapper | StreamReader | None = (
        sys.stderr
    )
    stdin: StreamWriter | TextIO | TextIOBase | StringIO | TextIOWrapper | StreamReader | None = (
        sys.stdin
    )
    identifier = uuid4().hex
    seperate_line = ""
    closed = True

    input_read_queue: Queue
    input_write_queue: Queue
    output_read_queue: Queue
    output_write_queue: Queue
    error_read_queue: Queue
    error_write_queue: Queue

    loop: AbstractEventLoop = new_event_loop()
    futures = None
    loop_sleep: float = 0.5
    task_timeout: float = 3
    command_timeout: float = 2

    std_thread: Thread = Thread()

    __input_data_list = []
    __output_data_list = []
    __error_data_list = []

    encoding = "utf-8"

    def __init__(
        self,
        stdout=sys.stdout,
        stdin=sys.stdin,
        stderr=sys.stderr,
    ):
        self.stdout = stdout
        self.stdin = stdin
        self.stderr = stderr

    async def input_write_produce(self):
        while not self.closed:
            if len(self.__input_data_list) > 0:
                input_argument = self.__input_data_list.pop()
                task = InputTask(input_argument, write_io=self.stdin)  # type: ignore
                task.encoding = self.encoding
                task.command_timeout = self.command_timeout
                task.seperate_line = self.seperate_line
                try:
                    await self.input_write_queue.put(task)
                except Exception as exception:
                    logging.error(f"input_write_produce :{exception}")
                    pass
            await asyncio.sleep(self.loop_sleep)

    async def input_read_produce(self):
        while not self.closed:
            task = InputTask("", read_io=self.stdin)  # type: ignore
            task.encoding = self.encoding
            task.command_timeout = self.command_timeout
            task.seperate_line = self.seperate_line
            try:
                await self.input_read_queue.put(task)
            except Exception as exception:
                logging.error(f"input_read_produce :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    async def output_write_produce(self):
        while not self.closed:
            if len(self.__output_data_list) > 0:
                output_argument = self.__output_data_list.pop()
                task = OutputTask(output_argument, write_io=self.stdout)  # type: ignore
                task.encoding = self.encoding
                task.command_timeout = self.command_timeout
                task.seperate_line = self.seperate_line
                try:
                    await self.output_write_queue.put(task)
                except Exception as exception:
                    logging.error(f"output_write_produce :{exception}")
                    pass
            await asyncio.sleep(self.loop_sleep)

    async def output_read_produce(self):
        while not self.closed:
            task = OutputTask("", read_io=self.stdout)  # type: ignore
            task.encoding = self.encoding
            task.command_timeout = self.command_timeout
            task.seperate_line = self.seperate_line
            try:
                await self.output_read_queue.put(task)
            except Exception as exception:
                logging.error(f"output_read_produce :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    async def error_write_produce(self):
        while not self.closed:
            if len(self.__error_data_list) > 0:
                error_argument = self.__error_data_list.pop()
                task = ErrorTask(error_argument, write_io=self.stderr)  # type: ignore
                task.command_timeout = self.command_timeout
                task.encoding = self.encoding
                task.seperate_line = self.seperate_line
                try:
                    await self.error_write_queue.put(task)
                except Exception as exception:
                    logging.error(f"error_write_produce :{exception}")
                    pass
            await asyncio.sleep(self.loop_sleep)

    async def error_read_produce(self):
        while not self.closed:
            task = ErrorTask("", read_io=self.stderr)  # type: ignore
            task.encoding = self.encoding
            task.command_timeout = self.command_timeout
            task.seperate_line = self.seperate_line
            try:
                await self.error_read_queue.put(task)
            except Exception as exception:
                logging.error(f"error_read_produce :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    async def input_write_custome(self):
        while not self.closed:
            try:
                task: InputTask = await self.input_write_queue.get()
                await task.run() if isinstance(task, InputTask) else None
            except Exception as exception:
                logging.error(f"input_write_custome :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    async def input_read_custome(self):
        while not self.closed:
            task: InputTask | None = None
            try:
                task = await self.input_read_queue.get()
                await task.run() if isinstance(task, InputTask) else None
            except Exception as exception:
                logging.error(f"input_read_custome :{exception}")
                pass
            if task and not is_empty_string(task.data):
                self.on_input(task.data, task)
            await asyncio.sleep(self.loop_sleep)

    async def output_write_custome(self):
        while not self.closed:
            task: OutputTask | None = None
            try:
                task = await self.output_write_queue.get()
                await task.run() if isinstance(task, OutputTask) else None
            except Exception as exception:
                logging.error(f"output_write_custome :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    async def output_read_custome(self):
        while not self.closed:
            task: OutputTask | None = None
            try:
                task = await self.output_read_queue.get()
                await task.run() if isinstance(task, OutputTask) else None
            except Exception as exception:
                logging.error(f"output_read_custome :{exception}")
                pass
            if isinstance(task, OutputTask) and not is_empty_string(task.data):
                self.on_output(task.data, task)
            await asyncio.sleep(self.loop_sleep)

    async def error_read_custome(self):
        while not self.closed:
            task: ErrorTask | None = None
            try:
                task = await self.error_read_queue.get()
                await task.run() if isinstance(task, ErrorTask) else None
            except Exception as exception:
                logging.error(f"error_read_custome :{exception}")
                pass
            if isinstance(task, ErrorTask) and not is_empty_string(task.data):
                self.on_error(task.data, task)
            await asyncio.sleep(self.loop_sleep)

    async def error_write_custome(self):
        while not self.closed:
            task: ErrorTask | None = None
            try:
                task = await self.error_write_queue.get()
                await task.run() if isinstance(task, ErrorTask) else None
            except Exception as exception:
                logging.error(f"error_write_custome :{exception}")
                pass
            await asyncio.sleep(self.loop_sleep)

    def _clean(self):
        self.closed = True
        try:
            self.input_write_queue.task_done() if self.input_write_queue and isinstance(
                self.input_write_queue, Queue
            ) else ""
        except:
            pass
        try:
            self.input_read_queue.task_done() if self.input_read_queue and isinstance(
                self.input_read_queue, Queue
            ) else ""
        except:
            pass
        try:
            self.output_read_queue.task_done() if self.output_read_queue and isinstance(
                self.output_read_queue, Queue
            ) else ""
        except:
            pass
        try:
            self.output_write_queue.task_done() if self.output_write_queue and isinstance(
                self.output_write_queue, Queue
            ) else ""
        except:
            pass
        try:
            self.error_read_queue.task_done() if self.error_read_queue and isinstance(
                self.error_read_queue, Queue
            ) else ""
        except:
            pass
        try:
            self.error_write_queue.task_done() if self.error_write_queue and isinstance(
                self.error_write_queue, Queue
            ) else ""
        except:
            pass
        asyncio.set_event_loop(None)
        for task in asyncio.all_tasks(self.loop):
            task.cancel()
        if self.futures:
            self.futures.cancel()
        try:
            self.loop.call_soon_threadsafe(self.loop.stop)
        except:
            pass

    async def _create(self):
        tasks = []
        self.input_read_queue = Queue()
        self.input_write_queue = Queue()
        self.output_read_queue = Queue()
        self.output_write_queue = Queue()
        self.error_read_queue = Queue()
        self.error_write_queue = Queue()
        input_read_produce_task = self.loop.create_task(self.input_read_produce())
        input_write_produce_task = self.loop.create_task(self.input_write_produce())
        output_read_produce_task = self.loop.create_task(self.output_read_produce())
        output_write_produce_task = self.loop.create_task(self.output_write_produce())
        error_read_produce_task = self.loop.create_task(self.error_read_produce())
        error_write_produce_task = self.loop.create_task(self.error_write_produce())
        input_read_custome_task = self.loop.create_task(self.input_read_custome())
        input_write_custome_task = self.loop.create_task(self.input_write_custome())
        output_read_custome_task = self.loop.create_task(self.output_read_custome())
        output_write_custome_task = self.loop.create_task(self.output_write_custome())
        error_read_custome_task = self.loop.create_task(self.error_read_custome())
        error_write_custome_task = self.loop.create_task(self.error_write_custome())
        tasks.append(input_read_produce_task)
        tasks.append(input_write_produce_task)
        tasks.append(output_read_produce_task)
        tasks.append(output_write_produce_task)
        tasks.append(error_read_produce_task)
        tasks.append(error_write_produce_task)
        tasks.append(input_read_custome_task)
        tasks.append(input_write_custome_task)
        tasks.append(output_read_custome_task)
        tasks.append(output_write_custome_task)
        tasks.append(error_read_custome_task)
        tasks.append(error_write_custome_task)
        self.futures = await asyncio.gather(*tasks)

    def _prepare(self) -> bool:
        if not self.loop or not self.loop.is_closed():
            try:
                self.loop.close()
            except Exception as exception:
                print(f"_prepare loop {exception}")
            self.loop = new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self._create())
        except Exception as exception:
            print(f"_prepare run_util_complete {exception}")
        return False

    def start(self) -> bool:
        if not self.closed or not self.stdin or not self.stdout or not self.stderr:
            return False
        if self.std_thread and not self.std_thread.is_alive():
            self.std_thread.setDaemon(False)
        self.std_thread = Thread(target=self._prepare)
        self.std_thread.daemon = True
        self.closed = False
        self.std_thread.start()
        return True

    def on_input(
        self,
        input_text: str,
        task: InputTask,
    ):
        pass

    def on_output(
        self,
        output_text: str,
        task: OutputTask,
    ):
        pass

    def on_error(
        self,
        error_text: str,
        task: ErrorTask,
    ):
        pass

    def close(self) -> bool:
        self._clean()
        return self.closed

    def write_input(
        self,
        data: str | bytes,
    ):
        if not data:
            pass
        else:
            self.__input_data_list.insert(
                0,
                data,
            )

    def write_output(
        self,
        data: str | bytes,
    ):
        if not data:
            pass
        else:
            self.__output_data_list.insert(
                0,
                data,
            )

    def write_error(
        self,
        data: str | bytes,
    ):
        if not data:
            pass
        else:
            self.__error_data_list.insert(
                0,
                data,
            )
