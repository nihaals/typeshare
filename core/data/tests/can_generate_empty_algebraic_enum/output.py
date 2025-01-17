from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import Literal, Union


class AddressDetails(BaseModel):
    pass
class AddressTypes(str, Enum):
    FIXED_ADDRESS = "FixedAddress"
    NO_FIXED_ADDRESS = "NoFixedAddress"

class AddressFixedAddress(BaseModel):
    type: Literal[AddressTypes.FIXED_ADDRESS] = AddressTypes.FIXED_ADDRESS
    content: AddressDetails

class AddressNoFixedAddress(BaseModel):
    type: Literal[AddressTypes.NO_FIXED_ADDRESS] = AddressTypes.NO_FIXED_ADDRESS

Address = Union[AddressFixedAddress, AddressNoFixedAddress]
