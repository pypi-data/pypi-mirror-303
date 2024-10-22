# Generated code. Do not modify.
# flake8: noqa: F401, F405, F811

from __future__ import annotations

import enum
import typing

from pydivkit.core import BaseDiv, Expr, Field


# Specifies position measured in `dp` from container's start as scroll destination.
# Applicable only in `gallery`.
class OffsetDestination(BaseDiv):

    def __init__(
        self, *,
        type: str = "offset",
        value: typing.Optional[typing.Union[Expr, int]] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            type=type,
            value=value,
            **kwargs,
        )

    type: str = Field(default="offset")
    value: typing.Union[Expr, int] = Field(
        description="Position in `dp`.",
    )


OffsetDestination.update_forward_refs()
