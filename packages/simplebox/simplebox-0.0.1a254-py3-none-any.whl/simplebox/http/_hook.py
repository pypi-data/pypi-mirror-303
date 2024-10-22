#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Callable, Optional, Any, Union

__all__ = []


class HookSendBefore:
    """
    run at the http send request before
    """

    def __init__(self, run: Callable[[Optional[dict]], Optional[dict]], order: int = 0):
        self.__run: Callable[[Optional[dict]], Optional[dict]] = run
        self.__order: int = order

    def __eq__(self, other):
        return self.__run == other.__run and self.__order == other.__order

    def __hash__(self):
        return hash(self.__run) + self.__order

    def __str__(self):
        return f"{self.__run.__name__}:{self.__order}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.__order < other.__order

    def run(self, kwargs) -> Optional[dict]:
        return self.__run(kwargs)


class HookSendAfter:
    """
    run at the http send request before
    """

    def __init__(self, run: Callable[[Any], Any], order: int = 0):
        """
        :param run: it is a callback function, http request finish will call,
                    and the response of the request will be injected into the callback function.
        :param order: the order in which they are executed.
        """
        self.__run: Callable[[Any], Any] = run
        self.__order: int = order

    def __eq__(self, other):
        return self.__run == other.__run and self.__order == other.__order

    def __hash__(self):
        return hash(self.__run) + self.__order

    def __str__(self):
        return f"{self.__run.__name__}:{self.__order}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.__order < other.__order

    def run(self, response) -> Any:
        return self.__run(response)


def _filter_hook(hooks, excepted_type: type) -> list:
    hooks_list = []
    if isinstance(hooks, excepted_type):
        hooks_list.append(hooks)
    elif isinstance(hooks, list):
        hooks_list.extend((hook for hook in hooks if isinstance(hook, excepted_type)))
    return hooks_list


Hooks = Union[list[Union[HookSendBefore, HookSendAfter]], Union[HookSendBefore, HookSendAfter]]
