"""
Data models in StructMSIG
"""
import typing
from pydantic import BaseModel

class DataItem(BaseModel):
    """
    Class represeting a data item in a structured data

    Attributes:
        key (str): name of data item
        value (bytes): base64 encoded content of data item
    """
    key: str
    value: bytes

class StructData(BaseModel):
    """
    Class represeting a structured data

    Attributes:
        items (list[DataItem]): a list of DataItem
    """
    items: list[DataItem]

class NodalSig(BaseModel):
    """
    Class represeting a nodal signature

    Attributes:
        signer (str): name of signer
        signature (str or None): hex signature if exist or None
        scope (list[str] or None): a list of keys of DataItem to define scope if exist or None
    """
    signer: str
    signature: typing.Optional[str] = None
    scope: typing.Optional[list[str]] = None

class SeqSig(BaseModel):
    """
    Class represeting a sequential signature

    Attributes:
        signatures (list[NodeSig] or None): a list of nodal signatures if exist or None
    """
    signatures: typing.Optional[list[NodalSig]] = None
