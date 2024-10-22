# Generated code. Do not modify.
# flake8: noqa: F401, F405, F811

from __future__ import annotations

import enum
import typing

from pydivkit.core import BaseDiv, Expr, Field


# Scrolls scrollable container from current position by `item_count` or by
# `offset`, if both provided scroll action will be combined, negative numbers
# associated with backward scroll.
class DivActionScrollBy(BaseDiv):

    def __init__(
        self, *,
        type: str = "scroll_by",
        animated: typing.Optional[typing.Union[Expr, bool]] = None,
        id: typing.Optional[typing.Union[Expr, str]] = None,
        item_count: typing.Optional[typing.Union[Expr, int]] = None,
        offset: typing.Optional[typing.Union[Expr, int]] = None,
        overflow: typing.Optional[typing.Union[Expr, DivActionScrollByOverflow]] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            type=type,
            animated=animated,
            id=id,
            item_count=item_count,
            offset=offset,
            overflow=overflow,
            **kwargs,
        )

    type: str = Field(default="scroll_by")
    animated: typing.Optional[typing.Union[Expr, bool]] = Field(
        description=(
            "If `true` (default value) scroll will be animated, else "
            "not."
        ),
    )
    id: typing.Union[Expr, str] = Field(
        description="Identifier of the view that is going to be manipulated.",
    )
    item_count: typing.Optional[typing.Union[Expr, int]] = Field(
        description=(
            "Count of container items to scroll, negative value is "
            "associated with backwardscroll."
        ),
    )
    offset: typing.Optional[typing.Union[Expr, int]] = Field(
        description=(
            "Distance to scroll measured in `dp` from current position, "
            "negative value isassociated with backward scroll. "
            "Applicable only in `gallery`."
        ),
    )
    overflow: typing.Optional[typing.Union[Expr, DivActionScrollByOverflow]] = Field(
        description=(
            "Specifies how navigation will occur when the boundary "
            "elements arereached:`clamp` — Transition will stop at the "
            "boundary element (defaultvalue);`ring` — Transition will be "
            "to the beginning or the end depending on thecurrent "
            "element."
        ),
    )


class DivActionScrollByOverflow(str, enum.Enum):
    CLAMP = "clamp"
    RING = "ring"


DivActionScrollBy.update_forward_refs()
