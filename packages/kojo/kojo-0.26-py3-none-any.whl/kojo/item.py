from __future__ import annotations
from collections import UserDict, UserList
from collections.abc import Mapping
import copy
import json
import logging
from typing import Any, Iterable

DictType = Mapping[str, Any]


def _flatten(item: DictType, prefix: str = "") -> DictType:
    flat_dict: dict[str, Any] = {}
    for k, v in item.items():
        kk = prefix + "." + k if prefix else k
        if isinstance(v, Mapping):
            flat_dict.update(_flatten(v, kk).items())
        else:
            flat_dict[kk] = v
    return flat_dict


class ItemLogEntry:
    def __init__(self, _level: int, _message: str, **details: Any):
        self.level: int = _level  # logging.NOTSET .. logging.CRITICAL
        self.message: str = _message
        self.details: dict[str, Any] = details

    def __repr__(self) -> str:
        d = "".join([", {}={}".format(k, repr(v)) for k, v in self.details.items()])
        return "ItemLogEntry(logging.{}, {}{})".format(
            logging.getLevelName(self.level), repr(self.message), d
        )

    def __contains__(self, key: str) -> bool:
        return key in self.details

    def __getitem__(self, key: str) -> Any:
        return self.details[key]


class ItemLog(UserList[ItemLogEntry]):
    @property
    def level(self) -> int:
        if len(self) == 0:
            return logging.NOTSET
        return max([entry.level for entry in self])

    def log(self, _level: int, _message: str, **details: Any) -> None:
        entry = ItemLogEntry(_level, _message, **details)
        self.append(entry)

    def debug(self, _message: str, **details: Any) -> None:
        self.log(logging.DEBUG, _message, **details)

    def info(self, _message: str, **details: Any) -> None:
        self.log(logging.INFO, _message, **details)

    def warning(self, _message: str, **details: Any) -> None:
        self.log(logging.WARNING, _message, **details)

    def error(self, _message: str, **details: Any) -> None:
        self.log(logging.ERROR, _message, **details)

    def critical(self, _message: str, **details: Any) -> None:
        self.log(logging.CRITICAL, _message, **details)

    def __repr__(self) -> str:
        return "ItemLog(" + ", ".join([repr(entry) for entry in self]) + ")"

    def __add__(self, other: Iterable[ItemLogEntry]) -> ItemLog:
        if type(other) is not ItemLog:
            msg = f"TypeError: unsupported operand type(s) for +: 'ItemLog' and '{type(other).__name__}'"
            raise TypeError(msg)

        return ItemLog(list(self) + list(other))


class Item(UserDict[str, Any]):
    """
    Item extends the dictionary class.

    Item behaves like a dict but provides additional functionality

    Each Item has an log list to report comments and incidents found while
    transforming, for example validation errors or import notes.

    Each Item has an empty dict of meta when being created. meta is
    used to track import information as the name of the file or the line
    number.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.log: ItemLog = ItemLog()
        self.meta: dict[str, Any] = {}

    def __copy__(self) -> Item:
        item = Item(**copy.copy(dict(self)))
        item.log = copy.deepcopy(self.log)
        item.meta = copy.copy(self.meta)
        return item

    def __deepcopy__(self, memo: Any) -> Item:
        item = Item(**copy.deepcopy(dict(self), memo))
        item.log = copy.deepcopy(self.log)
        item.meta = copy.copy(self.meta)
        return item

    def flatten(self) -> Item:
        item = Item(_flatten(self))
        item.log = copy.deepcopy(self.log)
        item.meta = copy.copy(self.meta)
        return item


class ItemLogEntryEncoder(json.JSONEncoder):
    def default(self, entry: ItemLogEntry) -> dict[str, Any]:
        return {
            "level": entry.level,
            "message": entry.message,
            "details": entry.details,
        }


class ItemLogEncoder(json.JSONEncoder):
    def default(self, item_log: ItemLog) -> list[dict[str, Any]]:
        encoder = ItemLogEntryEncoder()
        return [encoder.default(entry) for entry in item_log]


class ItemEncoder(json.JSONEncoder):
    def default(self, item: Item) -> dict[str, Any]:
        return {
            "data": dict(item),
            "log": ItemLogEncoder().default(item.log),
            "meta": item.meta,
        }


class ItemDecoder(json.JSONDecoder):
    def decode(self, s: str) -> Item:  # type: ignore
        raw = super().decode(s)
        item = Item(raw["data"])
        item.meta = raw["meta"]
        item.log = ItemLog()
        for entry in raw["log"]:
            item.log.log(int(entry["level"]), entry["message"], **entry["details"])
        return item
