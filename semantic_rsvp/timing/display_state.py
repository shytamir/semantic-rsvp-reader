from __future__ import annotations

from dataclasses import dataclass


QUOTE_BOUNDARY_NONE = "none"
QUOTE_BOUNDARY_OPEN = "open"
QUOTE_BOUNDARY_CLOSE = "close"
QUOTE_BOUNDARY_BOTH = "both"

_OPENING_QUOTES = {"\u201c"}
_CLOSING_QUOTES = {"\u201d"}
_STRAIGHT_QUOTE = '"'
_OPENING_PARENTHESES = {"(": ")", "[": "]"}
_CLOSING_PARENTHESES = {")", "]"}


@dataclass(frozen=True)
class DisplayState:
    in_quote: bool = False
    quote_boundary: str = QUOTE_BOUNDARY_NONE
    in_parenthetical: bool = False
    parenthetical_depth: int = 0


@dataclass
class DisplayStateTracker:
    quote_is_open: bool = False
    parenthetical_depth: int = 0

    def annotate(self, text: str) -> DisplayState:
        quote_before = self.quote_is_open
        depth_before = self.parenthetical_depth
        quote_opened = False
        quote_closed = False
        saw_parenthetical = False

        for char in text:
            if char in _OPENING_QUOTES:
                self.quote_is_open = True
                quote_opened = True
                continue
            if char in _CLOSING_QUOTES:
                self.quote_is_open = False
                quote_closed = True
                continue
            if char == _STRAIGHT_QUOTE:
                if self.quote_is_open:
                    self.quote_is_open = False
                    quote_closed = True
                else:
                    self.quote_is_open = True
                    quote_opened = True
                continue
            if char in _OPENING_PARENTHESES:
                self.parenthetical_depth += 1
                saw_parenthetical = True
                continue
            if char in _CLOSING_PARENTHESES:
                if self.parenthetical_depth > 0:
                    self.parenthetical_depth -= 1
                saw_parenthetical = True

        quote_boundary = _quote_boundary(quote_opened, quote_closed)
        return DisplayState(
            in_quote=quote_before or quote_opened or quote_closed or self.quote_is_open,
            quote_boundary=quote_boundary,
            in_parenthetical=depth_before > 0
            or saw_parenthetical
            or self.parenthetical_depth > 0,
            parenthetical_depth=max(self.parenthetical_depth, 0),
        )


def _quote_boundary(opened: bool, closed: bool) -> str:
    if opened and closed:
        return QUOTE_BOUNDARY_BOTH
    if opened:
        return QUOTE_BOUNDARY_OPEN
    if closed:
        return QUOTE_BOUNDARY_CLOSE
    return QUOTE_BOUNDARY_NONE
