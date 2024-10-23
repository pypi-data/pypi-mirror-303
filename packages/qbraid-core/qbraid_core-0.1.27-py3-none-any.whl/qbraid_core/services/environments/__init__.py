# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module providing utilities for interfacing with qBraid environments

.. currentmodule:: qbraid_core.services.environments

Classes
----------

.. autosummary::
   :toctree: ../stubs/

   EnvironmentManagerClient

Exceptions
------------

.. autosummary::
   :toctree: ../stubs/

   EnvironmentServiceRequestError
   EnvironmentServiceRuntimeError

"""
from .client import EnvironmentManagerClient
from .create import create_local_venv
from .exceptions import EnvironmentServiceRequestError, EnvironmentServiceRuntimeError
from .kernels import add_kernels, get_all_kernels, remove_kernels
from .magic import add_magic_config, remove_magic_config
from .paths import (
    get_default_envs_paths,
    get_env_path,
    get_next_tmpn,
    get_tmp_dir_names,
    which_python,
)
from .state import install_status_codes, update_install_status
from .validate import is_valid_env_name, is_valid_slug

__all__ = [
    "EnvironmentManagerClient",
    "EnvironmentServiceRequestError",
    "EnvironmentServiceRuntimeError",
    "create_local_venv",
    "add_magic_config",
    "remove_magic_config",
    "get_default_envs_paths",
    "get_env_path",
    "get_next_tmpn",
    "get_tmp_dir_names",
    "which_python",
    "install_status_codes",
    "update_install_status",
    "is_valid_env_name",
    "is_valid_slug",
    "get_all_kernels",
    "add_kernels",
    "remove_kernels",
]
