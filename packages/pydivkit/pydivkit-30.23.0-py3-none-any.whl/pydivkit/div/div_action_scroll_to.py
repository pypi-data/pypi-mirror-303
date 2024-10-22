# Generated code. Do not modify.
# flake8: noqa: F401, F405, F811

from __future__ import annotations

import enum
import typing

from pydivkit.core import BaseDiv, Expr, Field

from . import div_action_scroll_destination


# Scrolls or switches container to given destination provided by `destination`.
class DivActionScrollTo(BaseDiv):

    def __init__(
        self, *,
        type: str = "scroll_to",
        animated: typing.Optional[typing.Union[Expr, bool]] = None,
        destination: typing.Optional[div_action_scroll_destination.DivActionScrollDestination] = None,
        id: typing.Optional[typing.Union[Expr, str]] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            type=type,
            animated=animated,
            destination=destination,
            id=id,
            **kwargs,
        )

    type: str = Field(default="scroll_to")
    animated: typing.Optional[typing.Union[Expr, bool]] = Field(
        description=(
            "If `true` (default value) scroll will be animated, else "
            "not."
        ),
    )
    destination: div_action_scroll_destination.DivActionScrollDestination = Field(
        description=(
            "Specifies destination of scroll:`index` - scroll or switch "
            "to item with indexprovided by `value`;`offset` - scroll to "
            "position measured in `dp` fromcontainer\'s start and "
            "provided by `value`. Applicable only in `gallery`;`start` "
            "-scrolls to start of container;`end` - scrolls to end of "
            "container.."
        ),
    )
    id: typing.Union[Expr, str] = Field(
        description="Identifier of the view that is going to be manipulated.",
    )


DivActionScrollTo.update_forward_refs()
