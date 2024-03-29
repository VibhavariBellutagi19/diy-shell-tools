""" This module contains the BaseCommand class,
which is an abstract class that defines the interface for all the"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.main.input_source.base_source import BaseSource


class BaseCommand(ABC):
    """Base class for all commands"""

    def __init__(self, options: list[str] = None):
        self.options = options

    @abstractmethod
    def execute(self, input_source: BaseSource) -> int | tuple:
        """Abstract method to execute the command"""

    @abstractmethod
    def validate_options(self):
        """Abstract method to validate the options"""
