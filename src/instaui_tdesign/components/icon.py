from __future__ import annotations

from typing import Optional

from instaui import custom, ui

_prefix: Optional[str] = None


class Icon(custom.element):
    def __init__(
        self,
        name: str,
        *,
        size: Optional[str] = None,
        color: Optional[str] = None,
    ):
        super().__init__("t-icon")
        self.props(
            {
                "name": name,
                "size": size,
                "color": color,
                "prefix": _prefix,
            }
        )

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self


def _reset_prefix(value: str):
    global _prefix
    _prefix = value
