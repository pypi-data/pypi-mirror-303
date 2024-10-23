"""
A high-performance data profiling library oriented towards exploratory data analysis
"""

from __future__ import annotations
import typing
from . import ac
from . import afd
from . import aind
from . import ar
from . import cfd
from . import data_types
from . import dd
from . import dynamic_fd_verification
from . import fd
from . import fd_verification
from . import gfd_verification
from . import ind
from . import mfd_verification
from . import od
from . import pfd
from . import statistics
from . import ucc
from . import ucc_verification

__all__ = [
    "Algorithm",
    "ConfigurationError",
    "ac",
    "afd",
    "afd_verification",
    "aind",
    "ar",
    "aucc_verification",
    "cfd",
    "data_types",
    "dd",
    "dynamic_fd_verification",
    "fd",
    "fd_verification",
    "gfd_verification",
    "ind",
    "mfd_verification",
    "od",
    "od_module",
    "pfd",
    "statistics",
    "ucc",
    "ucc_verification",
]

class Algorithm:
    def execute(self, **kwargs) -> None:
        """
        Process data.
        """

    def get_description(self, option_name: str) -> str:
        """
        Get description of an option.
        """

    def get_needed_options(self) -> set[str]:
        """
        Get names of options the algorithm requires to be set at the moment.
        This option is only expected to be used by Python scripts in which it is
        easier to set all options one by one. For normal use, you may set the
        algorithms' options using keyword arguments of the load_data and execute
        methods.
        """

    def get_option_type(self, option_name: str) -> tuple:
        """
        Get info about the option's type.
        """

    def get_opts(self) -> dict[str, typing.Any]:
        """
        Get option values represented as the closest Python type
        """

    def get_possible_options(self) -> set[str]:
        """
        Get names of options the algorithm may request.
        """

    def load_data(self, **kwargs) -> None:
        """
        Load data for execution
        """

    def set_option(self, option_name: str, option_value: typing.Any = None) -> None:
        """
        Set option value. Passing None means setting the default value.
        This option is only expected to be used by Python scripts in which it is
        easier to set all options one by one. For normal use, you may set the
        algorithms' options using keyword arguments of the load_data and execute
        methods.
        """

class ConfigurationError(ValueError):
    pass

afd_verification = fd_verification
aucc_verification = ucc_verification
od_module = od
