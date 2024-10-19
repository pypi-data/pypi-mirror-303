# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExecutionPatchParams"]


class ExecutionPatchParams(TypedDict, total=False):
    task_id: Required[str]

    status: Required[Literal["queued", "starting", "running", "awaiting_input", "succeeded", "failed", "cancelled"]]
