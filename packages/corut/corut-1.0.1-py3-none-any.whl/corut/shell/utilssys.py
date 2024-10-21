#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
It is aimed to provide convenience by performing
many operations on the operating system.
"""

__all__ = (
    'run_cmd',
    'run_cmd_2',
    'SysReader',
)

import sys
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT, CalledProcessError, check_output
from threading import Lock, Thread


def run_cmd(
        command, password=None, encoding='utf-8', print_output_status=True,
        **kwargs
):
    data = ''
    try:
        with Popen(
                command,
                stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True,
                encoding=encoding, universal_newlines=True, **kwargs
        ) as process:
            if password:
                process.stdin.write(f'{password}\n')
                process.stdin.flush()
            if print_output_status:
                for line in process.stdout:
                    print(line, end='')
                    data += line
    except Exception as error:
        print('Subprocess Popen Error:', error)
    return data


def run_cmd_2(
        cmd, do_combine=False, return_binary=False, encoding='utf-8', **kwargs
):
    try:
        stdout = check_output(
            cmd,
            stderr=STDOUT,
            universal_newlines=return_binary is False,
            encoding=encoding,
            **kwargs
        )
    except CalledProcessError as cpe:
        stdout = cpe.output
        return_code = cpe.returncode
    else:
        return_code = 0
    if return_code != 0:
        raise Exception(f"Command failed with ({return_code}):{cmd}\n{stdout}")
    if return_binary or do_combine:
        return stdout
    return stdout.strip('\n').split('\n')


class _SysReader:
    def __init__(self, data, lock):
        self.__lock = lock
        self.data = data
    
    @staticmethod
    def __add_date_time_to_line(text: str) -> str:
        return f'[{datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")}]  {text}\n'
    
    def write(self, line):
        line = line.strip()
        if len(line) > 0:
            self.data_append(line)
    
    def data_append(self, txt):
        self.__lock.acquire()
        self.data.append(self.__add_date_time_to_line(txt))
        self.__lock.release()
    
    def flush(self):
        pass


class SysReader:
    def __init__(self):
        self.__lock = None
        self.__thread = None
        self.data = []
    
    def __sys_reader_function(self):
        sys.stdout = _SysReader(self.data, self.__lock)
        sys.stderr = _SysReader(self.data, self.__lock)
    
    def start(self):
        self.__lock = Lock()
        self.__thread = Thread(
            target=self.__sys_reader_function,
            name='SYS READER',
            daemon=True
        )
        self.__thread.start()
    
    def stop(self):
        if self.__thread:
            self.__thread.join()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.__thread = None
    
    def data_clean(self):
        self.__lock.acquire()
        self.data.clear()
        self.data.append('')
        self.__lock.release()
