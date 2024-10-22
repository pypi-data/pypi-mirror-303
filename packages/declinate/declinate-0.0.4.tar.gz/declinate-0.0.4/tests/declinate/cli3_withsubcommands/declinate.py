# Copyright 2022 - 2024 Ternaris
# SPDX-License-Identifier: Apache-2.0
"""Test minimal CLI."""

from __future__ import annotations


def command(**kwargs: int) -> int:
    """Minimal CLI.

    Args:
        kwargs: Allargs.

    Returns:
        Exit code.

    """
    assert kwargs
    return 0


async def subcommand(number: int) -> int:
    """Execute subcommand.

    Args:
        number: A number.

    Returns:
        Exit code.

    """
    assert isinstance(number, int)
    return 0


COMMAND = command
SUBCOMMANDS = [subcommand]
