#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itertools


def parser_private_attr_name(clz: type, origin_name: str) -> str:
    prefix = clz.__name__
    if not prefix.startswith("_"):
        prefix = f"_{prefix}"
    return origin_name.replace(prefix, "")


def rm_underline_start_end(string: str) -> str:
    new = itertools.dropwhile(lambda value: value == "_", string)
    new = itertools.dropwhile(lambda value: value == "_", list(new)[::-1])
    return "".join(list(new)[::-1]) or string
