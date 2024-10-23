"""
Nodal Structure in StructMSIG
"""
import base64
from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from OpenSSL import crypto

from structmsig.data_model import StructData, NodalSig

def sign(
    signer: str,
    data: StructData,
    key: str,
    scope : list[str] = None,
    out: bool = False) -> NodalSig:
    """Signing data with scope specifed by signer

    Args:
        signer (str): name of signer
        data (StructData): structured data to be signed
        key (str): path of PEM-formatted private key of signer
        scope (list[str], optional): keys of data items in structured data.
            Defaults to None, which means all data items will be included
        out (bool, optional): flag to output nodal and binary signatures to files

    Returns:
        NodeSig: nodal signature which includes name of signer, hex signature, and scope
    """
    nodal_sig = NodalSig(
        signer = signer,
        signature = None,
        scope = scope
    )

    # Open private key of signer
    try:
        with open(key, mode='r', encoding='utf-8') as f:
            sk_pem = f.read()
            sk = SigningKey.from_pem(sk_pem)
            f.close()
    except (FileNotFoundError) as e:
        raise FileNotFoundError(f'Failed to pen private key {key} of signer!\n{e}') from None

    # Prepare data with scope
    scope_data: bytes = b''
    try:
        data.items = sorted(data.items, key=lambda item: item.key)
        for item in data.items:
            if scope is None or item.key in scope:
                temp = base64.b64decode(item.value)
                scope_data += temp
    except (ValueError) as e:
        raise ValueError(f'Failed to prepare data with scope specified by signer!\n{e}') from None

    sig = sk.sign(scope_data)
    nodal_sig.signature = sig.hex()

    if out is True:
        with open(f"{signer}.sig", mode='wb') as f:
            f.write(sig)
            f.close()

        with open(f"{signer}.nodalsig", encoding='utf-8', mode='w') as f:
            f.write(nodal_sig.model_dump_json())
            f.close()

    return nodal_sig

def verify(data: StructData, nodal_sig: NodalSig, cert: str) -> bool:
    """Verifying nodal signature of data with scope specified by signer

    Args:
        data (StructData): structured data to be verified
        nodal_sig (NodeSig): nodal signature which includes name of singer, hex signature, and scope
        cert (str): path of PEM-formatted certificate of signer

    Returns:
        bool: verification result of nodal signature
    """
    
    # Open certificate of signer
    try:
        with open(cert, mode='r', encoding='utf-8') as f:
            cert_pem = f.read()
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
            vk = cert.get_pubkey()
            vk = crypto.dump_publickey(crypto.FILETYPE_PEM, vk)
            vk = VerifyingKey.from_pem(vk.decode('ASCII'))
            f.close()
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Failed to open certificate {cert} of signer!\n{e}') from None

    # Prepare data with scope
    scope_data: bytes = b''
    try:
        scope = nodal_sig.scope
        data.items = sorted(data.items, key=lambda item: item.key)
        for item in data.items:
            if scope is None or item.key in scope:
                temp = base64.b64decode(item.value)
                scope_data += temp
    except ValueError as e:
        raise ValueError(f'Failed to prepare data with scope specified by signer!\n{e}') from None

    try:
        sig = bytearray.fromhex(nodal_sig.signature)
        return vk.verify(sig, scope_data)
    except BadSignatureError as e:
        #raise BadSignatureError(f'Verify data {scope_data} failed!\n{e}') from None
        return False
