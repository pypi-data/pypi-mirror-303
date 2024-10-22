from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, TextIO

TERMCOLOR_GREEN = "\x1b[38;5;2m"
TERMCOLOR_RED = "\x1b[38;5;1m"
TERMCOLOR_YELLOW = "\x1b[38;5;3m"
TERMCOLOR_BLUE = "\x1b[38;5;4m"
TERMCOLOR_RESET = "\x1b[0m"
TERMCOLOR_DEFAULT = ""


class CharsBase(ABC):
    @abstractmethod
    def write_to(self, term: TermBase) -> None: ...

    @abstractmethod
    def write_ascii_to(self, term: TermBase) -> None: ...


@dataclass(frozen=True)
class Chars(CharsBase):
    string: str
    termcolor: str = TERMCOLOR_DEFAULT

    def write_to(self, term: TermBase) -> None:
        term.write(self.string, termcolor=self.termcolor)

    def write_ascii_to(self, term: TermBase) -> None:
        self.write_to(term)


@dataclass(frozen=True)
class CharsWithAsciiAlternate(CharsBase):
    string: str
    ascii_string: str
    termcolor: str = TERMCOLOR_DEFAULT

    def write_to(self, term: TermBase) -> None:
        term.write(self.string, termcolor=self.termcolor)

    def write_ascii_to(self, term: TermBase) -> None:
        term.write(self.ascii_string, termcolor=self.termcolor)


class TermBase(ABC):
    @abstractmethod
    def write(self, string: str, termcolor: str | None = None) -> None:
        raise NotImplementedError()

    @abstractmethod
    def print_line_of_chars(
        self, chars_seq: Sequence[CharsBase], indent: int = 0
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    def print_line(
        self, string: str, termcolor: str = TERMCOLOR_DEFAULT, indent: int = 0
    ) -> None:
        self.print_line_of_chars([Chars(string, termcolor=termcolor)], indent)


class BlackHole(TermBase):
    def write(self, string: str, termcolor: str | None = None) -> None:
        pass

    def print_line_of_chars(
        self, chars_seq: Sequence[CharsBase], indent: int = 0
    ) -> None:
        pass

    def close(self) -> None:
        pass

    def print_line(
        self, string: str, termcolor: str = TERMCOLOR_DEFAULT, indent: int = 0
    ) -> None:
        pass


@dataclass(frozen=True)
class Term(TermBase):
    has_color: bool
    has_unicode: bool
    stream: TextIO = sys.stdout
    indent_size: int = 2

    def _indented(self, string: str, indent: int) -> str:
        padding = indent * self.indent_size * " "
        return padding + string

    def _colored(self, string: str, termcolor: str | None) -> str:
        if self.has_color and termcolor is not None:
            return termcolor + string + TERMCOLOR_RESET
        return string

    def write(self, string: str, termcolor: str | None = None) -> None:
        self.stream.write(self._colored(string, termcolor))

    def print_line_of_chars(
        self, chars_seq: Sequence[CharsBase], indent: int = 0
    ) -> None:
        # Write indent
        self.write(self._indented("", indent))
        # Write chars
        for chars in chars_seq:
            if self.has_unicode:
                chars.write_to(self)
            else:
                chars.write_ascii_to(self)
        # Write newline
        self.write("\n")

    def close(self) -> None:
        pass  # self.stream was passed open, so don't close it


class LogFile(TermBase):
    _file = None

    def __init__(self, filename: Path, has_unicode: bool):
        self.filename = filename
        self.has_unicode = has_unicode
        self._file = filename.open("w")
        self._term = Term(has_color=False, has_unicode=has_unicode, stream=self._file)

    def write(self, string: str, termcolor: str | None = None) -> None:
        self._term.write(string, termcolor)

    def print_line_of_chars(
        self, chars_seq: Sequence[CharsBase], indent: int = 0
    ) -> None:
        self._term.print_line_of_chars(chars_seq, indent)

    def close(self) -> None:
        if self._file:
            self._file.close()

    def __del__(self) -> None:
        self.close()


@dataclass(frozen=True)
class TeeTerm(TermBase):
    terms: Sequence[TermBase]

    def write(self, string: str, termcolor: str | None = None) -> None:
        for term in self.terms:
            term.write(string, termcolor)

    def print_line_of_chars(
        self, chars_seq: Sequence[CharsBase], indent: int = 0
    ) -> None:
        for term in self.terms:
            term.print_line_of_chars(chars_seq, indent)

    def close(self) -> None:
        for term in self.terms:
            term.close()


class Message(ABC):
    @abstractmethod
    def print_to(self, term: TermBase, indent: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def count_leaf_messages(self) -> int:
        raise NotImplementedError


@dataclass(frozen=True)
class StrMsg(Message):
    string: str
    termcolor: str = TERMCOLOR_DEFAULT

    def print_to(self, term: TermBase, indent: int) -> None:
        term.print_line(self.string, termcolor=self.termcolor, indent=indent)

    def count_leaf_messages(self) -> int:
        return 1


class NullMsg(Message):
    def print_to(self, term: TermBase, indent: int) -> None:
        pass

    def count_leaf_messages(self) -> int:
        return 0


@dataclass(frozen=True)
class ConcatMsgs(Message):
    messages: Sequence[Message]

    def print_to(self, term: TermBase, indent: int) -> None:
        for message in self.messages:
            message.print_to(term, indent)

    def count_leaf_messages(self) -> int:
        return sum(message.count_leaf_messages() for message in self.messages)


@dataclass(frozen=True)
class CollectedMsgs(Message):
    messages: Sequence[Message]
    header_msg: Message = NullMsg()
    footer_msg: Message = NullMsg()

    def print_to(self, term: TermBase, indent: int) -> None:
        self.header_msg.print_to(term, indent)
        ConcatMsgs(self.messages).print_to(term, indent + 1)
        self.footer_msg.print_to(term, indent)

    def count_leaf_messages(self) -> int:
        return ConcatMsgs(self.messages).count_leaf_messages()


@dataclass(frozen=True)
class PrintOnlyIfHasLeaves(Message):
    message: Message

    def print_to(self, term: TermBase, indent: int) -> None:
        if self.message.count_leaf_messages() > 0:
            self.message.print_to(term, indent)

    def count_leaf_messages(self) -> int:
        return self.message.count_leaf_messages()


def info_msg(*strings: str) -> Message:
    msgs = list(StrMsg(s, termcolor=TERMCOLOR_DEFAULT) for s in strings)
    return ConcatMsgs(msgs)


def warn_msg(*strings: str) -> Message:
    msgs = list(StrMsg(s, termcolor=TERMCOLOR_YELLOW) for s in strings)
    return ConcatMsgs(msgs)


def err_msg(*strings: str) -> Message:
    msgs = list(StrMsg(s, termcolor=TERMCOLOR_RED) for s in strings)
    return ConcatMsgs(msgs)
