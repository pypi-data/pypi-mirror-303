# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MessageParam",
    "ContentUnionMember2",
    "ContentUnionMember2Content",
    "ContentUnionMember2ContentModel",
    "ContentUnionMember2ContentModelImageURL",
]


class ContentUnionMember2Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class ContentUnionMember2ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class ContentUnionMember2ContentModel(TypedDict, total=False):
    image_url: Required[ContentUnionMember2ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


ContentUnionMember2: TypeAlias = Union[ContentUnionMember2Content, ContentUnionMember2ContentModel]

_MessageParamReservedKeywords = TypedDict(
    "_MessageParamReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MessageParam(_MessageParamReservedKeywords, total=False):
    content: Required[Union[str, List[str], Iterable[ContentUnionMember2]]]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]
