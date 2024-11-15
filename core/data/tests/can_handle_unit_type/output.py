"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class StructHasVoidType(BaseModel):
    """
    This struct has a unit field
    """
    model_config = ConfigDict(populate_by_name=True)

    this_is_a_unit: None = Field(alias="thisIsAUnit")

class EnumHasVoidTypeHasAUnit(BaseModel):
    EnumHasVoidTypeTypes: Literal["hasAUnit"] = "hasAUnit"
    content: None

# This enum has a variant associated with unit data
EnumHasVoidType = EnumHasVoidTypeHasAUnit
