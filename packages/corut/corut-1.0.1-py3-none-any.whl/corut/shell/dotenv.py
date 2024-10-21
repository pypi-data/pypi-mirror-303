#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
It is aimed to read and update the .env file in a simple and effective way.
"""

__all__ = ('Dotenv',)

import os
from pathlib import Path
from typing import Optional


class Dotenv(dict):
    """
    A class for loading and persisting environment variables from a .env file.

    Inherits from the dict class, allowing environment variables to be accessed
    using dictionary-like syntax.

    Attributes:
        @param path (str): The path to the .env file.
    
    An example .env file could be as follows
    
    # DB Settings
    DB_ENGINE=db_engine
    DB_NAME=db_name
    DB_USER=db_user
    DB_PASSWORD=db_password#There is an explanation here
    DB_HOST=127.0.0.1
    DB_PORT=5432
    
    # Other Settings
    EXAMPLE="This is an example"#There is an explanation here
    EXAMPLE2='This is an example 2'#There is an explanation here
    
    
    If used as below, it adds key and value to the .env file.
    data = Dotenv(file_path)
    data[key] = value
    
    If used as below, it deletes the key and value given in the .env file.
    data = Dotenv(file_path)
    del data[key_name]
    """
    
    def __init__(
            self,
            path: Path,
            encoding: Optional[str] = "utf-8",
            shell_override: bool = True
    ):
        self.__file_path = path
        self.__encoding = encoding
        self.__shell_override = shell_override
        super().__init__(**self.__read_file())
    
    def __read_file(self) -> dict:
        data = {}
        with open(self.__file_path, 'r', encoding=self.__encoding) as f:
            for line in f.readlines():
                data.update(self.__parse_line(line))
        self.__update_environ(data)
        return data
    
    def __update_environ(
            self, data: dict[str, str], remove_list: list[str] = None
    ) -> None:
        if self.__shell_override:
            os.environ.update(data)
        if remove_list:
            for item in remove_list:
                if item in os.environ:
                    os.environ.pop(item)
    
    @staticmethod
    def __parse_line(line: str) -> dict[str, str]:
        if not line.lstrip().startswith('#') and line.lstrip():
            quote_delimit = max(
                line.find('\'', line.find('\'') + 1),
                line.find('"', line.rfind('"')) + 1
            )
            comment_delimit = line.find('#', quote_delimit)
            line = line[:comment_delimit]
            key, value = map(
                lambda x: x.strip().strip('\'').strip('"'),
                line.split('=', 1)
            )
            return {key: value}
        return {}
    
    def __update_env_file(self) -> None:
        with open(self.__file_path, 'w', encoding=self.__encoding) as f:
            for k, v in self.items():
                f.write(f'{k}={v}\n')
    
    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.__update_env_file()
        self.__update_environ({k: v for k, v in self.items()})
    
    def __setitem__(self, key: str, value: str) -> None:
        super().__setitem__(key, value)
        self.__update_env_file()
        self.__update_environ({key: value})
    
    def __delitem__(self, key: str) -> None:
        if key in self.keys():
            super().__delitem__(key)
        self.__update_env_file()
        self.__update_environ(data={}, remove_list=[key])
