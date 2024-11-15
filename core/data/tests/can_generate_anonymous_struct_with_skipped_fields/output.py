"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel
from typing import Literal, Union


class AutofilledByUsInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Us` of the `AutofilledBy` Rust enum
    """
    uuid: str
    """
    The UUID for the fill
    """

class AutofilledBySomethingElseInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `SomethingElse` of the `AutofilledBy` Rust enum
    """
    uuid: str
    """
    The UUID for the fill
    """

class AutofilledByUs(BaseModel):
    """
    This field was autofilled by us
    """
    AutofilledByTypes: Literal["Us"] = "Us"
    content: AutofilledByUsInner

class AutofilledBySomethingElse(BaseModel):
    """
    Something else autofilled this field
    """
    AutofilledByTypes: Literal["SomethingElse"] = "SomethingElse"
    content: AutofilledBySomethingElseInner

# Enum keeping track of who autofilled a field
AutofilledBy = Union[AutofilledByUs, AutofilledBySomethingElse]
