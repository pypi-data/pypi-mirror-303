from typing import overload
from enum import Enum
import typing

import System
import System.Runtime.ExceptionServices


class HandleProcessCorruptedStateExceptionsAttribute(System.Attribute):
    """Obsoletions.CorruptedStateRecoveryMessage"""

    def __init__(self) -> None:
        ...


class ExceptionDispatchInfo(System.Object):
    """This class has no documentation."""

    @property
    def source_exception(self) -> System.Exception:
        ...

    @staticmethod
    def capture(source: System.Exception) -> System.Runtime.ExceptionServices.ExceptionDispatchInfo:
        ...

    @staticmethod
    def set_current_stack_trace(source: System.Exception) -> System.Exception:
        """
        Stores the current stack trace into the specified Exception instance.
        
        :param source: The unthrown Exception instance.
        :returns: The  exception instance.
        """
        ...

    @staticmethod
    def set_remote_stack_trace(source: System.Exception, stack_trace: str) -> System.Exception:
        """
        Stores the provided stack trace into the specified Exception instance.
        
        :param source: The unthrown Exception instance.
        :param stack_trace: The stack trace string to persist within . This is normally acquired from the Exception.StackTrace property from the remote exception instance.
        :returns: The  exception instance.
        """
        ...

    @overload
    def throw(self) -> None:
        ...

    @staticmethod
    @overload
    def throw(source: System.Exception) -> None:
        ...


class FirstChanceExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception(self) -> System.Exception:
        ...

    def __init__(self, exception: System.Exception) -> None:
        ...


