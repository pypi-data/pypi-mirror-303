r"""Implement the event handlers."""

from __future__ import annotations

__all__ = [
    "BaseEventHandler",
    "BaseEventHandlerWithArguments",
    "ConditionalEventHandler",
    "EventHandler",
]

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from coola import objects_are_equal
from coola.utils import str_indent, str_mapping

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

    from minevent.conditions import BaseCondition


class BaseEventHandler(ABC):
    r"""Define the base class to implement an event handler.

    A child class has to implement the following methods:

        - ``handle``
        - ``equal``

    Example usage:

    ```pycon
    >>> from minevent import EventHandler
    >>> def hello_handler() -> None:
    ...     print("Hello!")
    ...
    >>> handler = EventHandler(hello_handler)
    >>> handler
    EventHandler(
      (handler): <function hello_handler at 0x...>
      (handler_args): ()
      (handler_kwargs): {}
    )
    >>> handler.handle()
    Hello!

    ```
    """

    def __eq__(self, other: object) -> bool:
        return self.equal(other)

    @abstractmethod
    def equal(self, other: Any) -> bool:
        r"""Compare two event handlers.

        Args:
            other: Specifies the other object to compare with.

        Returns:
            ``True`` if the two event handlers are equal,
                otherwise ``False``.

        Example usage:

        ```pycon
        >>> from minevent import EventHandler
        >>> def hello_handler() -> None:
        ...     print("Hello!")
        ...
        >>> handler = EventHandler(hello_handler)
        >>> handler.equal(EventHandler(hello_handler))
        True
        >>> handler.equal(EventHandler(print, handler_args=["Hello!"]))
        False

        ```
        """

    @abstractmethod
    def handle(self) -> None:
        r"""Handle the event.

        Example usage:

        ```pycon
        >>> from minevent import EventHandler
        >>> def hello_handler() -> None:
        ...     print("Hello!")
        ...
        >>> handler = EventHandler(hello_handler)
        >>> handler.handle()
        Hello!

        ```
        """


class BaseEventHandlerWithArguments(BaseEventHandler):
    r"""Define a base class to implement an event handler with positional
    and/or keyword arguments.

    A child class has to implement the ``equal`` method.

    Args:
        handler: Specifies the handler.
        handler_args: Specifies the positional arguments of the
            handler.
        handler_kwargs: Specifies the arbitrary keyword arguments of
            the handler.

    Example usage:

    ```pycon
    >>> from minevent import EventHandler
    >>> def hello_handler() -> None:
    ...     print("Hello!")
    ...
    >>> handler = EventHandler(hello_handler)
    >>> handler
    EventHandler(
      (handler): <function hello_handler at 0x...>
      (handler_args): ()
      (handler_kwargs): {}
    )
    >>> handler.handle()
    Hello!
    >>> handler = EventHandler(print, handler_args=["Hello!"])
    >>> handler.handle()
    Hello!

    ```
    """

    def __init__(
        self,
        handler: Callable,
        handler_args: Sequence | None = None,
        handler_kwargs: dict | None = None,
    ) -> None:
        if not callable(handler):
            msg = f"handler is not callable: {handler}"
            raise TypeError(msg)
        self._handler = handler
        self._handler_args = tuple(handler_args or ())
        self._handler_kwargs = handler_kwargs or {}

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "handler": self._handler,
                    "handler_args": self._handler_args,
                    "handler_kwargs": self._handler_kwargs,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    @property
    def handler(self) -> Callable:
        r"""The handler."""
        return self._handler

    @property
    def handler_args(self) -> tuple:
        r"""Variable length argument list of the handler."""
        return self._handler_args

    @property
    def handler_kwargs(self) -> dict:
        r"""Arbitrary keyword arguments of the handler."""
        return self._handler_kwargs

    def handle(self) -> None:
        self._handler(*self._handler_args, **self._handler_kwargs)


class EventHandler(BaseEventHandlerWithArguments):
    r"""Implement a simple event handler.

    Example usage:

    ```pycon
    >>> from minevent import EventHandler
    >>> def hello_handler() -> None:
    ...     print("Hello!")
    ...
    >>> handler = EventHandler(hello_handler)
    >>> handler
    EventHandler(
      (handler): <function hello_handler at 0x...>
      (handler_args): ()
      (handler_kwargs): {}
    )
    >>> handler.handle()
    Hello!

    ```
    """

    def equal(self, other: Any) -> bool:
        if not isinstance(other, EventHandler):
            return False
        return (
            objects_are_equal(self.handler, other.handler)
            and objects_are_equal(self.handler_args, other.handler_args)
            and objects_are_equal(self.handler_kwargs, other.handler_kwargs)
        )


class ConditionalEventHandler(BaseEventHandlerWithArguments):
    r"""Implement a conditional event handler.

    The handler is executed only if the condition is ``True``.

    Args:
        handler: Specifies the handler.
        condition: Specifies the condition for this event handler.
            The condition should be callable without arguments.
        handler_args: Specifies the positional arguments of the
            handler.
        handler_kwargs: Specifies the arbitrary keyword arguments of
            the handler.

    Example usage:

    ```pycon
    >>> from minevent import ConditionalEventHandler, PeriodicCondition
    >>> def hello_handler() -> None:
    ...     print("Hello!")
    ...
    >>> handler = ConditionalEventHandler(hello_handler, PeriodicCondition(freq=3))
    >>> handler
    ConditionalEventHandler(
      (handler): <function hello_handler at 0x...>
      (handler_args): ()
      (handler_kwargs): {}
      (condition): PeriodicCondition(freq=3, step=0)
    )
    >>> handler.handle()
    Hello!
    >>> handler.handle()
    >>> handler.handle()
    >>> handler.handle()
    Hello!

    ```
    """

    def __init__(
        self,
        handler: Callable,
        condition: BaseCondition,
        handler_args: Sequence | None = None,
        handler_kwargs: dict | None = None,
    ) -> None:
        super().__init__(handler=handler, handler_args=handler_args, handler_kwargs=handler_kwargs)
        self._condition = condition

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {
                    "handler": self._handler,
                    "handler_args": self._handler_args,
                    "handler_kwargs": self._handler_kwargs,
                    "condition": self._condition,
                }
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    @property
    def condition(self) -> BaseCondition:
        r"""The condition."""
        return self._condition

    def equal(self, other: Any) -> bool:
        if not isinstance(other, ConditionalEventHandler):
            return False
        return (
            objects_are_equal(self.handler, other.handler)
            and objects_are_equal(self.handler_args, other.handler_args)
            and objects_are_equal(self.handler_kwargs, other.handler_kwargs)
            and objects_are_equal(self.condition, other.condition)
        )

    def handle(self) -> None:
        if self._condition.evaluate():
            super().handle()
