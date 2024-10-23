"""
Sequential Structure in StructMSIG
"""
import base64
from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from OpenSSL import crypto

from structmsig.data_model import StructData, SeqSig, NodalSig

def sign(
    signer: str,
    data: StructData,
    key: str,
    seq_sig: SeqSig = None,
    scope: list[str] = None,
    out: bool = False) -> SeqSig:
    """Signing data with scope specified by current signer in a sequential structure

    Args:
        signer (str): name of singer
        data (StructData): structured data to be signed
        key (str): path of PEM-formatted private key of signer
        scope (list[str], optional): a list of keys of DataItem to define scope if exist or None
        seq_sig (SeqSig, optional): sequential sinature that previous singers signed 
            in a squential structure. Defaults to None, which means current signer 
            is the first signer in this sequential structure
        out (bool, optional): flag to output sequential and binary signatures to files

    Returns:
        SeqSig: sequential signature which includes a list of nodal signatures
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
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Failed to open private key {key} of signer!\n{e}') from None

    # Prepare data with scope
    scope_data: bytes = b''
    try:
        data.items = sorted(data.items, key=lambda item: item.key)
        for item in data.items:
            if scope is None or item.key in scope:
                temp = base64.b64decode(item.value)
                scope_data += temp
        if seq_sig is not None:
            for sig in seq_sig.signatures:
                scope_data += bytearray.fromhex(sig.signature)
    except (ValueError) as e:
        raise ValueError(f'Failed to prepare data with scope specified by signer!\n{e}') from None

    sig = sk.sign(scope_data)
    nodal_sig.signature = sig.hex()

    if seq_sig is not None:
        seq_sig.signatures.append(nodal_sig)
    else:
        seq_sig = SeqSig(signatures=[nodal_sig])

    if out is True:
        with open(f"{signer}.sig", mode='wb') as f:
            f.write(sig)
            f.close()

        with open(f"{signer}.seqsig", encoding='utf-8', mode='w') as f:
            f.write(seq_sig.model_dump_json())
            f.close()

    return seq_sig

def verify(data: StructData, seq_sig: SeqSig, certs: list[str]) -> bool:
    """Verify sequential signature of data with scope specified by signers

    Args:
        data (StructData): structured data to be verified
        seq_sig (SegSig): sequential sinature which includes a list of nodal signatures of all signers in order
        certs (list[str]): path of PEM-formatted certificates of signers in order

    Returns:
        bool: verification result of sequential signature
    """
    nodal_sigs = seq_sig.signatures.copy()

    if len(nodal_sigs) != len(certs):
        raise ValueError('Numbers of signatures and certificates not match!')

    for r_nodal_sig, r_cert in zip(reversed(nodal_sigs.copy()), reversed(certs)):
        # Open certificate of signer
        try:
            with open(r_cert, mode='r', encoding='utf-8') as f:
                cert_pem = f.read()
                vk = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem).get_pubkey()
                vk_pem = crypto.dump_publickey(crypto.FILETYPE_PEM, vk)
                vk = VerifyingKey.from_pem(vk_pem.decode('ASCII'))
                f.close()
        except FileNotFoundError as e:
            raise FileNotFoundError(f'Failed to open certificate {r_cert}!\n{e}') from None

        # Prepare data with scope
        scope_data: bytes = b''
        try:
            data.items = sorted(data.items, key=lambda item: item.key)
            for item in data.items:
                if r_nodal_sig.scope is None or item.key in r_nodal_sig.scope:
                    temp = base64.b64decode(item.value)
                    scope_data += temp
            nodal_sigs.remove(r_nodal_sig)
            for nodal_sig in nodal_sigs:
                scope_data += bytearray.fromhex(nodal_sig.signature)

        except ValueError as e:
            raise ValueError(f'Failed to prepare data with scope specified by signer\n{e}!') from None

        try:
            sig = bytearray.fromhex(r_nodal_sig.signature)
            return vk.verify(sig, scope_data)
        except BadSignatureError as e:
            #raise BadSignatureError(f'Verify data {scope_data} failed!\n{e}') from None
            return False
