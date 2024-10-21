from __future__ import annotations

import enum
import typing
from abc import abstractmethod
from collections.abc import Iterable, Sized, Iterator, Collection
from typing import Any, Optional, Protocol, TypeVar, overload

import pandas as pd


class MyMeta(type):  # implements Iterable[str] and Sized, however, explicit subclassing breaks pandas isinstance checks
    def __new__(cls, name, bases, dct):
        cli = super().__new__(cls, name, bases, dct)
        cli.value_map = {k: v for k, v in dct.items() if not str.startswith(k, '_') and type(v) is str}
        cli.values = list(cli.value_map.values())
        return cli

    def __getitem__(self, key) -> str:
        if key in self.value_map:
            return self.value_map[key]
        elif key in self.values:
            return key

    def __len__(self) -> int:
        return len(self.value_map)

    def __iter__(self) -> Iterator[str]:
        return iter(self.values)

    def derive_enum(cls, name: Optional[str] = None) -> typing.Type[enum.Enum]:
        return enum.Enum(cls.__name__[:-1] if name is None else name, cls.value_map)


class StringEnumeration(metaclass=MyMeta):
    pass


K = TypeVar('K')
V = TypeVar('V', covariant=True)


class SlimMapping(Protocol[K, V]):
    @abstractmethod
    def __contains__(self, __x: object) -> bool: ...

    @abstractmethod
    def __getitem__(self, item: K) -> V:  ...


class Copyable(Protocol):

    @abstractmethod
    def __copy__(self) -> typing.Self: ...


T = TypeVar('T')


def take_first(arg: Iterable[T]) -> Optional[T]:
    return next(iter(arg), None)


def intersection(a: Optional[Iterable[T]], b: Optional[Iterable[T]]) -> set[T]:
    if a is None or b is None:
        return set()
    else:
        return set(a) & set(b)


def symmetric_difference(a: Optional[Iterable[T]], b: Optional[Iterable[T]]) -> tuple[set[T], set[T]]:
    if a is None and b is None:
        return set(), set()
    elif a is None:
        return set(), set(b)
    elif b is None:
        return set(a), set()
    else:
        a, b = set(a), set(b)
        return a - b, b - a


def mangle_arg_to(arg: None | str | Iterable[T], cls: Any, rm_duplicates=False, preserve_order=True,
                  preserve_none=False) -> Collection[T]:
    if arg is None:
        return arg if preserve_none else cls()
    elif not type(arg) is str and isinstance(arg, Iterable):
        if rm_duplicates:
            if not preserve_order:
                return cls(set(arg))
            elif preserve_order:
                s = set()
                return cls(
                    (i for i in arg if (i not in s) and (s := s | {i})))  # the things I do for an (almost) one-liner
        else:
            return cls(arg)
    else:
        return cls((arg,))


def mangle_arg_to_set(arg, **kwargs) -> Collection[T]:
    return mangle_arg_to(arg, set, **kwargs)


def mangle_arg_to_list(arg, rm_duplicates=True, preserve_order=True, **kwargs) -> Collection[T]:
    return mangle_arg_to(arg, list, rm_duplicates=rm_duplicates, preserve_order=preserve_order, **kwargs)


def mangle_arg_to_tuple(arg, rm_duplicates=True, preserve_order=True, **kwargs) -> Collection[T]:
    return mangle_arg_to(arg, tuple, rm_duplicates=rm_duplicates, preserve_order=preserve_order, **kwargs)


def assert_in(items: Iterable[Any], allowed: Collection[Any]):
    assert all(i in allowed for i in items)


def mangle_arg_with_bool_fallback(mangler, arg: None | str | Iterable[T], if_true=None, if_false=None,
                                  treat_none_as_false=True, **kwargs) -> Collection[T] | Collection[str]:
    if arg is None and treat_none_as_false:
        arg = if_false
    elif isinstance(arg, bool):
        arg = if_true if arg else if_false
    return mangler(arg, **kwargs)


TimeIndexer = bool | pd.Timestamp | Collection[pd.Timestamp] | slice
StrIndexer = bool | str | Collection[str] | slice


def str_indexer_to_pandas(strs: StrIndexer) -> list[str] | slice | str:
    if not strs:
        strs = []
    elif strs is True:
        strs = slice(None)
    elif isinstance(strs, str):
        return [strs]
    return strs


E = TypeVar('E', bound=enum.Enum)


@overload
def enumize(enum_cls: type[E], arg: str | E) -> E: ...


@overload
def enumize(enum_cls: type[E], arg: Set[str | E]) -> set[E]: ...


@overload
def enumize(enum_cls: type[E], arg: Collection[str | E]) -> list[E]: ...


def enumize(enum_cls: type[E], arg: str | E | Collection[str | E]) -> E | list[E] | set[E]:
    if isinstance(arg, Set):
        return {enumize(enum_cls, e) for e in arg}
    elif isinstance(arg, Collection):
        return [enumize(enum_cls, e) for e in arg]
    else:
        return arg if isinstance(arg, enum_cls) else enum_cls(arg)
