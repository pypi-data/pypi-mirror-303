#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Developed to update and log all existing Python 3rd party packages.
"""

__all__ = (
    'get_all_packages',
    'update_packages',
    'delete_packages',
)

import sys
from subprocess import Popen, PIPE
from typing import List

from .utilssys import run_cmd


def get_all_packages(executable_path: str = sys.executable) -> List[str]:
    """Pip Returns the list of packages.
    
    :param executable_path: The existing executable environment or
                            a different environment is selected.
    :return: Returns only 3rd Party package list by name.
    """
    process = Popen([executable_path, "-m", "pip", "list"], stdout=PIPE)
    output, _ = process.communicate()
    packages = output.decode().splitlines()
    if packages.__len__() > 2:
        return [i.split(' ')[0] for i in packages[2:]]
    return []


def update_packages(
        packing_list: List[str],
        executable_path: str = sys.executable,
) -> None:
    """
    Package install or update is done via pip.
    
    :param packing_list: 3rd Party package names to be updated
    :param executable_path: Environment path to for update.
    """
    packages = ' '.join(packing_list)
    run_cmd(f"{executable_path} -m pip install -U pip wheel setuptools")
    run_cmd(f"{executable_path} -m pip install -U {packages}")


def delete_packages(
        packing_list: List[str],
        executable_path: str = sys.executable,
) -> None:
    """
    Package uninstallation is done via pip.

    :param packing_list: 3rd Party package names to be updated
    :param executable_path: Environment path to for update.
    """
    
    for package in packing_list:
        run_cmd(f"{executable_path} -m pip uninstall {package} -y")
