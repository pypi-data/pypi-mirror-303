"""
Utilities for Structural Multi-Signature (StructMSig)
"""
import base64
import json
from structmsig.data_model import StructData, NodalSig, SeqSig

def create_struct_data(texts: dict = None, files: dict = None) -> StructData:
    """
    Create a struct data

    Args:
        texts (dict): a dictionary representing a series of text data
        files (dict): a dictionary representing a series of file data

    Returns:
        StructData: a struct data
    """
    items = []
    if texts is not None:
        for key, value in texts.items():
            data_b64 = base64.b64encode(value.encode('utf-8')).decode('utf-8')
            items.append({"key": key, "value": data_b64})

    if files is not None:
        for key, value in files.items():
            with open(value, "rb") as file:
                data_binary = file.read()
                data_b64 = (base64.b64encode(data_binary)).decode('ascii')
                items.append({"key": key, "value": data_b64})

    return StructData(items=items)

def open_nodalsig(file: str) -> NodalSig:
    """_summary_

    Args:
        file (str): _description_

    Returns:
        NodalSig: _description_
    """
    file = open(file, encoding='utf-8', mode='r')
    json_data = file.read()
    return NodalSig.model_validate(json.loads(json_data))

def create_nodalsig(signer: str, file: str, scope : list[str] = None) -> NodalSig:
    """_summary_

    Args:
        file (str): _description_

    Returns:
        NodalSig: _description_
    """
    nodal_sig = NodalSig(
        signer = signer,
        scope = scope,
        signature = None
    )
    with open(file, mode='rb') as f:
        binary_sig = f.read()
        f.close()
        nodal_sig.signature = binary_sig.hex()
    return nodal_sig

def open_seqsig(file: str) -> SeqSig:
    """_summary_

    Args:
        file (str): _description_

    Returns:
        SeqSig: _description_
    """
    file = open(file, encoding='utf-8', mode='r')
    json_data = file.read()
    return SeqSig.model_validate(json.loads(json_data))
